from __future__ import print_function

import gzip
import os
import os.path
import struct
import tarfile
from array import array as pyarray

import numpy as np
import scipy.io as sio
from matplotlib import pyplot as plt
from scipy.misc import imresize

from six.moves import cPickle as pickle
from six.moves import range
from six.moves.urllib.request import urlretrieve

_DEBUG = True


def _log(message):
    if _DEBUG:
        print(message)


class Loader(object):

    pickle_prefix = None
    base_url = None
    dest_folder = None

    image_width = None
    image_height = None
    image_channel = None

    training_data_digits = None
    testing_data_digits = None

    training_data = None
    testing_data = None

    training_mixed_data = None
    testing_mixed_data = None

    @staticmethod
    def maybe_download(base_url, dest_folder, filename, expected_bytes=None):
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)

        filepath = os.path.join(dest_folder, filename)

        if not os.path.exists(filepath):
            filepath, _ = urlretrieve(base_url + filename, filepath)

        statinfo = os.stat(filepath)

        if expected_bytes is None or statinfo.st_size == expected_bytes:
            print('Found and verified %s' % filename)
        else:
            print(statinfo.st_size)
            raise Exception('Failed to verify ' + filename +
                            '. Can you get to it with a browser ?')
        return filename

    @staticmethod
    def maybe_untargz(filename, dest_folder, force=False):
        extraction_dir = filename.split('.')[0]
        if not os.path.isdir(extraction_dir):
            tar = tarfile.open(filename, 'r:gz')
            tar.extractall(dest_folder)
            tar.close()

            print(filename + " extracted to " + extraction_dir)
        else:
            print("Folder" + extraction_dir + " already exists. Skipping")

    @staticmethod
    def saveAsPickle(images, filename):
        try:
            with open(filename, 'wb') as f:
                pickle.dump(images, f, pickle.HIGHEST_PROTOCOL)
                print(filename + " pickled!")
        except Exception as e:
            print('Unable to save images to ', filename, ':', e)

    @staticmethod
    def loadPickle(file):
        with open(file, 'rb') as pickle_file:
            return pickle.load(pickle_file)

    @staticmethod
    def split_validation(train_data, train_label, split_ratio=0.9):

        permutation_indices = np.random.permutation(train_data.shape[0])
        split_pos = int(train_data.shape[0] * split_ratio)

        train_data_reidx = train_data[permutation_indices]
        valid_dt_set = train_data_reidx[split_pos:]
        train_dt_set = train_data_reidx[:split_pos]

        train_lb_reidx = train_label[permutation_indices]
        valid_lb_set = train_lb_reidx[split_pos:]
        train_lb_set = train_lb_reidx[:split_pos]

        return (train_dt_set, train_lb_set, valid_dt_set, valid_lb_set)

    @staticmethod
    def generate_numbers(max_number, size):
        return np.random.randint(max_number, size=size)

    @staticmethod
    def label_to_onehot(original):
        decimal_kind_of_digit = 10

        count_distinct_value = max(len(np.unique(original)), decimal_kind_of_digit)
        label_1hot = np.zeros((original.shape[0], count_distinct_value))
        label_1hot[np.arange(original.shape[0]), np.transpose(original)] = 1

        return label_1hot

    @staticmethod
    def onehot_to_label(encoded):
        return np.array([np.where(e == 1)[0]
                         for e in np.rollaxis(encoded,0)]).reshape([-1])


    def init_data(self):
        raise NotImplementedError('Should have implemented this')

    def generate_mixed_digit_data(self,
                                  numbers,
                                  scale=1,
                                  max_length=6,
                                  dims=(64, 64)):
        raise NotImplementedError('Should have implemented this')

    def get_data(self, dataset="training"):
        if not self.training_data_digits or not self.testing_data_digits:
            raise AssertionError('MNIST dataset may be initialized.')

        if dataset == "training":
            return self.training_data
        else:
            return self.testing_data

    def get_digit_data(self, digit, dataset="training"):
        if not self.training_data_digits or not self.testing_data_digits:
            raise AssertionError('MNIST dataset may be initialized.')

        if dataset == "training":
            return self.training_data_digits[digit]
        else:
            return self.testing_data_digits[digit]

    def get_mixed_data(self, dataset="training"):

        if not os.path.exists(self.dest_folder):
            os.makedirs(self.dest_folder)

        if not os.path.exists(
                os.path.join(self.dest_folder,
                             self.pickle_prefix + "_training_mixed_set.pickle")):

            trainset_lbl = list()
            trainset_lbl += Loader.generate_numbers(9, 2000).tolist()
            trainset_lbl += Loader.generate_numbers(99, 2000).tolist()
            trainset_lbl += Loader.generate_numbers(999, 2000).tolist()
            trainset_lbl += Loader.generate_numbers(9999, 2000).tolist()
            trainset_lbl += Loader.generate_numbers(99999, 2000).tolist()

            trainset_lbl = np.array(trainset_lbl)
            trainset_lbl = trainset_lbl[np.random.permutation(trainset_lbl.shape[0])]
            trainset_lbl.reshape(trainset_lbl.shape[0])

            trainset_data = self.generate_mixed_digit_data(trainset_lbl)
            self.training_mixed_data = trainset_data

            Loader.saveAsPickle(self.training_mixed_data,
                                os.path.join(self.dest_folder,
                                             self.pickle_prefix + "_training_mixed_set.pickle"))

        self.training_mixed_data = Loader.loadPickle(os.path.join(self.dest_folder,
                                             self.pickle_prefix + "_training_mixed_set.pickle"))

        if not os.path.exists(
                os.path.join(self.dest_folder,
                             self.pickle_prefix + "_testing_mixed_set.pickle")):

            testset_lbl = list()
            testset_lbl += Loader.generate_numbers(9, 750).tolist()
            testset_lbl += Loader.generate_numbers(99, 750).tolist()
            testset_lbl += Loader.generate_numbers(999, 750).tolist()
            testset_lbl += Loader.generate_numbers(9999, 750).tolist()
            testset_lbl += Loader.generate_numbers(99999, 750).tolist()

            testset_lbl = np.array(testset_lbl)
            testset_lbl = testset_lbl[np.random.permutation(testset_lbl.shape[0])]
            testset_lbl.reshape(testset_lbl.shape[0])

            testset_data = self.generate_mixed_digit_data(testset_lbl)
            self.testing_mixed_data = testset_data

            Loader.saveAsPickle(self.testing_mixed_data,
                                os.path.join(self.dest_folder,
                                             self.pickle_prefix + "_testing_mixed_set.pickle"))

        self.testing_mixed_data = Loader.loadPickle(os.path.join(self.dest_folder,
                                             self.pickle_prefix + "_testing_mixed_set.pickle"))

        if dataset == "training":
            return self.training_mixed_data
        else:
            return self.testing_mixed_data


