from __future__ import print_function

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

import tensorflow as tf
from data_loader import MNISTLoader, SVHNLoader

_DEBUG = True

def _log(message, end='\r\n'):
    if _DEBUG:
        print(message, end=end)

class Trainer:

    def __init__(self):

        return

    def weight_variable(self, shape):
        return tf.Variable(tf.truncated_normal(shape, stddev=0.1), dtype=tf.float32)

    def bias_variable(self, shape):
        return tf.Variable(tf.zeros(shape), dtype=tf.float32)

    def conv2d(self, x, W):
        return tf.nn.conv2d(x, W,
                            strides=[1, 1, 1, 1], padding='SAME')

    def max_pool_2x2(self, x):
        return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                              strides=[1, 2, 2, 1], padding='SAME')

    def get_conv2d(name, data, patch, d_in, d_out, stride, pooling=None):
        weights = tf.Variable(tf.truncated_normal([patch, patch, d_in, d_out], stddev=get_conv2d_weights_init_stddev(img_w,img_h,d_in)), name=str('%s_w' % name))
        biases = tf.Variable(tf.zeros([d_out]), name=str('%s_b' % name))
        layer = tf.nn.relu(tf.nn.conv2d(data, weights, stride, padding='SAME') + biases)
        if pooling is not None:
            layer = tf.nn.max_pool(layer, pooling, pooling, padding='SAME')
        return weights, biases, layer

    def get_fc(name, data, depth, relu=True):
        inbound = int(data.get_shape()[1])
        weights = tf.Variable(tf.truncated_normal([inbound, depth], stddev=math.sqrt(2.0 / inbound), name=str('%s_w' % name)))
        biases = tf.Variable(tf.zeros([depth]), name=str('%s_b' % name))
        layer = tf.matmul(data, weights) + biases
        if relu is True:
            layer = tf.nn.relu(layer)
        return weights, biases, layer

