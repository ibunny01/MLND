import os.path

import numpy as np
from matplotlib import pyplot as plt

import cv2

_DEBUG = True


def _log(message):
    if _DEBUG:
        print(message)


class ImageProcess(object):

    cap = None

    def __init__(self):
        self.cap = cv2.VideoCapture(0)

        # change input frame buffer size to 640x480
        # http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
        self.cap.set(3, 640)
        self.cap.set(4, 480)

    def __destroy__(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def processVideo(self, toGray=False, toShape=[64., 64.]):
        ret, frame = self.cap.read()

        if toGray:
            frame = cv2.cvtColor(frame,
                                cv2.COLOR_BGR2GRAY)

        h_sf = toShape[0] / img.shape[0]
        w_sf = toShape[1] / img.shape[1]
        frame_rescaled = cv2.resize(frame,
                                   None,
                                   fx=w_sf,
                                   fy=h_sf,
                                   interpolation=cv2.INTER_CUBIC)

        if False:
            cv2.imshow('frame',
                       frame_rescaled)

            cv2.waitKey(0)

        return frame_rescaled


    def processImage(self, fname, toGray=False, toShape = [64., 64.]):

        _log("%s is loading..." % fname)
        # Load an color image
        img = cv2.imread(fname, 1)

        # Convert color image to grayscale
        if toGray:
            img = cv2.cvtColor(img,
                                cv2.COLOR_BGR2GRAY)

        h_sf = toShape[0] / img.shape[0]
        w_sf = toShape[1] / img.shape[1]
        img_scaled = cv2.resize(img,
                                 None,
                                 fx=w_sf,
                                 fy=h_sf,
                                 interpolation=cv2.INTER_CUBIC)

        if False:
            cv2.imshow('frame',
                       img_scaled)

            cv2.waitKey(0)

        return img_scaled


def main():
    ip = ImageProcess()
    # ip.captureVideo()
    img = ip.processImage(os.path.join('./KR_data/','IMG_20170315_201204260.jpg'), toGray=True)

    plt.imshow(img, interpolation='nearest', cmap='Greys')
    plt.show()
    print(img.shape)


if __name__ == '__main__':
    main()