class SVHNFullLoader(Loader):

    def __init__(self):

        self.pickle_prefix = 'svhn_full'
        self.dest_folder = 'SVHN_full_data/'
        self.base_url = 'http://ufldl.stanford.edu/housenumbers/'

        self.image_width = 32
        self.image_height = 32
        self.image_channel = 3

    def init_data(self):
        if self.training_data_digits or self.testing_data_digits:
            raise AssertionError('svhn dataset may be initialized.')

        if not os.path.exists(
                os.path.join(self.dest_folder, "svhn_training_all.pickle")):
            self.training_data = self.load_data(dataset="training")
            Loader.saveAsPickle(self.training_data,
                                os.path.join(self.dest_folder,
                                             "svhn_training_all.pickle"))

        if not os.path.exists(
                os.path.join(self.dest_folder, "svhn_testing_all.pickle")):
            self.testing_data = self.load_data(dataset="testing")
            Loader.saveAsPickle(self.testing_data,
                                os.path.join(self.dest_folder,
                                             "svhn_testing_all.pickle"))

        for i in range(10):
            l = list()
            l.append(i)

            if not os.path.exists(
                    os.path.join(self.dest_folder, "svhn_training_digit_" +
                                 str(i) + ".pickle")):
                d = self.load_data(dataset="training", digits=l)

                Loader.saveAsPickle(
                    d,
                    os.path.join(self.dest_folder,
                                 "svhn_training_digit_" + str(i) + ".pickle"))

            if not os.path.exists(
                    os.path.join(self.dest_folder, "svhn_testing_digit_" + str(
                        i) + ".pickle")):

                d = self.load_data(dataset="testing", digits=i)

                Loader.saveAsPickle(
                    d,
                    os.path.join(self.dest_folder,
                                 "svhn_testing_digit_" + str(i) + ".pickle"))

        self.training_data = Loader.loadPickle(
                os.path.join(self.dest_folder,
                             "svhn_training_all.pickle"))

        self.testing_data = Loader.loadPickle(
            os.path.join(self.dest_folder,
                         "svhn_testing_all.pickle"))

        self.training_data_digits = [
            Loader.loadPickle(
                os.path.join(self.dest_folder, "svhn_training_digit_" + str(i)
                             + ".pickle")) for i in range(10)
        ]

        self.testing_data_digits = [
            Loader.loadPickle(
                os.path.join(self.dest_folder, "svhn_testing_digit_" + str(i) +
                             ".pickle")) for i in range(10)
        ]

    def download_data(self):
        svhn_train_images = Loader.maybe_download(
            self.base_url, self.dest_folder, 'train.tar.gz', 404141560)
        svhn_test_images = Loader.maybe_download(
            self.base_url, self.dest_folder, 'test.tar.gz', 276555967)
        svhn_extra_images = Loader.maybe_download(
            self.base_url, self.dest_folder, 'extra.tar.gz', 1955489752)

    def load_data(self, dataset='training', digits=None):
        files = {'training': 'train_32x32.mat', 'testing': 'test_32x32.mat'}

        try:
            data_fname = os.path.join(self.dest_folder, files[dataset])
        except KeyError:
            raise ValueError("Data set must be 'testing' or 'training'")

        loaded_dict = sio.loadmat(data_fname)
        X = loaded_dict['X']

        # change the matrix's shape
        X_ret = []
        for i in range(X.shape[3]):
            X_ret.append(X[:, :, :, i])
        X_ret = (np.asarray(X_ret).astype(float)) / 255.
 
        # because the value of 10 has been represented '10',
        # we would make it translated into '0'
        y_ret = loaded_dict['y']

        for i in range(len(y_ret)):
            if not y_ret[i] % 10:
                y_ret[i] = 0

        # I'll use numpy advanced indexing for one-hot encoding implementation
        y_ret_1hot = self.label_to_onehot(y_ret)

        indices = []
        if digits is not None:
            indices = np.where(
                y_ret == digits)[0]  # y_ret matrix was n by 1 matrix
        else:
            indices = range(y_ret.shape[0])

        _log("%d of digit %s was selected : " % (len(indices), digits))

        ret = (X_ret[indices, :, :, :], )
        ret += (y_ret[indices], )
        ret += (y_ret_1hot[indices, :], )

        return ret

    def validate_data(self, images, labels, height=None, width=None):
        """
        Prints digits as image along with their labels
        """

        valid_size = min(images.shape[0], 12)
        height = self.image_height if not height else height
        width = self.image_width if not width else width

        if _DEBUG:
            img_data = images
            img_labels = labels

            indices = np.random.randint(img_data.shape[0] - 1, size=valid_size)
            fig = plt.figure(figsize=(12, 3), dpi=80)

            for i, idx in enumerate(indices):
                plt.subplot(1, valid_size, i + 1)
                plt.title(img_labels[idx])
                plt.imshow(img_data[idx], interpolation='nearest')
                plt.tight_layout()

            plt.show()

    def __get_digit_data_rand(self, digit, dataset="training"):
        if not self.training_data_digits or not self.testing_data_digits:
            raise AssertionError('SVHN dataset may be initialized.')

        if dataset == "training":
            return self.training_data_digits[digit][0][np.random.randint(
                self.training_data_digits[digit][0].shape[0])]
        else:
            return self.testing_data_digits[digit][0][np.random.randint(
                self.testing_data_digits[digit][0].shape[0])]

    def generate_mixed_digit_data(self,
                                  numbers,
                                  scale=1,
                                  max_length=6,
                                  dims=(64, 64)):

        images = np.ones([len(numbers), dims[0], dims[1], self.image_channel])
        values = np.zeros(len(numbers)).astype(int)
        lengths = np.zeros([
            len(numbers),
        ]).astype(int)
        digits = np.zeros([len(numbers), 6]).astype(int)

        for i, number in enumerate(numbers):
            values[i] = int(number)

            # To store numbers list into digits list
            # if number is [123, 456], it will store [[1,2,3], [4,5,6]]
            num_digits = [int(j) for j in list(str(values[i]))]
            lengths[i] = min(len(num_digits), 6)
            digits[i, 0:lengths[i]] = num_digits[:lengths[i]]

            # generate mixed images. it will just paste images to righthand direction
            num_images = np.zeros([
                self.image_height, self.image_width * len(num_digits),
                self.image_channel
            ])
            for j, digit in enumerate(num_digits):

                v = self.__get_digit_data_rand(digit)
                num_images[0:self.image_height, j * self.image_width:(
                    j + 1) * self.image_width, 0:self.
                           image_channel] = self.__get_digit_data_rand(digit)

            # make pasted images to 64x64 matrix
            scale = float(dims[0]) / (self.image_width * (lengths[i] + 1))
            if scale != 1:
                num_images = imresize(num_images, scale, interp='bilinear')

            # make image list
            max_top = dims[0] - num_images.shape[0]
            max_left = dims[1] - num_images.shape[1]

            top = np.random.randint(0, max_top) if max_top > 0 else 0
            left = np.random.randint(0, max_left) if max_left > 0 else 0

            images[i, top:top + num_images.shape[0], left:left +
                   num_images.shape[1], 0:self.image_channel] = num_images

        return (images, values, digits, lengths)


