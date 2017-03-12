from __future__ import print_function

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from PIL import Image

from data_loader import MNISTLoader, SVHNLoader, generate_trainset_testset

_DEBUG = True

def _log(message, end='\r\n'):
    if _DEBUG:
        print(message, end=end)

class Trainer:
    tf_x = None
    tf_y_ = None

    tf_keep_prob = None

    train_dataset = None
    test_dataset = None

    tf_optimizer = None
    tf_accuracy = None
    tf_loss = None

    image_shape = None
    label_shape = None

    is_model_initialized = False

    tf_debug1 = None
    tf_debug2 = None
    tf_debug3 = None
    tf_debug4 = None

    def __init__(self, image_shape=[None, 32, 32, 3], label_shape=[None, 10]):
        self.image_shape = image_shape
        self.label_shape = label_shape

        self.tf_x = tf.placeholder(tf.float32, self.image_shape)
        self.tf_y_ = tf.placeholder(tf.float32, self.label_shape)

        self.tf_keep_prob = tf.placeholder(tf.float32)

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

    def set_model(self):
        self.is_model_initialized = True

        x_input = tf.reshape(self.tf_x, [-1, 28, 28, 1])

        # convolution vector definition
        w_conv1 = self.weight_variable([5, 5, 1, 32])
        b_conv1 = self.bias_variable([32])

        w_conv2 = self.weight_variable([5, 5, 32, 64])
        b_conv2 = self.bias_variable([64])

        # w_conv3 = self.weight_variable([5, 5, 32, 64])
        # b_conv3 = self.bias_variable([64])

        # # w_conv4 = self.weight_variable([5, 5, 32, 32])
        # # b_conv4 = self.bias_variable([32])

        # w_conv5 = self.weight_variable([5, 5, 32, 128])
        # b_conv5 = self.bias_variable([128])

        w_fc1 = self.weight_variable([7 * 7 * 64, 1024])
        b_fc1 = self.bias_variable([1024])

        w_fc2 = self.weight_variable([1024, 10])
        b_fc2 = self.bias_variable([10])

        # convolution layer
        h_conv1 = tf.nn.relu(self.conv2d(x_input, w_conv1) + b_conv1)
        h_pool1 = self.max_pool_2x2(h_conv1)

        h_conv2 = tf.nn.relu(self.conv2d(h_pool1, w_conv2) + b_conv2)
        h_pool2 = self.max_pool_2x2(h_conv2)

        # h_conv3 = tf.nn.relu(self.conv2d(h_conv1, w_conv3) + b_conv3)
        # h_pool3 = self.max_pool_2x2(h_conv3)

        # # h_conv4 = tf.nn.relu(self.conv2d(h_pool3, w_conv4) + b_conv4)
        # # h_pool4 = self.max_pool_2x2(h_conv4)

        # h_conv5 = tf.nn.relu(self.conv2d(h_pool3, w_conv5) + b_conv5)
        # h_pool5 = self.max_pool_2x2(h_conv5)

        # fully connected layer
        h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
        h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, w_fc1) + b_fc1)

        # dropout
        h_fc1_dropout = tf.nn.dropout(h_fc1, self.tf_keep_prob)

        # readout layer
        predict = tf.matmul(h_fc1_dropout, w_fc2) + b_fc2

        # loss calculation
        softmax_cross_entropy = tf.nn.softmax_cross_entropy_with_logits(labels=self.tf_y_,
                                                          logits=predict)
        self.tf_loss = tf.reduce_mean(softmax_cross_entropy)

        # loss optimizer 
        self.tf_optimizer = tf.train.AdamOptimizer(1e-4).minimize(self.tf_loss)

        # accuracy calculation
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
                    self.train_dataset[0] = self.train_dataset[0][indices]
                    self.train_dataset[1] = self.train_dataset[1][indices]
                    self.train_dataset[2] = self.train_dataset[2][indices]
                    shuffle_step = 0
                else:
                    shuffle_step += 1

                batch = [
                    self.train_dataset[0][shuffle_step*batch_size:shuffle_step*batch_size+batch_size],
                    self.train_dataset[2][shuffle_step*batch_size:shuffle_step*batch_size+batch_size],
                    self.train_dataset[1][shuffle_step*batch_size:shuffle_step*batch_size+batch_size]]

                # Logging training
                if not i % 100:

                    # Check batch images for the training
                    if False:
                        fig = plt.figure(figsize=(12, 3), dpi=80)
                        for i in range(12):
                            plt.subplot(1, 12, i+1)
                            plt.title(batch[2][i])
                            plt.imshow(batch[0][i,:,:].reshape(28,28),
                                       interpolation='nearest',
                                       cmap='Greys')
                            plt.tight_layout()
                            plt.show()

                    _loss, _train_accuracy = sess.run([self.tf_loss, self.tf_accuracy],
                                                      feed_dict={self.tf_x: batch[0],
                                                                 self.tf_y_: batch[1],
                                                                 self.tf_keep_prob: 1.0})

                    print("step %d, loss : %g / training_accuracy: %g" %
                          (i, _loss, _train_accuracy))

                # Do training

                # print(self.tf_debug1.eval(
                #     feed_dict={self.x: batch[0],
                #                self.y_: batch[1],
                #                self.keep_prob: 0.5}))

                # print(self.tf_debug2.eval(
                #     feed_dict={self.x: batch[0],
                #                self.y_: batch[1],
                #                self.keep_prob: 0.5}))

                # print(self.tf_debug3.eval(
                #     feed_dict={self.x: batch[0],
                #                self.y_: batch[1],
                #                self.keep_prob: 0.5}))

                # print(self.debug4.eval(
                #     feed_dict={self.x: batch[0],
                #                self.y_: batch[1],
                #                self.keep_prob: 0.5}))

                self.tf_optimizer.run(
                    feed_dict={self.tf_x: batch[0],
                               self.tf_y_: batch[1],
                               self.tf_keep_prob: 0.5})

            print('Test Accuracy %g' % (self.tf_accuracy.eval(
                feed_dict={self.tf_x: batch[0],
                           self.tf_y_: batch[1],
                           self.tf_keep_prob: 1.0})))

        return


