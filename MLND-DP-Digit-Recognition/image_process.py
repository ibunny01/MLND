import os.path

import cv2
import numpy as np
from matplotlib import pyplot as plt

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

    def __postProcess(self,
                      frame,
                      toGray=False,
                      toShape=[64., 64.],
                      rects=list(),
                      updateRects=False):

        drawRectangle = False

        # Convert color image to grayscale
        h_sf = toShape[0] / frame.shape[0]
        w_sf = toShape[1] / frame.shape[1]
        frame_scaled = cv2.resize(
            frame, None, fx=w_sf, fy=h_sf, interpolation=cv2.INTER_CUBIC)

        for r in rects:

            for k, v in r.items():
                r[k] = int(v)

            if drawRectangle:
                p1 = tuple(int(p) for p in (r['left'] * w_sf, r['top'] * h_sf, ))
                p2 = tuple(
                    int(p)
                    for p in (p1[0] + r['width'] * w_sf, p1[1] + r['height'] * h_sf))

                line_rgb = (255, 0, 0)
                line_type = 1
                cv2.rectangle(frame_scaled, p1, p2, line_rgb, line_type)

            if updateRects:
                idx = rects.index(r)
                rects[idx]['left'] *= w_sf
                rects[idx]['top'] *= h_sf
                rects[idx]['width'] *= w_sf
                rects[idx]['height'] *= h_sf

        if toGray:
            frame_scaled = cv2.cvtColor(frame_scaled, cv2.COLOR_BGR2GRAY)
            frame_scaled = frame_scaled * 1.0/255.0

        if False:
            cv2.imshow('frame', frame_scaled)
            cv2.waitKey(0)

        return frame_scaled

    def processVideo(self, toGray=False, toShape=[64., 64.], rects=list(), updateRects=False):

        # Load an color image
        ret, frame = self.cap.read()
        ret = self.__postProcess(frame, toGray, toShape, rects, updateRects)

        return ret

    def processImage(self,
                     fname,
                     toGray=False,
                     toShape=[64., 64.],
                     rects=list(),
                     updateRects=False):

        _log("%s is loading..." % fname)
        # Load an color image
        img = cv2.imread(fname, 1)
        ret = self.__postProcess(img, toGray, toShape, rects, updateRects)

        return ret


def main():
    ip = ImageProcess()
    # ip.captureVideo()
    img = ip.processImage(
        os.path.join('./KR_data/', 'IMG_20170315_201204260.jpg'), toGray=True)

    plt.imshow(img, interpolation='nearest', cmap='Greys')
    plt.show()
    print(img.shape)


if __name__ == '__main__':
    main()
