from __future__ import print_function
import os
import os.path
import urllib2

import scipy.io as sio
import numpy as np

DEBUG = False


def _log(message):
    if DEBUG:
        print(message)


class TrainDataLoader:
    # full numbers format
    hostname = None
    dirname = None

    # download list
    download_filelist = {
        # 'format1_train': 'train.tar.gz',
        # 'format1_test': 'test.tar.gz',
        # 'format1_extra': 'extra.tar.gz',
        'format2_train': 'train_32x32.mat',
        'format2_test': 'test_32x32.mat',
        'format2_extra': 'extra_32x32.mat',
    }

    train_file_name = 'train_32x32.mat'
    test_file_name = 'test_32x32.mat'

    def __init__(self, download_directory,
                 download_url_prefix='http://ufldl.stanford.edu/housenumbers/'):

        self.dirname = download_directory
        self.hostname = download_url_prefix

    def download_data(self):

        if not os.path.exists(self.dirname):
            _log('create directory : %s' % (self.dirname))
            os.mkdir(self.dirname)

        for k_type, v_filename in self.download_filelist.iteritems():
            if os.path.isfile(self.dirname + v_filename):
                _log('%s already has been downloaded.',
                     self.dirname + v_filename)
            else:
                _log('%s downloading into %s' %
                     (v_filename, self.dirname + v_filename))

                url = self.hostname + v_filename
                response = urllib2.urlopen(url)

                meta = response.info()
                file_size = int(meta.getheaders('Content-Length')[0])

                _log('Downloading: %s byte: %s' % (v_filename, file_size))

                file_size_dl = 0
                block_sz = 4 * 8192

                with open(self.dirname + v_filename, 'wb') as f:
                    while True:
                        buffer = response.read(block_sz)
                        if not buffer:
                            break

                        file_size_dl += len(buffer)
                        f.write(buffer)

                        status = r"%10d [%3.2f%%]" % (
                            file_size_dl, 100. * file_size_dl / file_size)
                        status = status + chr(8) * (len(status) + 1)
                        _log(status, end='')

    def load_test_data(self):
        test_dict = sio.loadmat(self.dirname + self.test_file_name)
        X = np.asarray(test_dict['X'])
        _log(X.shape)

        X_test = []
        for i in range(X.shape[3]):
            X_test.append(X[:, :, :, i])
        X_test = np.asarray(X_test)
        _log(X_test.shape)

        # because the value of 10 has been represented '10',
        # we would make it translated into '0'
        Y_test = np.array(test_dict['y'])
        count_distinct_value = len(np.unique(Y_test))

        for i in range(len(Y_test)):
            if not Y_test[i] % 10:
                Y_test[i] = 0

        # I'll use numpy advanced indexing for one-hot encoding implementation
        y_1hot_label = np.zeros((Y_test.shape[0], count_distinct_value))
        y_1hot_label[np.arange(Y_test.shape[0]), np.transpose(Y_test)] = 1

        return (X_test, y_1hot_label)

    def load_train_data(self):
        train_dict = sio.loadmat(self.dirname + self.train_file_name)
        X = np.asarray(train_dict['X'])
        _log(X.shape)

        X_train = []
        for i in range(X.shape[3]):
            X_train.append(X[:, :, :, i])
        X_train = np.asarray(X_train)
        _log(X_train.shape)

        # because the value of 10 has been represented '10',
        # we would make it translated into '0'
        Y_train = np.array(train_dict['y'])
        count_distinct_value = len(np.unique(Y_train))

        for i in range(len(Y_train)):
            if not Y_train[i] % 10:
                Y_train[i] = 0

        # I'll use numpy advanced indexing for one-hot encoding implementation
        y_1hot_label = np.zeros((Y_train.shape[0], count_distinct_value))
        y_1hot_label[np.arange(Y_train.shape[0]), np.transpose(Y_train)] = 1

        return (X_train, y_1hot_label)


def main():
    dirname = 'SVHN_data/'
    loader = TrainDataLoader(dirname)

    # loader.download_data('SVHN_data/')
    # X_train, y_train = loader.load_train_data()
    X_test, y_test = loader.load_test_data()

    # print(X_train.shape)
    # print(y_train.shape)

    print(X_test.shape)
    print(y_test.shape)


if __name__ == '__main__':
    main()
