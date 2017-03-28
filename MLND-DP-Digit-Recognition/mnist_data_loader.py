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
            trainset_lbl += Loader.generate_numbers(9, 1000).tolist()
            trainset_lbl += Loader.generate_numbers(99, 1000).tolist()
            trainset_lbl += Loader.generate_numbers(999, 1000).tolist()
            trainset_lbl += Loader.generate_numbers(9999, 1000).tolist()
            trainset_lbl += Loader.generate_numbers(99999, 1000).tolist()

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
            testset_lbl += Loader.generate_numbers(9, 400).tolist()
            testset_lbl += Loader.generate_numbers(99, 400).tolist()
            testset_lbl += Loader.generate_numbers(999, 400).tolist()
            testset_lbl += Loader.generate_numbers(9999, 400).tolist()
            testset_lbl += Loader.generate_numbers(99999, 400).tolist()

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


class MNISTLoader(Loader):

    training_data_digits = None
    testing_data_digits = None

    training_data = None
    testing_data = None

    def __init__(self):

        self.pickle_prefix = 'mnist'
        self.dest_folder = 'MNIST_data/'
        self.base_url = 'http://yann.lecun.com/exdb/mnist/'

        self.image_width = 28
        self.image_height = 28
        self.image_channel = 1

    def download_data(self):
        mnist_train_images = Loader.maybe_download(
            self.base_url, self.dest_folder, 'train-images-idx3-ubyte.gz',
            9912422)
        mnist_train_labels = Loader.maybe_download(
            self.base_url, self.dest_folder, 'train-labels-idx1-ubyte.gz',
            28881)
        mnist_test_images = Loader.maybe_download(
            self.base_url, self.dest_folder, 't10k-images-idx3-ubyte.gz',
            1648877)
        mnist_test_labels = Loader.maybe_download(
            self.base_url, self.dest_folder, 't10k-labels-idx1-ubyte.gz', 4542)

        files = [mnist_train_images, mnist_train_labels]

        for file in files:
            filepath = os.path.join(self.dest_folder, file)
            inF = gzip.open(filepath, 'rb')
            outF = open(filepath.split(".", 2)[0], 'wb')
            outF.write(inF.read())
            inF.close()
            outF.close()

    def init_data(self):
        if self.training_data_digits or self.testing_data_digits:
            raise AssertionError('MNIST dataset may be initialized.')

        if not os.path.exists(
                os.path.join(self.dest_folder, "mnist_training_all.pickle")):
            self.training_data = self.load_data(dataset="training", path=self.dest_folder)
            Loader.saveAsPickle(self.training_data,
                                os.path.join(self.dest_folder,
                                             "mnist_training_all.pickle"))

        if not os.path.exists(
                os.path.join(self.dest_folder, "mnist_testing_all.pickle")):
            self.testing_data = self.load_data(dataset="testing", path=self.dest_folder)
            Loader.saveAsPickle(self.testing_data,
                                os.path.join(self.dest_folder,
                                             "mnist_testing_all.pickle"))

        for i in range(10):
            l = list()
            l.append(i)

            if not os.path.exists(
                    os.path.join(self.dest_folder, "mnist_training_digit_" +
                                 str(i) + ".pickle")):
                d = self.load_data(
                    dataset="training",
                    digits=l,
                    path=self.dest_folder,
                    asbytes=False,
                    selection=None,
                    return_labels=True,
                    return_indices=False)

                Loader.saveAsPickle(
                    d,
                    os.path.join(self.dest_folder,
                                 "mnist_training_digit_" + str(i) + ".pickle"))

            if not os.path.exists(
                    os.path.join(self.dest_folder, "mnist_testing_digit_" +
                                 str(i) + ".pickle")):

                d = self.load_data(
                    dataset="testing",
                    digits=l,
                    path=self.dest_folder,
                    asbytes=False,
                    selection=None,
                    return_labels=True,
                    return_indices=False)

                Loader.saveAsPickle(
                    d,
                    os.path.join(self.dest_folder,
                                 "mnist_testing_digit_" + str(i) + ".pickle"))

        self.training_data = Loader.loadPickle(
                os.path.join(self.dest_folder,
                             "mnist_training_all.pickle"))

        self.testing_data = Loader.loadPickle(
            os.path.join(self.dest_folder,
                         "mnist_testing_all.pickle"))

        self.training_data_digits = [
            Loader.loadPickle(
                os.path.join(self.dest_folder, "mnist_training_digit_" + str(i)
                             + ".pickle")) for i in range(10)
        ]

        self.testing_data_digits = [
            Loader.loadPickle(
                os.path.join(self.dest_folder, "mnist_testing_digit_" + str(i)
                             + ".pickle")) for i in range(10)
        ]


    def load_data(self,
                    dataset="training",
                    digits=None,
                    path="",
                    asbytes=False,
                    selection=None,
                    return_labels=True,
                    return_indices=False):
        """
        from: https://raw.githubusercontent.com/amitgroup/amitgroup/master/amitgroup/io/mnist.py
        Loads MNIST files into a 3D numpy array.

        Parameters
        ----------
        dataset : str
            Either "training" or "testing", depending on which dataset you want to
            load.
        digits : list
            Integer list of digits to load. The entire database is loaded if set to
            ``None``. Default is ``None``.
        path : str
            Path to your MNIST datafiles. The default is ``None``, which will try
            to take the path from your environment variable ``MNIST``. The images can
            be downloaded from http://yann.lecun.com/exdb/mnist/.
        asbytes : bool
            If True, returns images as ``numpy.uint8`` in [0, 255] as opposed to
            ``numpy.float64`` in [0.0, 1.0].
        selection : slice
            Using a `slice` object, specify what subset of the dataset to load. An
            example is ``slice(0, 20, 2)``, which would load every other digit
            until--but not including--the twentieth.
        return_labels : bool
            Specify whether or not labels should be returned. This is also a speed
            performance if digits are not specified, since then the labels file
            does not need to be read at all.
        return_indicies : bool
            Specify whether or not to return the MNIST indices that were fetched.
            This is valuable only if digits is specified, because in that case it
            can be valuable to know how far
            in the database it reached.

        Returns
        -------
        images : ndarray
            Image images of shape ``(N, rows, cols)``, where ``N`` is the numbers of images. If neither labels nor inices are returned, then this is returned directly, and not inside a 1-sized tuple.
        labels : ndarray
            Array of size ``N`` describing the labels. Returned only if ``return_labels`` is `True`, which is default.
        indices : ndarray
            The indices in the database that were returned.
        """

        # The files are assumed to have these names and should be found in
        # 'path'
        files = {
            'training': ('train-images-idx3-ubyte', 'train-labels-idx1-ubyte'),
            'testing': ('t10k-images-idx3-ubyte', 't10k-labels-idx1-ubyte'),
        }

        try:
            images_fname = os.path.join(path, files[dataset][0])
            labels_fname = os.path.join(path, files[dataset][1])
        except KeyError:
            raise ValueError("Data set must be 'testing' or 'training'")

        # We can skip the labels file only if digits aren't specified and
        # labels aren't asked for
        if return_labels or digits is not None:
            flbl = open(labels_fname, 'rb')
            magic_nr, size = struct.unpack(">II", flbl.read(8))
            labels_raw = pyarray("b", flbl.read())
            flbl.close()

        fimg = open(images_fname, 'rb')
        magic_nr, size, rows, cols = struct.unpack(">IIII", fimg.read(16))
        images_raw = pyarray("B", fimg.read())
        fimg.close()

        if digits:
            indices = [k for k in range(size) if labels_raw[k] in digits]
        else:
            indices = range(size)

        if selection:
            indices = indices[selection]
        N = len(indices)

        images = np.zeros((N, rows, cols), dtype=np.uint8)

        if return_labels:
            labels = np.zeros((N), dtype=np.int8)
        for i, index in enumerate(indices):
            images[i] = np.array(images_raw[indices[i] * rows * cols:(indices[
                i] + 1) * rows * cols]).reshape((rows, cols))
            if return_labels:
                labels[i] = labels_raw[indices[i]]

        if not asbytes:
            images = images.astype(float) / 255.

        ret = (images, )
        if return_labels:
            ret += (labels, )
        if return_indices:
            ret += (indices, )
        if len(ret) == 1:
            return ret[0]  # Don't return a tuple of one
        else:
            return ret

    def validate_data(self, images, labels, height=None, width=None):
        """
        Prints digits as image along with their labels
        """

        valid_size = min(images.shape[0], 12)
        height = self.image_height if not height else height
        width = self.image_width if not width else width

        if _DEBUG:
            img_data = (images * 255).astype(int)
            img_labels = labels

            indices = np.random.randint(
                img_data.shape[0] - 1,
                size=valid_size) if valid_size > 12 else range(valid_size)
            fig = plt.figure(figsize=(12, 3), dpi=80)

            for i, idx in enumerate(indices):
                plt.subplot(1, valid_size, i + 1)
                plt.title(img_labels[idx])
                plt.imshow(
                    img_data[idx].reshape(height, width),
                    interpolation='nearest',
                    cmap='Greys')
                plt.tight_layout()

            plt.show()

    def __get_digit_data_rand(self, digit, dataset="training"):
        if not self.training_data_digits or not self.testing_data_digits:
            raise AssertionError('MNIST dataset may be initialized.')

        if dataset == "training":
            return self.training_data_digits[digit][0][np.random.randint(
                self.training_data_digits[digit][0].shape[0])].reshape(
                    self.image_height, self.image_width)
        else:
            return self.testing_data_digits[digit][0][np.random.randint(
                self.testing_data_digits[digit][0].shape[0])].reshape(
                    self.image_height, self.image_width)

    def generate_mixed_digit_data(self,
                                  numbers,
                                  scale=1,
                                  max_length=6,
                                  dims=(64, 64)):

        images = np.zeros([len(numbers), dims[0], dims[1]])
        values = np.zeros(len(numbers)).astype(int)
        lengths = np.zeros([
            len(numbers),
        ]).astype(int)
        digits = np.zeros([len(numbers), 6]).astype(int)

        for i, number in enumerate(numbers):
            _log('generate %d\'s image...' % number)
            values[i] = int(number)

            # To store numbers list into digits list
            # if number is [123, 456], it will store [[1,2,3], [4,5,6]]
            num_digits = [int(j) for j in list(str(values[i]))]
            lengths[i] = min(len(num_digits), 6)
            digits[i, 0:lengths[i]] = num_digits[:lengths[i]]

            lengths[i] -= 1

            # generate mixed images. it will just paste images to righthand direction
            num_images = np.zeros(
                [self.image_height, self.image_width * len(num_digits)])
            for j, digit in enumerate(num_digits):

                v = self.__get_digit_data_rand(digit)
                num_images[0:self.image_height, j * self.image_width:(j + 1) *
                           self.image_width] = self.__get_digit_data_rand(
                               digit)

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
                   num_images.shape[1]] = num_images

        return (images, values, digits, lengths)


