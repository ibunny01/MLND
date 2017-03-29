from __future__ import print_function

import gc
import math
import os

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

from image_process import ImageProcess
from svhn_bbox_loader import SVHNBboxLoader

_DEBUG = True


def _log(message, end='\r\n'):
    if _DEBUG:
        print(message, end=end)


class CNNTrainer:

    train_name = 'convolution_neural_networks_train'
    summary_dirname = None
    ckpt_saver = None
    ckpt_fname = None

    seed = 42

    def __init__(self):

        return

    def weights_init_stddev(self, d_in):
        raise NotImplementedError('Should have implemented this')

    def get_conv2d(self, name, data, patch, d_in, d_out, stride, pooling=None):
        with tf.name_scope(str('%s_namescope' % name)) as hl_scope:
            weights = tf.Variable(
                tf.truncated_normal(
                    [patch, patch, d_in, d_out],
                    stddev=self.weights_init_stddev(d_in)),
                name=str('%s_w' % name))

            biases = tf.Variable(tf.zeros([d_out]), name=str('%s_b' % name))

            layer = tf.nn.relu(
                tf.nn.conv2d(data, weights, stride, padding='SAME') + biases)

            if pooling is not None:
                layer = tf.nn.max_pool(layer, pooling, pooling, padding='SAME')

        return weights, biases, layer, hl_scope

    def get_fc(self, name, data, depth, relu=True, dropout=True,
               keep_prob=1.0):
        with tf.name_scope(str('%s_namescope' % name)) as hl_scope:
            inbound = int(data.get_shape()[1])
            weights = tf.Variable(
                tf.truncated_normal(
                    [inbound, depth],
                    stddev=math.sqrt(2.0 / inbound),
                    name=str('%s_w' % name)))
            biases = tf.Variable(tf.zeros([depth]), name=str('%s_b' % name))
            layer = tf.matmul(data, weights) + biases

            if relu is True:
                layer = tf.nn.relu(layer)

            if dropout is True:
                layer = tf.nn.dropout(layer, keep_prob, seed=self.seed)

        return weights, biases, layer, hl_scope


