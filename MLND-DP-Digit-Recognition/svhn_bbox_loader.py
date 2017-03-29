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

from image_process import ImageProcess
from six.moves import cPickle as pickle
from six.moves import range
from six.moves.urllib.request import urlretrieve
from svhn_dataextract_tojson import DigitStructFile

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

    training_data = None
    testing_data = None

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

        count_distinct_value = max(
            len(np.unique(original)), decimal_kind_of_digit)
        label_1hot = np.zeros((original.shape[0], count_distinct_value))
        label_1hot[np.arange(original.shape[0]), np.transpose(original)] = 1

        return label_1hot

    @staticmethod
    def onehot_to_label(encoded):
        return np.array([np.where(e == 1)[0]
                         for e in np.rollaxis(encoded, 0)]).reshape([-1])

    def init_data(self):
        raise NotImplementedError('Should have implemented this')

    def generate_mixed_digit_data(self,
                                  numbers,
                                  scale=1,
                                  max_length=6,
                                  dims=(64, 64)):
        raise NotImplementedError('Should have implemented this')

    def get_data(self, dataset="training"):
        if not self.training_data or not self.testing_data:
            raise AssertionError('MNIST dataset may be initialized.')

        if dataset == "training":
            return self.training_data
        else:
            return self.testing_data


class SVHNBboxLoader(Loader):
    def __init__(self):

        self.pickle_prefix = 'svhn_bbox_full'
        self.dest_folder = 'SVHN_bbox_data/'
        self.base_url = 'http://ufldl.stanford.edu/housenumbers/'

        self.image_width = 32
        self.image_height = 32
        self.image_channel = 3

    def init_data(self):
        if self.training_data or self.testing_data:
            raise AssertionError('svhn dataset may be initialized.')

        if not os.path.exists(
                os.path.join(self.dest_folder,
                             "svhn_bbox_training_all.pickle")):
            self.training_data = self.load_data(dataset="training")
            Loader.saveAsPickle(self.training_data,
                                os.path.join(self.dest_folder,
                                             "svhn_bbox_training_all.pickle"))

        if not os.path.exists(
                os.path.join(self.dest_folder,
                             "svhn_bbox_testing_all.pickle")):
            self.testing_data = self.load_data(dataset="testing")
            Loader.saveAsPickle(self.testing_data,
                                os.path.join(self.dest_folder,
                                             "svhn_bbox_testing_all.pickle"))

        self.training_data = Loader.loadPickle(
            os.path.join(self.dest_folder, "svhn_bbox_training_all.pickle"))

        self.testing_data = Loader.loadPickle(
            os.path.join(self.dest_folder, "svhn_bbox_testing_all.pickle"))

    def download_data(self):
        train_images = Loader.maybe_download(self.base_url, self.dest_folder,
                                             'train.tar.gz', 404141560)
        test_images = Loader.maybe_download(self.base_url, self.dest_folder,
                                            'test.tar.gz', 276555967)
        extra_images = Loader.maybe_download(self.base_url, self.dest_folder,
                                             'extra.tar.gz', 1955489752)

    def load_data(self, dataset='training', digits=None):
        """
        return :
        (images, labels, labels_1hot)
        """
        files = {'training': 'digitStruct.mat', 'testing': 'digitStruct.mat'}

        dir_prefix = {
            'training': 'train/',
            'testing': 'test/',
        }

        try:
            data_fname = os.path.join(self.dest_folder,
                                      dir_prefix[dataset] + files[dataset])
        except KeyError:
            raise ValueError("Data set must be 'testing' or 'training'")

        ret_images = []
        ret_labels = []
        ret_bboxes_cnt = []
        ret_bboxes_pt = []
        ret_fname = []

        ip = ImageProcess()
        dsf = DigitStructFile(data_fname)
        digit_structs = dsf.getAllDigitStructure_ByDigit()

        for ds in digit_structs:
            fname = os.path.join(self.dest_folder,
                                 dir_prefix[dataset] + ds['filename'])

            image = np.array(
                ip.processImage(
                    fname, toGray=True, rects=ds['boxes'], updateRects=True))

            bboxes_cnt = len(ds['boxes'])
            bboxes_pt = np.zeros([24], dtype=np.int32)
            label = np.zeros([6], dtype=np.int32)

            for i, bbox in enumerate(ds['boxes']):
                label[i] = bbox['label']

                bboxes_pt[4 * i:4 * i + 4] = [
                    bbox['left'],
                    bbox['top'],
                    bbox['left'] + bbox['width'],
                    bbox['top'] + bbox['height'],
                ]

            ret_images.append(image)
            ret_labels.append(label)
            ret_bboxes_cnt.append(bboxes_cnt)
            ret_bboxes_pt.append(bboxes_pt)
            ret_fname.append(fname)

            # img = np.array(ip.processImage(fname, toGray=True, rects=feat))
            # plt.imshow(img, interpolation='nearest', cmap='Greys')
            # plt.show()

        return {
            'images': ret_images,
            'labels': ret_labels,
            'bboxes_cnt': ret_bboxes_cnt,
            'bboxes_pt': ret_bboxes_pt,
            'fname': ret_fname,
        }

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


def testcase_for_loader():
    svhn_bbox_full_loader = SVHNBboxLoader()
    svhn_bbox_full_loader.download_data()
    # svhn_bbox_full_loader.load_data(dataset='training')
    svhn_bbox_full_loader.init_data()
    train_set = svhn_bbox_full_loader.get_data(dataset='training')

    plt.imshow(train_set['images'][1], interpolation='nearest', cmap='Greys')
    plt.tight_layout
    plt.show()


def main():
    testcase_for_loader()


if __name__ == '__main__':
    main()
