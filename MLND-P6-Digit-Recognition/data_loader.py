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

from six.moves import cPickle as pickle
from six.moves import range
from six.moves.urllib.request import urlretrieve

_DEBUG = True


def _log(message):
    if _DEBUG:
        print(message)


class Loader(object):
    base_url = None
    dest_folder = None

    image_width = None
    image_height = None
    image_channel = None

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

    def maybe_untargz(filename, dest_folder, force=False):
        extraction_dir = filename.split('.')[0]
        if not os.path.isdir(extraction_dir):
            tar = tarfile.open(filename, 'r:gz')
            tar.extractall(dest_folder)
            tar.close()

            print(filename + " extracted to " + extraction_dir)
        else:
            print("Folder" + extraction_dir + " already exists. Skipping")

    def saveAsPickle(data, filename):
        try:
            with open(filename, 'wb') as f:
                pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
                print(filename + " pickled!")
        except Exception as e:
            print('Unable to save data to ', filename, ':', e)

    def loadPickle(file):
        with open(file, 'rb') as pickle_file:
            return pickle.load(pickle_file)

    def split_validation(train_data, train_label, split_ratio=0.9):

        permutation_indices = np.random.permutation(train_data.index)
        split_pos = int(train_data.shape[0] * split_ratio)

        train_data_reidx = train_data.reindex(permutation_indices).reset_index(
            drop=True)
        valid_dt_set = train_data_reidx[split_pos:].reset_index(drop=True)
        train_dt_set = train_data_reidx[:split_pos]

        train_lb_reidx = train_label.reindex(permutation_indices).reset_index(
            drop=True)
        valid_lb_set = train_lb_reidx[split_pos:].reset_index(drop=True)
        train_lb_set = train_lb_reidx[:split_pos]

        return (train_dt_set, train_lb_set, valid_dt_set, valid_lb_set)


class MNISTLoader(Loader):
    def __init__(self):

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
            to take the path from your environment variable ``MNIST``. The data can
            be downloaded from http://yann.lecun.com/exdb/mnist/.
        asbytes : bool
            If True, returns data as ``numpy.uint8`` in [0, 255] as opposed to
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
            Image data of shape ``(N, rows, cols)``, where ``N`` is the number of images. If neither labels nor inices are returned, then this is returned directly, and not inside a 1-sized tuple.
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
            images = images.astype(float) / 255.0

        ret = (images, )
        if return_labels:
            ret += (labels, )
        if return_indices:
            ret += (indices, )
        if len(ret) == 1:
            return ret[0]  # Don't return a tuple of one
        else:
            return ret

    def validate_data(self, data):
        """
        Prints digits as image along with their labels
        """

        if _DEBUG:
            img_labels = data[1]
            img_data = (data[0] * 255).astype(int)
            indices = np.random.randint(img_data.shape[0] - 1, size=12)
            fig = plt.figure(figsize=(1, 12), dpi=80)

            for index, indice in enumerate(indices):
                plt.subplot(10, 12, index + 1)
                plt.title(img_labels[indice])
                plt.imshow(
                    img_data[indice], interpolation='nearest', cmap='Greys')
                plt.tight_layout()

            plt.show()