def testcase_for_loader():
    svhn_full_loader = SVHNFullLoader()
    svhn_full_loader.download_data()
    svhn_full_loader.init_data()

    dl = svhn_full_loader.get_digit_data(1, "training")
    dt = svhn_full_loader.get_digit_data(1, "testing")

    svhn_mixed_set = svhn_full_loader.get_mixed_data()

    svhn_full_loader.validate_data(svhn_mixed_set[0],
                              svhn_mixed_set[1], 64, 64)

    # cross validation testcase
    for i in range(0, 10):
        da = Loader.loadPickle(
            os.path.join(svhn_full_loader.dest_folder, "svhn_training_digit_" +
                         str(i) + ".pickle"))
        # mnist_loader.validate_data(da)

        train_dt, train_lb, valid_dt, valid_lb = Loader.split_validation(
            dl[0], dl[1])

        print('train_dt size : %d' % train_dt.shape[0])
        print('train_lb size : %d' % train_lb.shape[0])
        print('valid_dt size : %d' % valid_dt.shape[0])
        print('valid_lb size : %d' % valid_lb.shape[0])


def main():
    testcase_for_loader()

    # svhn_full_loader = SVHNLoader()
    # svhn_full_loader.download_data()
    # svhn_full_loader.init_data()

    # encoded = Loader.label_to_onehot(
    #         np.array([0, 1, 2, 3, 4, 5]).reshape(6, 1))

    # print(encoded)

    # decoded = Loader.onehot_to_label(encoded)

    # print(decoded)

    # # serialize svhn images into pickle format
    # for i in range(10):

    #     d = svhn_full_loader.load_data('training', digits=i)

    #     Loader.saveAsPickle(
    #         d,
    #         os.path.join(svhn_full_loader.dest_folder,
    #                      "svhn_training_digit_" + str(i) + ".pickle"))

    # for i in range(0, 10):

    #     da = Loader.loadPickle(
    #         os.path.join(svhn_full_loader.dest_folder, "svhn_training_digit_" + str(
    #             i) + ".pickle"))
    #     # svhn_full_loader.validate_data(da)


if __name__ == '__main__':
    main()
