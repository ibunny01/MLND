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


# full numbers format
hostname = 'http://ufldl.stanford.edu/housenumbers/'

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


def download_data(dirname):

    if not os.path.exists(dirname):
        _log('create directory : %s' % (dirname))
        os.mkdir(dirname)

    for k_type, v_filename in download_filelist.iteritems():
        if os.path.isfile(dirname + v_filename):
            _log('%s already has been downloaded.', dirname + v_filename)
        else:
            _log('%s downloading into %s' %
                 (v_filename, dirname + v_filename))

            url = hostname + v_filename
            response = urllib2.urlopen(url)

            meta = response.info()
            file_size = int(meta.getheaders('Content-Length')[0])

            _log('Downloading: %s byte: %s' % (v_filename, file_size))

            file_size_dl = 0
            block_sz = 4 * 8192

            with open(dirname + v_filename, 'wb') as f:
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


def load_test_data(dirname):
    test_dict = sio.loadmat(dirname + test_file_name)
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

    y_1hot_label = np.zeros((Y_test.shape[0], count_distinct_value))
    y_1hot_label[np.arange(Y_test.shape[0]), Y_test] = 1

    return (X_test, y_1hot_label)


def load_train_data(dirname):
    train_dict = sio.loadmat(dirname + train_file_name)
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

    y_1hot_label = np.zeros((Y_train.shape[0], count_distinct_value))
    y_1hot_label[np.arange(Y_train.shape[0]), Y_train] = 1

    return (X_train, y_1hot_label)


def main():
    dirname = 'SVHN_data/'
    # download_data('SVHN_data/')
    X_train, y_train = load_train_data(dirname)
    X_test, y_test = load_test_data(dirname)

    print(X_train.shape)
    print(y_train.shape)

    print(X_test.shape)
    print(y_test.shape)


if __name__ == '__main__':
    main()
