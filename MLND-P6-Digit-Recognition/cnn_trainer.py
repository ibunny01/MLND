from __future__ import print_function

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from PIL import Image

from train_data_loader import DataLoader

__DEBUG = False


class Trainer:
    x = None
    y_ = None

    keep_prob = None

    train_dataset = None
    test_dataset = None

    optimizer = None
    accuracy = None
    loss = None

    def __init__(self, image_shape=[None, 32, 32, 3], label_shape=[None, 10]):
        self.x = tf.placeholder(tf.float32, image_shape)
        self.y_ = tf.placeholder(tf.float32, label_shape)
        self.keep_prob = tf.placeholder(tf.float32)

        return

    def weight_variable(self, shape):
        return tf.Variable(tf.truncated_normal(shape, stddev=0.1))

    def bias_variable(self, shape):
        return tf.Variable(tf.zeros(shape))

    def conv2d(self, x, W):
        return tf.nn.conv2d(x, W,
                            strides=[1, 1, 1, 1], padding='SAME')

    def max_pool_2x2(self, x):
        return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                              strides=[1, 2, 2, 1], padding='SAME')

    def set_model(self):
        x_input = tf.reshape(self.x, [-1, 32, 32, 3])

        # convolution vector definition
        w_conv1 = self.weight_variable([5, 5, 3, 16])
        b_conv1 = self.bias_variable([16])

        w_conv2 = self.weight_variable([5, 5, 16, 16])
        b_conv2 = self.bias_variable([16])

        w_conv3 = self.weight_variable([5, 5, 16, 32])
        b_conv3 = self.bias_variable([32])

        w_conv4 = self.weight_variable([5, 5, 32, 32])
        b_conv4 = self.bias_variable([32])

        w_conv5 = self.weight_variable([5, 5, 32, 128])
        b_conv5 = self.bias_variable([128])

        w_fc1 = self.weight_variable([1 * 1 * 128, 256])
        b_fc1 = self.bias_variable([256])

        w_fc2 = self.weight_variable([256, 10])
        b_fc2 = self.bias_variable([10])

        # convolution layer
        h_conv1 = tf.nn.relu(self.conv2d(x_input, w_conv1) + b_conv1)
        h_pool1 = self.max_pool_2x2(h_conv1)

        h_conv2 = tf.nn.relu(self.conv2d(h_pool1, w_conv2) + b_conv2)
        h_pool2 = self.max_pool_2x2(h_conv2)

        h_conv3 = tf.nn.relu(self.conv2d(h_pool2, w_conv3) + b_conv3)
        h_pool3 = self.max_pool_2x2(h_conv3)

        h_conv4 = tf.nn.relu(self.conv2d(h_pool3, w_conv4) + b_conv4)
        h_pool4 = self.max_pool_2x2(h_conv4)

        h_conv5 = tf.nn.relu(self.conv2d(h_pool4, w_conv5) + b_conv5)
        h_pool5 = self.max_pool_2x2(h_conv5)

        # fully connected layer
        h_pool5_flat = tf.reshape(h_pool5, [-1, 1 * 1 * 128])
        h_fc1 = tf.nn.relu(tf.matmul(h_pool5_flat, w_fc1) + b_fc1)

        # dropout
        h_fc1_dropout = tf.nn.dropout(h_fc1, self.keep_prob)

        # readout layer
        predict = tf.matmul(h_fc1_dropout, w_fc2) + b_fc2

        # loss calculation
        softmax = tf.nn.softmax_cross_entropy_with_logits(labels=self.y_,
                                                          logits=predict)
        self.loss = tf.reduce_mean(softmax)

        # accuracy calculation

        print(predict.shape)
        print(self.y_.shape)

        is_correct_pred = tf.equal(
            tf.argmax(predict, 1), tf.argmax(self.y_, 1))
        self.accuracy = tf.reduce_mean(tf.cast(is_correct_pred, tf.float32))

        self.optimizer = tf.train.AdamOptimizer(1e-1).minimize(self.loss)

    def train(self):
        self.set_model()

        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())

            for i in range(20000):

                # This problem is somewhat inappropriate.
                #
                # batch = tf.train.shuffle_batch(self.train_dataset,
                #                                batch_size=32,
                #                                capacity=50000,
                #                                min_after_dequeue=10000)

                # Batching data
                batch_size = 100

                np.random.shuffle(self.train_dataset[0])
                np.random.shuffle(self.train_dataset[1])

                batch = [
                    self.train_dataset[0][:batch_size],
                    self.train_dataset[1][:batch_size]]

                # Logging training
                if not i % 500:
                    _loss = self.loss.eval(
                        feed_dict={self.x: batch[0],
                                   self.y_: batch[1],
                                   self.keep_prob: 1.0}
                    )

                    _train_accuracy = self.accuracy.eval(
                        feed_dict={self.x: batch[0],
                                   self.y_: batch[1],
                                   self.keep_prob: 1.0})

                    print("step %d, loss : %g / training_accuracy: %g" %
                          (i, _loss, _train_accuracy))

                # Do training
                self.optimizer.run(
                    feed_dict={self.x: batch[0],
                               self.y_: batch[1],
                               self.keep_prob: 0.5})

            print('Test Accuracy %g' % (self.accuracy.eval(
                feed_dict={self.x: batch[0],
                           self.y_: batch[1],
                           self.keep_prob: 1.0}))
                  )

        return


def main():
    dirname = 'SVHN_data/'

    loader = DataLoader(dirname)
    trainer = Trainer()

    print('data loading...', end='\r\n')
    trainer.train_dataset = loader.load_train_data()
    trainer.test_dataset = loader.load_test_data()
    print('Done')

    if __DEBUG:
        print('data validation...', end='\r\n')
        # To check image input
        print('chking image data')
        fig = plt.figure()
        print(trainer.train_dataset[0][0].shape)
        image_data = Image.fromarray(trainer.train_dataset[0][0])
        fig.add_subplot(1, 1, 1)
        plt.imshow(image_data)
        plt.show()

        # To check label input
        print('checking label data')
        print(trainer.train_dataset[1][0])
        print('Done')

    print('training.', end='\r\n')
    trainer.train()
    print('Done')

if __name__ == '__main__':
    main()
