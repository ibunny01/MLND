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


def weights_init_stddev(w, h, d_in):
    # https://arxiv.org/pdf/1502.01852v1.pdf
    return math.sqrt(2.0 / (w * h * d_in))


def get_conv2d(name,
               data,
               patch,
               d_in,
               d_out,
               stride,
               pooling=None,
               image_shape=(None, 64, 64, 1)):

    stddev = weights_init_stddev(image_shape[1], image_shape[2], d_in)

    with tf.name_scope(str('%s_namescope' % name)) as hl_scope:
        weights = tf.Variable(
            tf.truncated_normal([patch, patch, d_in, d_out], stddev=stddev),
            dtype=tf.float32,
            name=str('%s_w' % name))

        biases = tf.Variable(
            tf.zeros([d_out]), dtype=tf.float32, name=str('%s_b' % name))

        layer = tf.nn.relu(
            tf.nn.conv2d(data, weights, stride, padding='SAME') + biases)

        if pooling is not None:
            layer = tf.nn.max_pool(layer, pooling, pooling, padding='SAME')

    return weights, biases, layer, hl_scope


def get_fc(name, data, depth, relu=True, dropout=True, keep_prob=1.0, seed=42):
    with tf.name_scope(str('%s_namescope' % name)) as hl_scope:
        inbound = int(data.get_shape()[1])
        weights = tf.Variable(
            tf.truncated_normal(
                [inbound, depth],
                stddev=math.sqrt(2.0 / inbound),
                dtype=tf.float32,
                name=str('%s_w' % name)))

        biases = tf.Variable(
            tf.zeros([depth]), dtype=tf.float32, name=str('%s_b' % name))

        layer = tf.matmul(data, weights) + biases

        if relu is True:
            layer = tf.nn.relu(layer)

        if dropout is True:
            layer = tf.nn.dropout(layer, keep_prob, seed=seed)

    return weights, biases, layer, hl_scope