class SVHNTrainer(CNNTrainer):
    tf_x = None
    tf_y_ = None

    tf_keep_prob = None
    tf_l2_beta = None

    train_dataset = None
    test_dataset = None

    tf_optimizer = None
    tf_accuracy = None
    tf_loss = None

    raw_image_shape = None
    image_shape = None
    label_shape = None

    is_model_initialized = False

    pred_value = None

    def __init__(self,
                 image_shape=[None, 32, 32, 3],
                 label_shape=[None, 10],
                 train_name=None):

        # set image, label shape
        self.image_shape = image_shape
        self.label_shape = label_shape
        self.raw_image_shape = self.image_shape if image_shape[
            3] != 1 else image_shape[0:3]

        _log('input shape must be ', end='')
        _log(self.raw_image_shape)

        # set tf variables for input, labels and hyper-parameters
        self.tf_x = tf.placeholder(tf.float32, self.raw_image_shape)
        self.tf_y_ = tf.placeholder(tf.int32, self.label_shape)

        self.tf_learning_rate = tf.placeholder(tf.float32)
        self.tf_l2_beta = tf.placeholder(tf.float32)

        self.tf_keep_prob = tf.placeholder(tf.float32)

        # set this trainer name
        self.train_name = train_name if train_name else self.train_name
        self.ckpt_fname = './ckpt/%s.ckpt' % self.train_name
        self.summary_dirname = './summary/%s/' % self.train_name

        return

    def weights_init_stddev(self, d_in):
        # https://arxiv.org/pdf/1502.01852v1.pdf
        return math.sqrt(2.0 /
                         (self.image_shape[1] * self.image_shape[2] * d_in))

    def set_model(self):
        self.is_model_initialized = True

        x_input = tf.reshape(self.tf_x, [-1] + self.image_shape[1:4])

        # convolution vector definition
        w_conv1, b_conv1, l_conv1, ns_conv1 = self.get_conv2d(
            'conv1',
            data=x_input,
            patch=5,
            d_in=1,
            d_out=16,
            stride=[1, 1, 1, 1],
            pooling=[1, 2, 2, 1], )

        w_conv2, b_conv2, l_conv2, ns_conv2 = self.get_conv2d(
            'conv2',
            data=l_conv1,
            patch=5,
            d_in=16,
            d_out=32,
            stride=[1, 1, 1, 1],
            pooling=[1, 2, 2, 1], )

        w_conv3, b_conv3, l_conv3, ns_conv3 = self.get_conv2d(
            'conv3',
            data=l_conv2,
            patch=5,
            d_in=32,
            d_out=64,
            stride=[1, 1, 1, 1],
            pooling=[1, 2, 2, 1], )

        w_conv4, b_conv4, l_conv4, ns_conv4 = self.get_conv2d(
            'conv1',
            data=l_conv3,
            patch=5,
            d_in=64,
            d_out=128,
            stride=[1, 1, 1, 1],
            pooling=[1, 2, 2, 1], )

        shape = l_conv4.get_shape().as_list()
        reshape = tf.reshape(l_conv4, [-1, shape[1] * shape[2] * shape[3]])

        # weight & bias matrix depends on features
        w_fc1, b_fc1, fc1, ns_fc1 = self.get_fc(
            'fc1',
            reshape,
            256,
            relu=True,
            dropout=True,
            keep_prob=self.tf_keep_prob)

        w_fc2, b_fc2, fc2, ns_fc2 = self.get_fc(
            'fc2',
            fc1,
            128,
            relu=True,
            dropout=True,
            keep_prob=self.tf_keep_prob)

        # count of bound box
        w_len, b_len, pred_len, ns_len = self.get_fc(
            'bboxes_len', fc2, 1, relu=False, dropout=False)

        # bound boxes position
        num_labels = self.label_shape[1] - 1

        bboxes_param = [
            self.get_fc(
                str('fc3_pos_%d_%d' % (i / 4, i % 4)), fc2, 1, relu=False)
            for i in range(num_labels)
        ]

        bboxes_weights = [bboxes_param[i][0] for i in range(num_labels)]
        bboxes_biases = [bboxes_param[i][1] for i in range(num_labels)]
        bboxes_pred = tf.stack([bboxes_param[i][2] for i in range(num_labels)])

        # loss calculation
        with tf.name_scope('loss_calculation') as lc_scope:
            softmax_len = tf.nn.sparse_softmax_cross_entropy_with_logits(
                labels=tf.reshape(self.tf_y_, (-1, 25))[:, 0], logits=pred_len)
            softmax_pred = []

            for i in range(num_labels):
                softmax_pred.append(
                    tf.nn.sparse_softmax_cross_entropy_with_logits(
                        labels=tf.reshape(self.tf_y_, (-1, 25))[i + 1],
                        logits=bboxes_pred[i]))

            regularization = tf.nn.l2_loss(w_fc1) + tf.nn.l2_loss(b_fc1)
            self.tf_loss = self.tf_l2_beta * regularization
            for softmax in softmax_pred:
                self.tf_loss += tf.reduce_mean(softmax)

            tf.summary.scalar('loss', self.tf_loss)

        # loss optimizer
        with tf.name_scope('training') as tr_scope:
            self.tf_optimizer = tf.train.AdamOptimizer(
                learning_rate=self.tf_learning_rate,
                beta1=0.9,
                beta2=0.999,
                epsilon=1e-08,
                use_locking=False,
                name='Adam').minimize(self.tf_loss)

        # accuracy calculation
        with tf.name_scope('accuracy_calculation') as acc_scope:
            pred_combined = tf.stack([pred_len, bboxes_pred], axis=1)
            predict = tf.reshape(pred_combined, (-1, 25))
            is_correct_pred = tf.equal(predict,
                                       tf.reshape(self.tf_y_, (-1, 25)))
            self.tf_accuracy = tf.reduce_mean(
                tf.cast(is_correct_pred, tf.float32))
            tf.summary.scalar('accuracy', self.tf_accuracy)

            self.pred_value = predict

        # set up saver for continuous learning
        # https://www.tensorflow.org/api_docs/python/tf/train/Saver
        param_lst = [
            w_conv1,
            w_conv2,
            w_conv3,
            w_conv4,
            w_fc1,
            w_fc2,
        ]
        param_lst += [
            b_conv1,
            b_conv2,
            b_conv3,
            b_conv4,
            b_fc1,
            b_fc2,
        ]
        param_lst += [
            w_len,
            b_len,
        ]
        param_lst += [w for w in bboxes_weights]
        param_lst += [b for b in bboxes_biases]

        self.ckpt_saver = tf.train.Saver(param_lst)

    def train(self, for_training=True):
        if not self.is_model_initialized:
            raise AssertionError(
                'you must initilize model using set_model function')

        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())

            # Batching dat
            batch_size = 50
            train_size = self.train_dataset[0].shape[0]

            # hyper-parameters
            learning_rate = 3.1e-4
            l2_beta = 16e-4
            keep_prob = 0.50

            feed_train = None
            feed_accu = None
            feed_test = None

            if for_training:
                # generate tensorflow summary merged
                merged = tf.summary.merge_all()
                train_writer = tf.summary.FileWriter(self.summary_dirname,
                                                     sess.graph)

                _log('we\'re about to training using %d trainset...' %
                     self.train_dataset[0].shape[0])
                _log('trainset size : {:4d}'.format(train_size))
                _log('batch    size : {:4d}'.format(batch_size))

                _log('. : 1 training epoch')

                for epoch in range(1000):

                    # Shuffling the train sets
                    indices = np.random.permutation(
                        range(self.train_dataset[0].shape[0]))
                    for i, _ in enumerate(self.train_dataset):
                        self.train_dataset[i] = self.train_dataset[i][indices]

                    # batch_ training
                    for batch_step in range(0, train_size, batch_size):

                        batch = [
                            self.train_dataset['images'][batch_step:batch_step
                                                         + batch_size],
                            self.train_dataset['labels_for_tr'][
                                batch_step:batch_step + batch_size].astype(
                                    np.float32),
                        ]

                        # Check batch images for the training
                        if False:
                            fig = plt.figure(figsize=(12, 1), dpi=80)

                            for i in range(12):
                                plt.subplot(1, 12, i + 1)
                                plt.imshow(
                                    batch[0][i, :, :].reshape(64, 64, 3),
                                    interpolation='nearest')
                                plt.tight_layout()

                            plt.show()

                        feed_train = {
                            self.tf_x: batch[0],
                            self.tf_y_: batch[1],
                            self.tf_learning_rate: learning_rate,
                            self.tf_l2_beta: l2_beta,
                            self.tf_keep_prob: keep_prob
                        }

                        feed_accu = {
                            self.tf_x: batch[0],
                            self.tf_y_: batch[1],
                            self.tf_learning_rate: learning_rate,
                            self.tf_l2_beta: l2_beta,
                            self.tf_keep_prob: 1.0
                        }

                        # Do training
                        self.tf_optimizer.run(feed_dict=feed_train)

                    # tensorflow logging for tensorboard
                    _summaries = sess.run(merged, feed_dict=feed_train)
                    train_writer.add_summary(_summaries, epoch)

                    # save model weights and biases
                    self.ckpt_saver.save(sess, self.ckpt_fname)

                    # logging loss and accuracy
                    print(".", end='')
                    if not epoch % 20:
                        _loss, _train_accuracy = sess.run(
                            [self.tf_loss, self.tf_accuracy],
                            feed_dict=feed_accu)

                        print('')
                        print(
                            "epoch {:4d} -> loss : {:05.2f} / training_accuracy: {:05.2f}".
                            format(epoch, _loss, _train_accuracy))

                        if _loss < 5. or _train_accuracy >= 0.70:
                            break

            self.ckpt_saver.restore(sess, self.ckpt_fname)

            feed_test = {
                self.tf_x: self.test_dataset[0],
                self.tf_y_: self.test_dataset[4],
                self.tf_learning_rate: learning_rate,
                self.tf_l2_beta: l2_beta,
                self.tf_keep_prob: 1.0
            }

            print('testing accuracy {:05.2f}'.format(
                self.tf_accuracy.eval(feed_dict=feed_test)))
        return

    def predict(self, test_dataset):
        if not self.is_model_initialized:
            raise AssertionError(
                'you must initilize model using set_model function')

        label = np.zeros(test_dataset.shape[0] * 70).reshape(-1, 70)
        pred = None

        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            self.ckpt_saver.restore(sess, self.ckpt_fname)

            # hyper-parameters
            learning_rate = 3.1e-4
            l2_beta = 16e-4

            feed_test = {
                self.tf_x: test_dataset,
                self.tf_y_: label,
                self.tf_learning_rate: learning_rate,
                self.tf_l2_beta: l2_beta,
                self.tf_keep_prob: 1.0
            }

            pred = sess.run(self.pred_value, feed_dict=feed_test)

        return pred


