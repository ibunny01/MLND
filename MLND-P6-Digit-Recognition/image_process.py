import os.path

import numpy as np

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

    def processVideo(self):
        while(True):
            ret, frame = self.cap.read()

            gray = cv2.cvtColor(frame,
                                cv2.COLOR_BGR2GRAY)

            h_sf = 64. / gray.shape[0]
            w_sf = 64. / gray.shape[1]
            gray_rescaled = cv2.resize(gray,
                                       None,
                                       fx=w_sf,
                                       fy=h_sf,
                                       interpolation=cv2.INTER_CUBIC)

            cv2.imshow('frame',
                       gray_rescaled)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def processImage(self, fname):

        _log("%s is loading..." % fname)
        # Load an color image
        img = cv2.imread(fname, 1)
        # Convert color image to grayscale
        gray = cv2.cvtColor(img,
                            cv2.COLOR_BGR2GRAY)

        h_sf = 64. / gray.shape[0]
        w_sf = 64. / gray.shape[1]
        gray_scaled = cv2.resize(gray,
                                 None,
                                 fx=w_sf,
                                 fy=h_sf,
                                 interpolation=cv2.INTER_CUBIC)

        cv2.imshow('frame',
                   gray_scaled)

        cv2.waitKey(0)


def main():
    ip = ImageProcess()
    # ip.captureVideo()
    ip.processImage(os.path.join('./KR_data/','IMG_20170315_201204260.jpg'))


if __name__ == '__main__':
    main()