def main():
    dataset = 'mnist'

    loader = MNISTLoader()
    loader.init_data()

    trainer = Trainer([None, 28, 28, 1], [None, 10])

    _log('data loading...', end='\r\n')

    trainer.train_dataset = list(loader.get_data("training"))
    trainer.test_dataset = list(loader.get_data("testing"))

    trainer.train_dataset[0] = trainer.train_dataset[0].reshape([-1, 28, 28, 1])
    trainer.test_dataset[0] = trainer.test_dataset[0].reshape([-1, 28, 28, 1])
    trainer.train_dataset[1] = trainer.train_dataset[1]
    trainer.test_dataset[1] = trainer.test_dataset[1]

    trainer.train_dataset.append(np.array(loader.label_to_onehot(trainer.train_dataset[1])))
    trainer.test_dataset.append(np.array(loader.label_to_onehot(trainer.test_dataset[1])))

    _log('Done')

    _log('data validation...', end='\r\n')

    # To check image input
    _log('chking image data')
    _log(trainer.train_dataset[0].shape)
    _log(trainer.train_dataset[0][0,:,:].shape)

    # if _DEBUG:
    # fig = plt.figure()
    # fig.add_subplot(1, 1, 1)
    # plt.imshow(trainer.train_dataset[0][0,:,:],
    #                 interpolation='nearest',
    #                 cmap='Greys')
    # plt.show()

    # To check label input
    _log('checking label data')
    _log(trainer.train_dataset[1].shape)
    _log(trainer.train_dataset[1][0])
    _log('Done')

    _log('training.', end='\r\n')
    trainer.set_model()
    trainer.train()
    _log('Done')

if __name__ == '__main__':
    main()