def train():
    loader = SVHNBboxLoader()
    loader.init_data()

    trainer = SVHNTrainer(
        [None, 64, 64, 1], [None, 25], train_name='svhn_synthetic')

    _log('data loading...', end='\r\n')

    trainer.train_dataset = loader.get_data("training")
    trainer.test_dataset = loader.get_data("testing")

    train_labels = trainer.train_dataset['bboxes_cnt'] + trainer.train_dataset[
        'bboxes_pt']
    test_labels = trainer.test_dataset['bboxes_cnt'] + trainer.test_dataset[
        'bboxes_pt']

    trainer.train_dataset['labels_for_tr'] = train_labels
    trainer.test_dataset['labels_for_tr'] = test_labels

    _log('training...')
    trainer.set_model()
    trainer.train(for_training=True)


def predict_real_image_using_svhn():
    trainer = SVHNTrainer(
        [None, 64, 64, 1], [None, 25], train_name='svhn_synthetic')
    _log('data loading...', end='\r\n')

    _log('testring for real dataset...')
    fname_list = [
        os.path.join('./KR_data', 'IMG_20170315_201204260.jpg'),
        os.path.join('./KR_data', 'IMG_20170315_201212453.jpg'),
        os.path.join('./KR_data',
                     'IMG_20170315_201232407_BURST000_COVER_TOP.jpg'),
        os.path.join('./KR_data', 'IMG_20170315_201232407_BURST001.jpg'),
        os.path.join('./KR_data', 'IMG_20170315_203000566.jpg'),
    ]

    ip = ImageProcess()
    img = np.array(
        [ip.processImage(fname, toGray=True) for fname in fname_list])

    trainer.set_model()
    print(trainer.predict(img))


def main():
    train()
    tf.reset_default_graph()
    predict_real_image_using_svhn()

    gc.collect()


if __name__ == '__main__':
    main()
