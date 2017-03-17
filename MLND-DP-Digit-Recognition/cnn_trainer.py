from __future__ import print_function

import gc
import math
import os

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

from data_loader import MNISTLoader, SVHNLoader
from image_process import ImageProcess

_DEBUG = True


def _log(message, end='\r\n'):
    if _DEBUG:
        print(message, end=end)


class CNNTrainer:

    train_name = 'convolution_neural_networks_train'
    summary_dirname = None
    ckpt_saver = None
    ckpt_fname = None

    def __init__(self):

        return

    def weight_variable(self, shape, name=None, kstddev = None):
        """
        Initialize weight variables

        Parameters
        ----------
        shape : list
            weight variable's shape
        name : str
            tensorflow graph's name
        kstddev: int
            if you want to customize stddev up to image size, pass the size using this parameter
            normally you can use image's W * H * depth or labels' distinct encoding
            from https://arxiv.org/pdf/1502.01852v1.pdf


        Returns
        ------
        tf.Variable
        """

        name = '%s_w' % name if not name else None
        stddev = None if kstddev is None else math.sqrt(2.0 / kstddev)

        return tf.Variable(tf.truncated_normal(shape, stddev=0.1),
                           dtype=tf.float32,
                           name=name)

    def bias_variable(self, shape, name=None):
        name = '%s_b' % name if not name else None

        return tf.Variable(tf.zeros(shape),
                           dtype=tf.float32,
                           name=name)

    def conv2d(self, x, W, strides=[1,1,1,1], padding='SAME'):

        strides = strides
        padding = padding

        return tf.nn.conv2d(x, W,
                            strides=strides,
                            padding=padding)

    def max_pool_2x2(self, x):
        return tf.nn.max_pool(x,
                              ksize=[1, 2, 2, 1],
                              strides=[1, 2, 2, 1],
                              padding='SAME')

    # def get_conv2d(name, data, patch, d_in, d_out, stride, pooling=None):
    #     weights = tf.Variable(tf.truncated_normal([patch, patch, d_in, d_out],
    #                                               stddev=get_conv2d_weights_init_stddev(img_w, img_h, d_in)),
    #                           name=str('%s_w' % name))

    #     biases = tf.Variable(tf.zeros([d_out]),
    #                          name=str('%s_b' % name))

    #     layer = tf.nn.relu(tf.nn.conv2d(data, weights, stride, padding='SAME') + biases)

    #     if pooling is not None:
    #         layer = tf.nn.max_pool(layer, pooling, pooling, padding='SAME')

    #     return weights, biases, layer

    # def get_conv2d_weights_init_stddev(w, h, d_in):
    #     # from https://arxiv.org/pdf/1502.01852v1.pdf
    #     return math.sqrt(2.0 / (w*h*d_in))

    # def get_fc(name, data, depth, relu=True):
    #     inbound = int(data.get_shape()[1])
    #     weights = tf.Variable(tf.truncated_normal([inbound, depth], stddev=math.sqrt(2.0 / inbound), name=str('%s_w' % name)))
    #     biases = tf.Variable(tf.zeros([depth]), name=str('%s_b' % name))
    #     layer = tf.matmul(data, weights) + biases
    #     if relu is True:
    #         layer = tf.nn.relu(layer)
    #     return weights, biases, layer