class SVHNLoader(Loader):
    def __init__(self):

        self.dest_folder = 'SVHN_data/'
        self.base_url = 'http://ufldl.stanford.edu/housenumbers/'

        self.image_width = 32
        self.image_height = 32
        self.image_channel = 3

    def download_data(self):
        svhn_train_images = Loader.maybe_download(
            self.base_url, self.dest_folder, 'train_32x32.mat', 182040794)
        svhn_test_images = Loader.maybe_download(
            self.base_url, self.dest_folder, 'test_32x32.mat', 64275384)
        svhn_extra_images = Loader.maybe_download(
            self.base_url, self.dest_folder, 'extra_32x32.mat', 1329278602)

    def load_data(self, dataset='training', digits=None):
        files = {'training': 'train_32x32.mat', 'testing': 'test_32x32.mat'}

        try:
            data_fname = os.path.join(self.dest_folder, files[dataset])
        except KeyError:
            raise ValueError("Data set must be 'testing' or 'training'")

        loaded_dict = sio.loadmat(data_fname)
        X = loaded_dict['X']
        _log(X.shape)

        # change the matrix's shape
        X_ret = []
        for i in range(X.shape[3]):
            X_ret.append(X[:, :, :, i])
        X_ret = (np.asarray(X_ret).astype(float)) / 256.
        _log(X_ret.shape)

        # because the value of 10 has been represented '10',
        # we would make it translated into '0'
        y_ret = loaded_dict['y']
        count_distinct_value = len(np.unique(y_ret))

        for i in range(len(y_ret)):
            if not y_ret[i] % 10:
                y_ret[i] = 0

        # I'll use numpy advanced indexing for one-hot encoding implementation
        y_ret_1hot = np.zeros((y_ret.shape[0], count_distinct_value))
        y_ret_1hot[np.arange(y_ret.shape[0]), np.transpose(y_ret)] = 1

        indices = []
        if digits is not None:
            indices = np.where(
                y_ret == digits)[0]  # y_ret matrix was n by 1 matrix
        else:
            indices = range(y_ret.shape[0])

        _log("%d of digit %d was selected : " % (len(indices), digits))

        ret = (X_ret[indices, :, :, :], )
        ret += (y_ret_1hot[indices, :], )
        ret += (y_ret[indices], )

        return ret

    def validate_data(self, data):
        """
        Prints digits as image along with their labels
        """
        if _DEBUG:
            img_labels = data[2]
            img_1hot_lables = data[1]
            img_data = data[0]
            indices = np.random.randint(img_data.shape[0] - 1, size=12)
            fig = plt.figure(figsize=(12, 3), dpi=80)

            for index, indice in enumerate(indices):
                plt.subplot(1, 12, index + 1)
                plt.title(img_labels[indice])
                plt.imshow(img_data[indice], interpolation='nearest')
                plt.tight_layout()

            plt.show()


def main():
    mnist_loader = MNISTLoader()
    svhn_loader = SVHNLoader()

    mnist_loader.download_data()
    svhn_loader.download_data()

    # serialize mnist data into pickle format
    # training_data_digits = list()
    # for i in range(10):
    #     l = list()
    #     l.append(i)

    #     d = mnist_loader.load_data(
    #         dataset="training",
    #         digits=l,
    #         path=mnist_loader.dest_folder,
    #         asbytes=False,
    #         selection=None,
    #         return_labels=True,
    #         return_indices=False)

    #     Loader.saveAsPickle(
    #         d,
    #         os.path.join(mnist_loader.dest_folder,
    #                      "mnist_training_digit_" + str(i) + ".pickle"))
    #     training_data_digits.append(d)

    for i in range(0, 10):
        da = Loader.loadPickle(
            os.path.join(mnist_loader.dest_folder, "mnist_training_digit_" +
                         str(i) + ".pickle"))
        # mnist_loader.validate_data(da)

        train_dt, train_lb, valid_dt, valid_lb = Loader.split_validation(da[0], da[1])

        print('train_dt size : %d' % train_dt.shape[0])
        print('train_lb size : %d' % train_lb.shape[0])
        print('valid_dt size : %d' % valid_dt.shape[0])
        print('valid_lb size : %d' % valid_lb.shape[0])

    # serialize svhn data into pickle format
    # for i in range(10):

    #     d = svhn_loader.load_data('training', digits=i)

    #     Loader.saveAsPickle(
    #         d,
    #         os.path.join(svhn_loader.dest_folder,
    #                      "svhn_training_digit_" + str(i) + ".pickle"))

    for i in range(0, 10):

        da = Loader.loadPickle(
            os.path.join(svhn_loader.dest_folder, "svhn_training_digit_" + str(
                i) + ".pickle"))
        # svhn_loader.validate_data(da)


if __name__ == '__main__':
    main()