def testcase_for_loader():
    mnist_loader = MNISTLoader()
    mnist_loader.download_data()
    mnist_loader.init_data()
    dl1 = mnist_loader.get_digit_data(0, "training")
    # mnist_loader.validate_data(dl1[0], dl1[1])

    dt1 = mnist_loader.get_digit_data(0, "testing")
    # mnist_loader.validate_data(dt1[0], dt1[1])

    mnist_mixed_set = mnist_loader.get_mixed_data()

    mnist_loader.validate_data(mnist_mixed_set[0],
                               mnist_mixed_set[1], 64, 64)

    # cross validation testcase
    for i in range(0, 10):
        da = Loader.loadPickle(
            os.path.join(mnist_loader.dest_folder, "mnist_training_digit_" +
                         str(i) + ".pickle"))
        # mnist_loader.validate_data(da)

        train_dt, train_lb, valid_dt, valid_lb = Loader.split_validation(
            dl1[0], dl1[1])

        print('train_dt size : %d' % train_dt.shape[0])
        print('train_lb size : %d' % train_lb.shape[0])
        print('valid_dt size : %d' % valid_dt.shape[0])
        print('valid_lb size : %d' % valid_lb.shape[0])


def main():
    # testcase_for_loader()
    mnist_loader = MNISTLoader()
    mnist_loader.download_data()
    mnist_loader.init_data()

    encoded = Loader.label_to_onehot(
            np.array([0, 1, 2, 3, 4, 5]).reshape(6, 1))

    print(encoded)

    decoded = Loader.onehot_to_label(encoded)

    print(decoded)

    # mnist images serialization testcase
    training_data_digits = list()
    for i in range(10):
        l = list()
        l.append(i)

        d = mnist_loader.load_data(
            dataset="training",
            digits=l,
            path=mnist_loader.dest_folder,
            asbytes=False,
            selection=None,
            return_labels=True,
            return_indices=False)

        Loader.saveAsPickle(
            d,
            os.path.join(mnist_loader.dest_folder,
                         "mnist_training_digit_" + str(i) + ".pickle"))
        training_data_digits.append(d)


if __name__ == '__main__':
    main()