class CNNTrainer(Trainer):
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

    def __init__(self, image_shape=[None, 32, 32, 3], label_shape=[None, 10]):

        self.image_shape = image_shape
        self.label_shape = label_shape
        self.raw_image_shape = self.image_shape if image_shape[3] != 1 else image_shape[0:3]

        _log('input shape must be ', end='')
        _log(self.raw_image_shape)

        self.tf_x = tf.placeholder(tf.float32, self.raw_image_shape)
        self.tf_y_ = tf.placeholder(tf.float32, self.label_shape)

        self.tf_learning_rate = tf.placeholder(tf.float32)
        self.tf_l2_beta = tf.placeholder(tf.float32)

        self.tf_keep_prob = tf.placeholder(tf.float32)

        return

    def set_model(self):
        self.is_model_initialized = True

        x_input = tf.reshape(self.tf_x, [-1] + self.image_shape[1:4])

        # convolution vector definition
        w_conv1 = self.weight_variable([5, 5, 1, 16])
        b_conv1 = self.bias_variable([16])

        w_conv2 = self.weight_variable([5, 5, 16, 32])
        b_conv2 = self.bias_variable([32])

        w_conv3 = self.weight_variable([5, 5, 32, 64])
        b_conv3 = self.bias_variable([64])

        w_conv4 = self.weight_variable([5, 5, 64, 128])
        b_conv4 = self.bias_variable([128])

        w_fc1 = self.weight_variable([4 * 4 * 128, 256])
        b_fc1 = self.bias_variable([256])

        w_fc2 = self.weight_variable([256, 128])
        b_fc2 = self.bias_variable([128])

        # weight & bias matrix depends on features
        w_fc2_len = self.weight_variable([128, 10])
        b_fc2_len = self.bias_variable([10])

        w_fc2_d1 = self.weight_variable([128, 10])
        b_fc2_d1 = self.bias_variable([10])

        w_fc2_d2 = self.weight_variable([128, 10])
        b_fc2_d2 = self.bias_variable([10])

        w_fc2_d3 = self.weight_variable([128, 10])
        b_fc2_d3 = self.bias_variable([10])

        w_fc2_d4 = self.weight_variable([128, 10])
        b_fc2_d4 = self.bias_variable([10])

        w_fc2_d5 = self.weight_variable([128, 10])
        b_fc2_d5 = self.bias_variable([10])

        w_fc2_d6 = self.weight_variable([128, 10])
        b_fc2_d6 = self.bias_variable([10])

        # convolution layer
        h_conv1 = tf.nn.relu(self.conv2d(x_input, w_conv1) + b_conv1)
        h_pool1 = self.max_pool_2x2(h_conv1)

        h_conv2 = tf.nn.relu(self.conv2d(h_pool1, w_conv2) + b_conv2)
        h_pool2 = self.max_pool_2x2(h_conv2)

        h_conv3 = tf.nn.relu(self.conv2d(h_pool2, w_conv3) + b_conv3)
        h_pool3 = self.max_pool_2x2(h_conv3)

        h_conv4 = tf.nn.relu(self.conv2d(h_pool3, w_conv4) + b_conv4)
        h_pool4 = self.max_pool_2x2(h_conv4)

        # fully connected layer
        shape  = h_pool4.get_shape().as_list()

        h_pool4_flat = tf.reshape(h_pool4, [-1, shape[1] * shape[2] * shape[3]])

        h_pool4_flat_dropout = tf.nn.dropout(h_pool4_flat, self.tf_keep_prob, seed=self.seed)
        h_fc1 = tf.nn.relu(tf.matmul(h_pool4_flat_dropout, w_fc1) + b_fc1)

        # dropout
        h_fc1_dropout = tf.nn.dropout(h_fc1, self.tf_keep_prob, seed=self.seed)
        h_fc2 = tf.nn.relu(tf.matmul(h_fc1_dropout, w_fc2)+b_fc2)

        # readout layer
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

        self.tf_loss = tf.maximum(tf.reduce_mean(softmax_len), tf.constant(0.0))
        self.tf_loss += tf.maximum(tf.reduce_mean(softmax_d1), tf.constant(0.0))
        self.tf_loss += tf.maximum(tf.reduce_mean(softmax_d2), tf.constant(0.0))
        self.tf_loss += tf.maximum(tf.reduce_mean(softmax_d3), tf.constant(0.0))
        self.tf_loss += tf.maximum(tf.reduce_mean(softmax_d4), tf.constant(0.0))
        self.tf_loss += tf.maximum(tf.reduce_mean(softmax_d5), tf.constant(0.0))
        # self.tf_loss += tf.reduce_mean(softmax_d6)

        # loss optimizer 
        self.tf_optimizer = tf.train.AdamOptimizer(learning_rate=self.tf_learning_rate).minimize(self.tf_loss)

        # accuracy calculation
        pred_combined = tf.stack([pred_len, pred_d1, pred_d2, pred_d3, pred_d4, pred_d5, pred_d6], axis=1)
        predict = tf.reshape(pred_combined, (-1, 70))

        print(predict)
        print(self.tf_y_)

        is_correct_pred = tf.equal(
            tf.argmax(predict, 1), tf.argmax(self.tf_y_, 1))
        self.tf_accuracy = tf.reduce_mean(tf.cast(is_correct_pred, tf.float32))

        self.tf_debug1 = predict
        self.tf_debug2 = self.tf_y_
        self.tf_debug3 = tf.argmax(predict, 1)
        self.tf_debug4 = tf.argmax(self.tf_y_, 1)


    def train(self):
        if not self.is_model_initialized:
            raise AssertionError('you must initilize model using set_model function')

        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            shuffle_step = 0

            _log('we\'re about to training using %d trainset...' % self.train_dataset[0].shape[0])
            _log('now gonna makeing the dataset shuffled...')
            indices = np.random.permutation(range(self.train_dataset[0].shape[0]))

            for i, _ in enumerate(self.train_dataset):
                self.train_dataset[i] = self.train_dataset[i][indices]

            for i in range(20000):

                # This problem is somewhat inappropriate.
                #
                # batch = tf.train.shuffle_batch(self.train_dataset,
                #                                batch_size=32,
                #                                capacity=50000,
                #                                min_after_dequeue=10000)

                # Batching data
                batch_size = 50

                if self.train_dataset[0].shape[0] <= batch_size * (shuffle_step+1):
                    _log('now gonna makeing the dataset shuffled...')
                    indices = np.random.permutation(range(self.train_dataset[0].shape[0]))

                    for i, _ in enumerate(self.train_dataset):
                        self.train_dataset[i] = self.train_dataset[i][indices]

                    shuffle_step = 0
                else:
                    shuffle_step += 1

                # Need to change label dataset according to label 
                batch = [
                    self.train_dataset[0][shuffle_step*batch_size:shuffle_step*batch_size+batch_size],
                    self.train_dataset[4][shuffle_step*batch_size:shuffle_step*batch_size+batch_size],
                    self.train_dataset[1][shuffle_step*batch_size:shuffle_step*batch_size+batch_size]]

                feed_train ={self.tf_x: batch[0],
                             self.tf_y_: batch[1],
                             self.tf_learning_rate: 3.1e-4,
                             self.tf_l2_beta: 16e-4,
                             self.tf_keep_prob: 0.5}

                feed_test = {self.tf_x: self.test_dataset[0],
                             self.tf_y_: self.test_dataset[4],
                             self.tf_learning_rate: 3.1e-4,
                             self.tf_l2_beta: 16e-4,
                             self.tf_keep_prob: 1.}

                # Logging training
                if not i % 100:

                    # Check batch images for the training
                    if False:

                        fig = plt.figure(figsize=(12, 1), dpi=80)

                        for i in range(12):
                            plt.subplot(1, 12, i+1)
                            plt.title(batch[2][i])
                            plt.imshow(batch[0][i,:,:].reshape(64, 64),
                                       interpolation='nearest',
                                       cmap='Greys')
                            plt.tight_layout()

                        plt.show()

                    _loss, _train_accuracy = sess.run([self.tf_loss, self.tf_accuracy],
                                                      feed_dict=feed_test)

                    print("step %d, loss : %g / training_accuracy: %g" %
                          (i, _loss, _train_accuracy))

                # Do training
                self.tf_optimizer.run(feed_dict=feed_train)

            print('Test Accuracy %g' % (self.tf_accuracy.eval(feed_dict=feed_test)))
        return


def train_for_mnist_normal():
    dataset = 'mnist'

    loader = MNISTLoader()
    loader.init_data()

    trainer = CNNTrainer([None, 28, 28, 1], [None, 10])

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
    dataset = 'mnist'

    loader = MNISTLoader()
    loader.init_data()

    trainer = CNNTrainer([None, 64, 64, 1], [None, 70])

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

    # train_length_1hot_lbl = np.array(loader.label_to_onehot(trainer.train_dataset[3]+1))
    # train_digit_1hot_lbl = np.array([[loader.label_to_onehot(digit)] for digit in trainer.train_dataset[2].T])
    # T = np.transpose(train_digit_1hot_lbl, (1,2,0,3))    

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

def main():
    # train_for_mnist_normal()
    train_for_mnist_synthetic()

if __name__ == '__main__':
    main()