class MNISTTrainer(CNNTrainer):

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

    tf_debug1 = None
    tf_debug2 = None
    tf_debug3 = None
    tf_debug4 = None

    seed = 42
    pred_value = None

    def __init__(self, image_shape=[None, 32, 32, 3], label_shape=[None, 10], train_name=None):

        # set image, label shape
        self.image_shape = image_shape
        self.label_shape = label_shape
        self.raw_image_shape = self.image_shape if image_shape[3] != 1 else image_shape[0:3]

        _log('input shape must be ', end='')
        _log(self.raw_image_shape)

        # set tf variables for input, labels and hyper-parameters
        self.tf_x = tf.placeholder(tf.float32, self.raw_image_shape)
        self.tf_y_ = tf.placeholder(tf.float32, self.label_shape)

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
        w_conv1 = self.weight_variable([5, 5, 1, 16], name='conv1')
        b_conv1 = self.bias_variable([16], name='conv1')

        w_conv2 = self.weight_variable([5, 5, 16, 32], name='conv2')
        b_conv2 = self.bias_variable([32], name='conv2')

        w_conv3 = self.weight_variable([5, 5, 32, 64], name='conv3')
        b_conv3 = self.bias_variable([64], name='conv3')

        w_conv4 = self.weight_variable([5, 5, 64, 128], name='conv4')
        b_conv4 = self.bias_variable([128], name='conv4')

        w_fc1 = self.weight_variable([4 * 4 * 128, 256], name='fc1')
        b_fc1 = self.bias_variable([256], name='fc1')

        w_fc2 = self.weight_variable([256, 128], name='fc2')
        b_fc2 = self.bias_variable([128], name='fc2')

        # weight & bias matrix depends on features
        w_fc2_len = self.weight_variable([128, 10], name='fc2_len')
        b_fc2_len = self.bias_variable([10], name='fc2_len')

        w_fc2_d1 = self.weight_variable([128, 10], name='fc2_d1')
        b_fc2_d1 = self.bias_variable([10], name='fc2_d1')

        w_fc2_d2 = self.weight_variable([128, 10], name='fc2_d2')
        b_fc2_d2 = self.bias_variable([10], name='fc2_d2')

        w_fc2_d3 = self.weight_variable([128, 10], name='fc2_d3')
        b_fc2_d3 = self.bias_variable([10], name='fc2_d3')

        w_fc2_d4 = self.weight_variable([128, 10], name='fc2_d4')
        b_fc2_d4 = self.bias_variable([10], name='fc2_d4')

        w_fc2_d5 = self.weight_variable([128, 10], name='fc2_d5')
        b_fc2_d5 = self.bias_variable([10], name='fc2_d5')

        w_fc2_d6 = self.weight_variable([128, 10], name='fc2_d6')
        b_fc2_d6 = self.bias_variable([10], name='fc2_d6')

        # set up saver for continuous learning
        # https://www.tensorflow.org/api_docs/python/tf/train/Saver
        param_lst = [w_conv1, w_conv2, w_conv3, w_conv4, w_fc1, w_fc2,]
        param_lst += [b_conv1, b_conv2, b_conv3, b_conv4, b_fc1, b_fc2,]
        param_lst += [w_fc2_len, w_fc2_d1, w_fc2_d2, w_fc2_d3, w_fc2_d4, w_fc2_d5, w_fc2_d6, ]
        param_lst += [b_fc2_len, b_fc2_d1, b_fc2_d2, b_fc2_d3, b_fc2_d4, b_fc2_d5, b_fc2_d6, ]

        self.ckpt_saver = tf.train.Saver(param_lst)

        # convolution layer
        with tf.name_scope('hidden_layer1') as hl_scope1:
            h_conv1 = tf.nn.relu(self.conv2d(x_input, w_conv1) + b_conv1)
            h_pool1 = self.max_pool_2x2(h_conv1)

        with tf.name_scope('hidden_layer2') as hl_scope2:
            h_conv2 = tf.nn.relu(self.conv2d(h_pool1, w_conv2) + b_conv2)
            h_pool2 = self.max_pool_2x2(h_conv2)

        with tf.name_scope('hidden_layer3') as hl_scope3:
            h_conv3 = tf.nn.relu(self.conv2d(h_pool2, w_conv3) + b_conv3)
            h_pool3 = self.max_pool_2x2(h_conv3)

        with tf.name_scope('hidden_layer4') as hl_scope4:
            h_conv4 = tf.nn.relu(self.conv2d(h_pool3, w_conv4) + b_conv4)
            h_pool4 = self.max_pool_2x2(h_conv4)

        # fully connected layer
        with tf.name_scope('fully_connected_layer1') as fc_scope1:
            shape  = h_pool4.get_shape().as_list()
            h_pool4_flat = tf.reshape(h_pool4, [-1, shape[1] * shape[2] * shape[3]])

            h_pool4_flat_dropout = tf.nn.dropout(h_pool4_flat, self.tf_keep_prob, seed=self.seed)
            h_fc1 = tf.nn.relu(tf.matmul(h_pool4_flat_dropout, w_fc1) + b_fc1)

        # dropout
        with tf.name_scope('fully_connected_layer2') as fc_scope2:
            h_fc1_dropout = tf.nn.dropout(h_fc1, self.tf_keep_prob, seed=self.seed)
            h_fc2 = tf.nn.relu(tf.matmul(h_fc1_dropout, w_fc2)+b_fc2)

        # readout layer
        with tf.name_scope('readout_layer') as ro_scope:
            pred_r_len = tf.matmul(h_fc2, w_fc2_len) + b_fc2_len
            pred_len = tf.reshape(pred_r_len, [-1,10])

            pred_r_d1 = tf.matmul(h_fc2, w_fc2_d1) + b_fc2_d1
            pred_d1 = tf.reshape(pred_r_d1, [-1,10])

            pred_r_d2 = tf.matmul(h_fc2, w_fc2_d2) + b_fc2_d2
            pred_d2 = tf.reshape(pred_r_d2, [-1,10])

            pred_r_d3 = tf.matmul(h_fc2, w_fc2_d3) + b_fc2_d3
            pred_d3 = tf.reshape(pred_r_d3, [-1,10])

            pred_r_d4 = tf.matmul(h_fc2, w_fc2_d4) + b_fc2_d4
            pred_d4 = tf.reshape(pred_r_d4, [-1,10])

            pred_r_d5 = tf.matmul(h_fc2, w_fc2_d5) + b_fc2_d5
            pred_d5 = tf.reshape(pred_r_d5, [-1,10])

            pred_r_d6 = tf.matmul(h_fc2, w_fc2_d6) + b_fc2_d6
            pred_d6 = tf.reshape(pred_r_d6, [-1,10])

        # loss calculation
        with tf.name_scope('loss_calculation') as lc_scope:
            softmax_len = tf.nn.softmax_cross_entropy_with_logits(labels=tf.reshape(self.tf_y_, (-1,7,10))[:,0,:],
                                                                  logits=pred_len)
            softmax_d1 = tf.nn.softmax_cross_entropy_with_logits(labels=tf.reshape(self.tf_y_, (-1,7,10))[:,1,:],
                                                                  logits=pred_d1)
            softmax_d2 = tf.nn.softmax_cross_entropy_with_logits(labels=tf.reshape(self.tf_y_, (-1,7,10))[:,2,:],
                                                                  logits=pred_d2)
            softmax_d3 = tf.nn.softmax_cross_entropy_with_logits(labels=tf.reshape(self.tf_y_, (-1,7,10))[:,3,:],
                                                                  logits=pred_d3)
            softmax_d4 = tf.nn.softmax_cross_entropy_with_logits(labels=tf.reshape(self.tf_y_, (-1,7,10))[:,4,:],
                                                                  logits=pred_d4)
            softmax_d5 = tf.nn.softmax_cross_entropy_with_logits(labels=tf.reshape(self.tf_y_, (-1,7,10))[:,5,:],
                                                                  logits=pred_d5)
            softmax_d6 = tf.nn.softmax_cross_entropy_with_logits(labels=tf.reshape(self.tf_y_, (-1,7,10))[:,6,:],
                                                                  logits=pred_d6)

            regularization = tf.nn.l2_loss(w_fc1) + tf.nn.l2_loss(b_fc1)
            self.tf_loss = self.tf_l2_beta * regularization
            self.tf_loss += tf.reduce_mean(softmax_len)
            self.tf_loss += tf.reduce_mean(softmax_d1)
            self.tf_loss += tf.reduce_mean(softmax_d2)
            self.tf_loss += tf.reduce_mean(softmax_d3)
            self.tf_loss += tf.reduce_mean(softmax_d4)
            self.tf_loss += tf.reduce_mean(softmax_d5)
            # self.tf_loss += tf.reduce_mean(softmax_d6)

            tf.summary.scalar('loss', self.tf_loss)

        # loss optimizer
        with tf.name_scope('training') as tr_scope:
            self.tf_optimizer = tf.train.AdamOptimizer(learning_rate=self.tf_learning_rate).minimize(self.tf_loss)

        # accuracy calculation
        with tf.name_scope('accuracy_calculation') as acc_scope:
            pred_combined = tf.stack([pred_len, pred_d1, pred_d2, pred_d3, pred_d4, pred_d5, pred_d6], axis=1)
            predict = tf.reshape(pred_combined, (-1, 70))
            is_correct_pred = tf.equal(
                tf.argmax(predict, 1), tf.argmax(tf.reshape(self.tf_y_, (-1,7,10)), 1))
            self.tf_accuracy = tf.reduce_mean(tf.cast(is_correct_pred, tf.float32))
            tf.summary.scalar('accuracy', self.tf_accuracy)

            self.pred_value = predict


    def train(self, for_training=True):
        if not self.is_model_initialized:
            raise AssertionError('you must initilize model using set_model function')

        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())

            # generate tensorflow summary merged
            merged = tf.summary.merge_all()
            train_writer = tf.summary.FileWriter(self.summary_dirname, sess.graph)

            # Batching data
            batch_size = 50
            train_size = self.train_dataset[0].shape[0]

            # hyper-parameters
            learning_rate = 3.1e-4
            l2_beta = 16e-4
            keep_prob = 0.5

            feed_train = None
            feed_accu = None
            feed_test = None

            if for_training:
                _log('we\'re about to training using %d trainset...' % self.train_dataset[0].shape[0])
                _log('trainset size : {:4d}'.format(train_size))
                _log('batch    size : {:4d}'.format(batch_size))

                _log('. : 1 training epoch')

                for epoch in range(200):

                    # Shuffling the train sets
                    indices = np.random.permutation(range(self.train_dataset[0].shape[0]))
                    for i, _ in enumerate(self.train_dataset):
                        self.train_dataset[i] = self.train_dataset[i][indices]

                    # batch_ training
                    for batch_step in range(0, train_size, batch_size):

                        batch = [
                            self.train_dataset[0][batch_step:batch_step+batch_size],
                            self.train_dataset[4][batch_step:batch_step+batch_size],
                            self.train_dataset[1][batch_step:batch_step+batch_size]]

                        # Check batch images for the training
                        if False:
                            fig = plt.figure(figsize=(12, 1), dpi=80)

                            for i in range(12):
                                plt.subplot(1, 12, i+1)
                                plt.title(batch[2][i])
                                plt.imshow(batch[0][i,:,:].reshape(64, 64),
                                           interpolation='nearest',
                                           cmap='Grey')
                                plt.tight_layout()

                            plt.show()

                        feed_train ={self.tf_x: batch[0],
                                     self.tf_y_: batch[1],
                                     self.tf_learning_rate: learning_rate,
                                     self.tf_l2_beta: l2_beta,
                                     self.tf_keep_prob: keep_prob}

                        feed_accu ={self.tf_x: batch[0],
                                     self.tf_y_: batch[1],
                                     self.tf_learning_rate: learning_rate,
                                     self.tf_l2_beta: l2_beta,
                                     self.tf_keep_prob: 1.0}

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
                        _loss, _train_accuracy = sess.run([self.tf_loss, self.tf_accuracy],
                                                          feed_dict=feed_accu)

                        print('')
                        print("epoch {:4d} -> loss : {:05.2f} / training_accuracy: {:05.2f}".format(
                            epoch, _loss, _train_accuracy))

            self.ckpt_saver.restore(sess, self.ckpt_fname)

            feed_test = {self.tf_x: self.test_dataset[0],
                         self.tf_y_: self.test_dataset[4],
                         self.tf_learning_rate: learning_rate,
                         self.tf_l2_beta: l2_beta,
                         self.tf_keep_prob: 1.0}

            print('testing accuracy {:05.2f}'.format(self.tf_accuracy.eval(feed_dict=feed_test)))
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

    tf_debug1 = None
    tf_debug2 = None
    tf_debug3 = None
    tf_debug4 = None

    seed = 42
    pred_value = None


    def __init__(self, image_shape=[None, 32, 32, 3], label_shape=[None, 10], train_name=None):

        # set image, label shape
        self.image_shape = image_shape
        self.label_shape = label_shape
        self.raw_image_shape = self.image_shape if image_shape[3] != 1 else image_shape[0:3]

        _log('input shape must be ', end='')
        _log(self.raw_image_shape)

        # set tf variables for input, labels and hyper-parameters
        self.tf_x = tf.placeholder(tf.float32, self.raw_image_shape)
        self.tf_y_ = tf.placeholder(tf.float32, self.label_shape)

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
        w_conv1 = self.weight_variable([5, 5, 3, 16], name='conv1')
        b_conv1 = self.bias_variable([16], name='conv1')

        w_conv2 = self.weight_variable([5, 5, 16, 32], name='conv2')
        b_conv2 = self.bias_variable([32], name='conv2')

        w_conv3 = self.weight_variable([5, 5, 32, 64], name='conv3')
        b_conv3 = self.bias_variable([64], name='conv3')

        w_conv4 = self.weight_variable([5, 5, 64, 128], name='conv4')
        b_conv4 = self.bias_variable([128], name='conv4')

        w_fc1 = self.weight_variable([4 * 4 * 128, 256], name='fc1')
        b_fc1 = self.bias_variable([256], name='fc1')

        w_fc2 = self.weight_variable([256, 128], name='fc2')
        b_fc2 = self.bias_variable([128], name='fc2')

        # weight & bias matrix depends on features
        w_fc2_len = self.weight_variable([128, 10], name='fc2_len')
        b_fc2_len = self.bias_variable([10], name='fc2_len')

        w_fc2_d1 = self.weight_variable([128, 10], name='fc2_d1')
        b_fc2_d1 = self.bias_variable([10], name='fc2_d1')

        w_fc2_d2 = self.weight_variable([128, 10], name='fc2_d2')
        b_fc2_d2 = self.bias_variable([10], name='fc2_d2')

        w_fc2_d3 = self.weight_variable([128, 10], name='fc2_d3')
        b_fc2_d3 = self.bias_variable([10], name='fc2_d3')

        w_fc2_d4 = self.weight_variable([128, 10], name='fc2_d4')
        b_fc2_d4 = self.bias_variable([10], name='fc2_d4')

        w_fc2_d5 = self.weight_variable([128, 10], name='fc2_d5')
        b_fc2_d5 = self.bias_variable([10], name='fc2_d5')

        w_fc2_d6 = self.weight_variable([128, 10], name='fc2_d6')
        b_fc2_d6 = self.bias_variable([10], name='fc2_d6')

        # set up saver for continuous learning
        # https://www.tensorflow.org/api_docs/python/tf/train/Saver
        param_lst = [w_conv1, w_conv2, w_conv3, w_conv4, w_fc1, w_fc2,]
        param_lst += [b_conv1, b_conv2, b_conv3, b_conv4, b_fc1, b_fc2,]
        param_lst += [w_fc2_len, w_fc2_d1, w_fc2_d2, w_fc2_d3, w_fc2_d4, w_fc2_d5, w_fc2_d6, ]
        param_lst += [b_fc2_len, b_fc2_d1, b_fc2_d2, b_fc2_d3, b_fc2_d4, b_fc2_d5, b_fc2_d6, ]

        self.ckpt_saver = tf.train.Saver(param_lst)

        # convolution layer
        with tf.name_scope('hidden_layer1') as hl_scope1:
            h_conv1 = tf.nn.relu(self.conv2d(x_input, w_conv1) + b_conv1)
            h_pool1 = self.max_pool_2x2(h_conv1)

        with tf.name_scope('hidden_layer2') as hl_scope2:
            h_conv2 = tf.nn.relu(self.conv2d(h_pool1, w_conv2) + b_conv2)
            h_pool2 = self.max_pool_2x2(h_conv2)

        with tf.name_scope('hidden_layer3') as hl_scope3:
            h_conv3 = tf.nn.relu(self.conv2d(h_pool2, w_conv3) + b_conv3)
            h_pool3 = self.max_pool_2x2(h_conv3)

        with tf.name_scope('hidden_layer4') as hl_scope4:
            h_conv4 = tf.nn.relu(self.conv2d(h_pool3, w_conv4) + b_conv4)
            h_pool4 = self.max_pool_2x2(h_conv4)

        # fully connected layer
        with tf.name_scope('fully_connected_layer1') as fc_scope1:
            shape  = h_pool4.get_shape().as_list()
            h_pool4_flat = tf.reshape(h_pool4, [-1, shape[1] * shape[2] * shape[3]])

            h_pool4_flat_dropout = tf.nn.dropout(h_pool4_flat, self.tf_keep_prob, seed=self.seed)
            h_fc1 = tf.nn.relu(tf.matmul(h_pool4_flat_dropout, w_fc1) + b_fc1)

        # dropout
        with tf.name_scope('fully_connected_layer2') as fc_scope2:
            h_fc1_dropout = tf.nn.dropout(h_fc1, self.tf_keep_prob, seed=self.seed)
            h_fc2 = tf.nn.relu(tf.matmul(h_fc1_dropout, w_fc2)+b_fc2)

        # readout layer
        with tf.name_scope('readout_layer') as ro_scope:
            pred_r_len = tf.matmul(h_fc2, w_fc2_len) + b_fc2_len
            pred_len = tf.reshape(pred_r_len, [-1,10])

            pred_r_d1 = tf.matmul(h_fc2, w_fc2_d1) + b_fc2_d1
            pred_d1 = tf.reshape(pred_r_d1, [-1,10])

            pred_r_d2 = tf.matmul(h_fc2, w_fc2_d2) + b_fc2_d2
            pred_d2 = tf.reshape(pred_r_d2, [-1,10])

            pred_r_d3 = tf.matmul(h_fc2, w_fc2_d3) + b_fc2_d3
            pred_d3 = tf.reshape(pred_r_d3, [-1,10])

            pred_r_d4 = tf.matmul(h_fc2, w_fc2_d4) + b_fc2_d4
            pred_d4 = tf.reshape(pred_r_d4, [-1,10])

            pred_r_d5 = tf.matmul(h_fc2, w_fc2_d5) + b_fc2_d5
            pred_d5 = tf.reshape(pred_r_d5, [-1,10])

            pred_r_d6 = tf.matmul(h_fc2, w_fc2_d6) + b_fc2_d6
            pred_d6 = tf.reshape(pred_r_d6, [-1,10])

        # loss calculation
        with tf.name_scope('loss_calculation') as lc_scope:
            softmax_len = tf.nn.softmax_cross_entropy_with_logits(labels=tf.reshape(self.tf_y_, (-1,7,10))[:,0,:],
                                                                  logits=pred_len)
            softmax_d1 = tf.nn.softmax_cross_entropy_with_logits(labels=tf.reshape(self.tf_y_, (-1,7,10))[:,1,:],
                                                                  logits=pred_d1)
            softmax_d2 = tf.nn.softmax_cross_entropy_with_logits(labels=tf.reshape(self.tf_y_, (-1,7,10))[:,2,:],
                                                                  logits=pred_d2)
            softmax_d3 = tf.nn.softmax_cross_entropy_with_logits(labels=tf.reshape(self.tf_y_, (-1,7,10))[:,3,:],
                                                                  logits=pred_d3)
            softmax_d4 = tf.nn.softmax_cross_entropy_with_logits(labels=tf.reshape(self.tf_y_, (-1,7,10))[:,4,:],
                                                                  logits=pred_d4)
            softmax_d5 = tf.nn.softmax_cross_entropy_with_logits(labels=tf.reshape(self.tf_y_, (-1,7,10))[:,5,:],
                                                                  logits=pred_d5)
            softmax_d6 = tf.nn.softmax_cross_entropy_with_logits(labels=tf.reshape(self.tf_y_, (-1,7,10))[:,6,:],
                                                                  logits=pred_d6)

            regularization = tf.nn.l2_loss(w_fc1) + tf.nn.l2_loss(b_fc1)
            self.tf_loss = self.tf_l2_beta * regularization
            self.tf_loss += tf.reduce_mean(softmax_len)
            self.tf_loss += tf.reduce_mean(softmax_d1)
            self.tf_loss += tf.reduce_mean(softmax_d2)
            self.tf_loss += tf.reduce_mean(softmax_d3)
            self.tf_loss += tf.reduce_mean(softmax_d4)
            self.tf_loss += tf.reduce_mean(softmax_d5)
            # self.tf_loss += tf.reduce_mean(softmax_d6)

            tf.summary.scalar('loss', self.tf_loss)

        # loss optimizer
        with tf.name_scope('training') as tr_scope:
            self.tf_optimizer = tf.train.AdamOptimizer(learning_rate=self.tf_learning_rate).minimize(self.tf_loss)

        # accuracy calculation
        with tf.name_scope('accuracy_calculation') as acc_scope:
            pred_combined = tf.stack([pred_len, pred_d1, pred_d2, pred_d3, pred_d4, pred_d5, pred_d6], axis=1)
            predict = tf.reshape(pred_combined, (-1, 7, 10))
            is_correct_pred = tf.equal(
                tf.argmax(predict, 2), tf.argmax(tf.reshape(self.tf_y_, (-1,7,10)), 2))
            self.tf_accuracy = tf.reduce_mean(tf.cast(is_correct_pred, tf.float32))
            tf.summary.scalar('accuracy', self.tf_accuracy)

            self.pred_value = tf.argmax(predict, 2)


    def train(self, for_training=True):
        if not self.is_model_initialized:
            raise AssertionError('you must initilize model using set_model function')

        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())

            # Batching data
            batch_size = 50
            train_size = self.train_dataset[0].shape[0]

            # hyper-parameters
            learning_rate = 3.1e-4
            l2_beta = 16e-4
            keep_prob = 0.5

            feed_train = None
            feed_accu = None
            feed_test = None

            if for_training:
                # generate tensorflow summary merged
                merged = tf.summary.merge_all()
                train_writer = tf.summary.FileWriter(self.summary_dirname, sess.graph)

                _log('we\'re about to training using %d trainset...' % self.train_dataset[0].shape[0])
                _log('trainset size : {:4d}'.format(train_size))
                _log('batch    size : {:4d}'.format(batch_size))

                _log('. : 1 training epoch')

                for epoch in range(450):

                    # Shuffling the train sets
                    indices = np.random.permutation(range(self.train_dataset[0].shape[0]))
                    for i, _ in enumerate(self.train_dataset):
                        self.train_dataset[i] = self.train_dataset[i][indices]

                    # batch_ training
                    for batch_step in range(0, train_size, batch_size):

                        batch = [
                            self.train_dataset[0][batch_step:batch_step+batch_size],
                            self.train_dataset[4][batch_step:batch_step+batch_size],
                            self.train_dataset[1][batch_step:batch_step+batch_size]]

                        # Check batch images for the training
                        if False:
                            fig = plt.figure(figsize=(12, 1), dpi=80)

                            for i in range(12):
                                plt.subplot(1, 12, i+1)
                                plt.title(batch[2][i])
                                plt.imshow(batch[0][i,:,:].reshape(64, 64, 3),
                                           interpolation='nearest')
                                plt.tight_layout()

                            plt.show()

                        feed_train ={self.tf_x: batch[0],
                                     self.tf_y_: batch[1],
                                     self.tf_learning_rate: learning_rate,
                                     self.tf_l2_beta: l2_beta,
                                     self.tf_keep_prob: keep_prob}

                        feed_accu ={self.tf_x: batch[0],
                                     self.tf_y_: batch[1],
                                     self.tf_learning_rate: learning_rate,
                                     self.tf_l2_beta: l2_beta,
                                     self.tf_keep_prob: 1.0}

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
                        _loss, _train_accuracy = sess.run([self.tf_loss, self.tf_accuracy],
                                                          feed_dict=feed_accu)

                        print('')
                        print("epoch {:4d} -> loss : {:05.2f} / training_accuracy: {:05.2f}".format(
                            epoch, _loss, _train_accuracy))

            self.ckpt_saver.restore(sess, self.ckpt_fname)

            feed_test = {self.tf_x: self.test_dataset[0],
                         self.tf_y_: self.test_dataset[4],
                         self.tf_learning_rate: learning_rate,
                         self.tf_l2_beta: l2_beta,
                         self.tf_keep_prob: 1.0}

            print('testing accuracy {:05.2f}'.format(self.tf_accuracy.eval(feed_dict=feed_test)))
        return


    def predict(self, test_dataset):
        if not self.is_model_initialized:
            raise AssertionError('you must initilize model using set_model function')

        label = np.zeros(test_dataset.shape[0] * 70).reshape(-1, 70)
        pred = None

        with tf.Session() as sess:
            self.ckpt_saver.restore(sess, self.ckpt_fname)

            # hyper-parameters
            learning_rate = 3.1e-4
            l2_beta = 16e-4

            feed_test = {self.tf_x: test_dataset,
                         self.tf_y_: label,
                         self.tf_learning_rate: learning_rate,
                         self.tf_l2_beta: l2_beta,
                         self.tf_keep_prob: 1.0}

            pred = sess.run(self.pred_value,
                            feed_dict=feed_test)

        return pred