class CNNTrainer:

    train_name = 'convolution_neural_networks_train'
    summary_dirname = None
    ckpt_saver = None
    ckpt_fname = None

    seed = 42

    _TF_DEBUG = None

    def __init__(self):

        return


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
        self.tf_y_ = tf.placeholder(tf.int64, self.label_shape)

        self.tf_learning_rate = tf.placeholder(tf.float32)
        self.tf_l2_beta = tf.placeholder(tf.float32)

        self.tf_keep_prob = tf.placeholder(tf.float32)

        # set this trainer name
        self.train_name = train_name if train_name else self.train_name
        self.ckpt_fname = './ckpt/%s.ckpt' % self.train_name
        self.summary_dirname = './summary/%s/' % self.train_name

        return

    def set_model(self):
        self.is_model_initialized = True

        x_input = tf.reshape(self.tf_x, [-1] + self.image_shape[1:4])

        # convolution vector definition

        w_conv1, b_conv1, l_conv1, ns_conv1 = get_conv2d(
            'conv1',
            data=x_input,
            patch=5,
            d_in=1,
            d_out=16,
            stride=[1, 1, 1, 1],
            pooling=[1, 2, 2, 1],
            image_shape=self.image_shape, )

        w_conv2, b_conv2, l_conv2, ns_conv2 = get_conv2d(
            'conv2',
            data=l_conv1,
            patch=5,
            d_in=16,
            d_out=32,
            stride=[1, 1, 1, 1],
            pooling=[1, 2, 2, 1],
            image_shape=self.image_shape, )

        w_conv3, b_conv3, l_conv3, ns_conv3 = get_conv2d(
            'conv3',
            data=l_conv2,
            patch=5,
            d_in=32,
            d_out=64,
            stride=[1, 1, 1, 1],
            pooling=[1, 2, 2, 1],
            image_shape=self.image_shape, )

        w_conv4, b_conv4, l_conv4, ns_conv4 = get_conv2d(
            'conv1',
            data=l_conv3,
            patch=5,
            d_in=64,
            d_out=128,
            stride=[1, 1, 1, 1],
            pooling=[1, 2, 2, 1],
            image_shape=self.image_shape, )

        shape = l_conv4.get_shape().as_list()
        l_reshape = tf.reshape(l_conv4, [-1, shape[1] * shape[2] * shape[3]])

        # weight & bias matrix depends on features
        w_fc1, b_fc1, fc1, ns_fc1 = get_fc(
            'fc1',
            l_reshape,
            256,
            relu=True,
            dropout=True,
            keep_prob=self.tf_keep_prob)

        w_fc2, b_fc2, fc2, ns_fc2 = get_fc(
            'fc2',
            fc1,
            128,
            relu=True,
            dropout=True,
            keep_prob=self.tf_keep_prob)

        # bound boxes position
        num_bboxes = 6
        num_coord = 4
        num_label = num_bboxes * num_coord
        max_coord_val = self.image_shape[1]

        # count of bound box
        w_len, b_len, pred_len, ns_len = get_fc(
            'fc3_bboxes_len', fc2, max_coord_val, relu=False, dropout=False)

        bboxes_param = [
            get_fc(
                str('fc3_bboxes_pos_%d_%d' % (i / 4, i % 4)),
                fc2,
                max_coord_val,
                relu=False) for i in range(num_label)
        ]

        bboxes_weights = [bboxes_param[i][0] for i in range(num_label)]
        bboxes_biases = [bboxes_param[i][1] for i in range(num_label)]
        bboxes_pred = tf.stack(
            [bboxes_param[i][2] for i in range(num_label)], axis=1)

        # loss calculation
        with tf.name_scope('loss_calculation') as lc_scope:
            len_labels = self.tf_y_[:, 0, :]
            len_logits = pred_len

            softmax_len = tf.nn.softmax_cross_entropy_with_logits(
                labels=len_labels, logits=len_logits)
            loss_len = tf.reduce_mean(softmax_len)

            regularization = tf.nn.l2_loss(w_fc1) + tf.nn.l2_loss(b_fc1)
            l2_regularizer = self.tf_l2_beta * regularization

            bboxes_loss = 0.0

            bbox_labels = self.tf_y_[:, 1:, :]
            bbox_logits = bboxes_pred

            bbox_loss = tf.nn.softmax_cross_entropy_with_logits(
                        labels=bbox_labels, logits=bbox_logits)
            reduced_mean_bbox_loss = tf.reduce_mean(bbox_loss, 0)

            bboxes_loss = tf.reduce_sum(reduced_mean_bbox_loss)
            self.tf_loss = loss_len + l2_regularizer + bboxes_loss
            tf.summary.scalar('loss', self.tf_loss)

            self._TF_DEBUG = bbox_loss

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

            pred_len = tf.argmax(tf.nn.softmax(pred_len), 1)
            pred_coord = tf.argmax(
                tf.nn.softmax(
                    tf.reshape(bboxes_pred, (-1, num_label, max_coord_val))),
                2)

            merged_labels = tf.concat(
                [tf.reshape(pred_len, (-1, 1)), pred_coord], 1)

            labels = tf.argmax(self.tf_y_, 2)

            import pdb; pdb.set_trace()

            is_correct = tf.equal(merged_labels, labels)

            self.tf_accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
            tf.summary.scalar('accuracy', self.tf_accuracy)

            self.pred_value = merged_labels

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
            train_tot_sz = self.train_dataset[0].shape[0]

            train_size = 0
            valid_size = 0

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
                     train_tot_sz)
                _log('trainset size : {:4d}'.format(train_tot_sz))
                _log('batch    size : {:4d}'.format(batch_size))

                _log('. : 1 training epoch')

                for epoch in range(1000):

                    # Shuffling the train sets
                    indices = np.random.permutation(range(train_tot_sz))
                    for i in range(len(self.train_dataset)):
                        self.train_dataset[i] = self.train_dataset[i][indices]

                    # split train and valid set
                    train_data, train_label, valid_data, valid_label = SVHNBboxLoader.split_validation(self.train_dataset[0], self.train_dataset[2])

                    train_size = train_data.shape[0]
                    valid_size = valid_data.shape[0]

                    # batch_ training
                    for batch_step in range(0, train_size, batch_size):

                        batch = [
                            train_data[batch_step:batch_step + batch_size],
                            train_label[batch_step:batch_step + batch_size],
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
                            self.tf_x: valid_data,
                            self.tf_y_: valid_label,
                            self.tf_learning_rate: learning_rate,
                            self.tf_l2_beta: l2_beta,
                            self.tf_keep_prob: 1.0
                        }

                        # Do training
                        self.tf_optimizer.run(feed_dict=feed_train)
                        # print(self._TF_DEBUG.eval(feed_dict=feed_accu))

                    # tensorflow logging for tensorboard
                    _summaries = sess.run(merged, feed_dict=feed_train)
                    train_writer.add_summary(_summaries, epoch)

                    # save model weights and biases
                    self.ckpt_saver.save(sess, self.ckpt_fname)

                    # logging loss and accuracy
                    print(".", end='')
                    if not epoch % 1:
                        _loss, _train_accuracy = sess.run(
                            [self.tf_loss, self.tf_accuracy],
                            feed_dict=feed_accu)

                        print('')
                        print(
                            "epoch {:5d} -> loss : {:9.2f} / training_accuracy: {:9.2f}".
                            format(epoch, _loss, _train_accuracy))
                        print(_loss)

                        if _loss < 3. or _train_accuracy >= 0.850:
                            break

            self.ckpt_saver.restore(sess, self.ckpt_fname)

            feed_test = {
                self.tf_x: self.test_dataset[0][:5000],
                self.tf_y_: self.test_dataset[2][:5000],
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

        label = np.zeros(test_dataset.shape[0] * 25*64).reshape(-1, 25, 64)
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
        [None, 64, 64, 1], [None, 25, 64], train_name='svhn_synthetic')

    _log('data loading...', end='\r\n')

    train_dataset = loader.get_data("training")
    test_dataset = loader.get_data("testing")

    train_labels = np.c_[np.array(train_dataset['bboxes_cnt']).reshape((
        -1, 1)), np.array(train_dataset['bboxes_pt'])]

    train_labels_1hot = np.array(
        [[loader.label_to_onehot(digit)] for digit in train_labels.T])
    train_labels_1hot = np.transpose(train_labels_1hot, (1, 2, 0, 3))
    train_labels_1hot = train_labels_1hot.reshape((-1, 25, 64))

    train_digit_labels = np.c_[np.array(train_dataset['bboxes_cnt']).reshape((-1,1)),
                               np.array(train_dataset['labels'])]

    import pdb; pdb.set_trace()
    train_digit_labels_1hot = np.array(
        [[loader.label_to_onehot(digit, 11)] for digit in train_digit_labels.T])
    train_digit_labels_1hot = np.transpose(train_digit_labels_1hot, (1, 2, 0, 3))
    train_digit_labels_1hot = train_digit_labels_1hot.reshape((-1, 7, 11))


    test_labels = np.c_[np.array(test_dataset['bboxes_cnt']).reshape((-1, 1)),
                        np.array(test_dataset['bboxes_pt'])]

    test_labels_1hot = np.array(
        [[loader.label_to_onehot(digit)] for digit in test_labels.T])
    test_labels_1hot = np.transpose(test_labels_1hot, (1, 2, 0, 3))
    test_labels_1hot = test_labels_1hot.reshape((-1, 25, 64))

    test_digit_labels = np.c_[np.array(test_dataset['bboxes_cnt']).reshape((-1,1)),
                               np.array(test_dataset['labels'])]

    test_digit_labels_1hot = np.array(
        [[loader.label_to_onehot(digit, 11)] for digit in test_digit_labels.T])
    test_digit_labels_1hot = np.transpose(test_digit_labels_1hot, (1, 2, 0, 3))
    test_digit_labels_1hot = test_digit_labels_1hot.reshape((-1, 7, 11))


    trainer.train_dataset = list()
    trainer.train_dataset.append(np.array(train_dataset['images']))
    trainer.train_dataset.append(np.array(train_labels))
    trainer.train_dataset.append(np.array(train_labels_1hot))
    trainer.train_dataset.append(np.array(train_digit_labels))
    trainer.train_dataset.append(np.array(train_digit_labels_1hot))

    trainer.test_dataset = list()
    trainer.test_dataset.append(np.array(test_dataset['images']))
    trainer.test_dataset.append(np.array(test_labels))
    trainer.test_dataset.append(np.array(test_labels_1hot))
    trainer.test_dataset.append(np.array(test_digit_labels))
    trainer.test_dataset.append(np.array(test_digit_labels_1hot))

    _log('training...')
    trainer.set_model()
    trainer.train(for_training=False)


def predict_real_image_using_svhn():
    trainer = SVHNTrainer(
        [None, 64, 64, 1], [None, 25, 64], train_name='svhn_synthetic')
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