def train_for_mnist_normal():
    loader = MNISTLoader('mnist')
    loader.init_data()

    trainer = MNISTTrainer([None, 28, 28, 1], [None, 10], train_name='mnist')

    _log('data loading...', end='\r\n')

    trainer.train_dataset = list(loader.get_data("training"))
    trainer.test_dataset = list(loader.get_data("testing"))

    # normal label to one hot encoding
    trainer.train_dataset.append(np.array(loader.label_to_onehot(trainer.train_dataset[1])))
    trainer.test_dataset.append(np.array(loader.label_to_onehot(trainer.test_dataset[1])))

    _log('data validation...', end='\r\n')

    # To check image input
    _log('input image data shape : ', end='')
    _log(trainer.train_dataset[0].shape)

    # To check label input
    _log('input label data shape : ', end='')
    _log(trainer.train_dataset[1].shape)

    # if _DEBUG:
    # fig = plt.figure()
    # fig.add_subplot(1, 1, 1)
    # plt.imshow(trainer.train_dataset[0][0,:,:],
    #                 interpolation='nearest',
    #                 cmap='Greys')
    # plt.show()

    _log('training...')
    trainer.set_model()
    trainer.train()


def train_for_mnist_synthetic():
    loader = MNISTLoader()
    loader.init_data()

    trainer = MNISTTrainer([None, 64, 64, 1], [None, 70], train_name='mnist_synthetic')

    _log('data loading...', end='\r\n')

    trainer.train_dataset = list(loader.get_mixed_data("training"))
    trainer.test_dataset = list(loader.get_mixed_data("testing"))

    train_L = np.c_[trainer.train_dataset[3]+1, trainer.train_dataset[2]]
    train_L_1hot = np.array([[loader.label_to_onehot(digit)] for digit in train_L.T])
    train_L_1hot = np.transpose(train_L_1hot, (1,2,0,3))
    train_L_1hot = train_L_1hot.reshape((-1, 7 * 10))

    test_L = np.c_[trainer.test_dataset[3]+1, trainer.test_dataset[2]]
    test_L_1hot = np.array([[loader.label_to_onehot(digit)] for digit in test_L.T])
    test_L_1hot = np.transpose(test_L_1hot, (1,2,0,3))
    test_L_1hot = test_L_1hot.reshape((-1, 7 * 10))

    trainer.train_dataset.append(train_L_1hot)
    trainer.test_dataset.append(test_L_1hot)

    _log('data validation...', end='\r\n')

    # To check image input
    _log('input image data shape : ', end='')
    _log(trainer.train_dataset[0].shape)

    # To check label input
    _log('input label data shape : ', end='')
    _log(trainer.train_dataset[1].shape)

    _log('training...')
    trainer.set_model()
    trainer.train(for_training=False)


def train_for_svhn_synthetic():
    loader = SVHNLoader()
    loader.init_data()

    trainer = SVHNTrainer([None, 64, 64, 3], [None, 70], train_name='svhn_synthetic')

    _log('data loading...', end='\r\n')

    trainer.train_dataset = list(loader.get_mixed_data("training"))
    trainer.test_dataset = list(loader.get_mixed_data("testing"))

    train_L = np.c_[trainer.train_dataset[3]+1, trainer.train_dataset[2]]
    train_L_1hot = np.array([[loader.label_to_onehot(digit)] for digit in train_L.T])
    train_L_1hot = np.transpose(train_L_1hot, (1,2,0,3))
    train_L_1hot = train_L_1hot.reshape((-1, 7 * 10))

    test_L = np.c_[trainer.test_dataset[3]+1, trainer.test_dataset[2]]
    test_L_1hot = np.array([[loader.label_to_onehot(digit)] for digit in test_L.T])
    test_L_1hot = np.transpose(test_L_1hot, (1,2,0,3))
    test_L_1hot = test_L_1hot.reshape((-1, 7 * 10))

    trainer.train_dataset.append(train_L_1hot)
    trainer.test_dataset.append(test_L_1hot)

    _log('data validation...', end='\r\n')

    # To check image input
    _log('input image data shape : ', end='')
    _log(trainer.train_dataset[0].shape)

    # To check label input
    _log('input label data shape : ', end='')
    _log(trainer.train_dataset[1].shape)

    _log('training...')
    trainer.set_model()
    trainer.train(for_training=False)

    _log('testring for real dataset...')
    fname_list = [
        os.path.join('./KR_data', 'IMG_20170315_201204260.jpg'),
        os.path.join('./KR_data', 'IMG_20170315_201212453.jpg'),
        os.path.join('./KR_data', 'IMG_20170315_201232407_BURST000_COVER_TOP.jpg'),
        os.path.join('./KR_data', 'IMG_20170315_201232407_BURST001.jpg'),
        os.path.join('./KR_data', 'IMG_20170315_203000566.jpg'),
    ]

    ip = ImageProcess()
    img = np.array([ip.processImage(fname) for fname in fname_list])
    print(trainer.predict(img))


def main():
    # train_for_mnist_normal()
    # train_for_mnist_synthetic()
    train_for_svhn_synthetic()

    gc.collect()

if __name__ == '__main__':
    main()
