import cv2
import struct
import numpy as np
import serial
import serial.tools.list_ports
import matplotlib.pyplot as plt

'''
todo
    减小import
    ……
'''

class TransTrunk:

    def __init__(self, wi=None, hi=None):
        if not (wi and hi):
            raise EOFError
        self.data = None
        self.width = wi
        self.height = hi
        self.byte_len = wi * hi // 8 + 1
        self.arr = np.zeros((wi, hi), dtype=np.uint8)

    def trans(self):
        return self.data

    def show(self):
        pass


class ImgTrans(TransTrunk):

    def __init__(self, im, wi=None, hi=None):
        super(ImgTrans, self).__init__(wi, hi)
        self.img = cv2.imread(im, 0) if isinstance(im, str) else im

    def trans_img(self, is_ratio=False):

        if self.width and self.height:
            # 等比例缩放
            if is_ratio:
                hr = self.height / self.img.shape[0]
                wr = self.width / self.img.shape[1]
                fr = min(hr, wr)
                self.img = cv2.resize(self.img,
                                      None, fx=fr, fy=fr,
                                      interpolation=cv2.INTER_AREA)
            # 拉伸缩放
            else:
                self.img = cv2.resize(self.img,
                                      (self.width, self.height),
                                      interpolation=cv2.INTER_AREA)
        else:
            print('\n未输入显示设备分辨率，可能造成显示错误！')

        ret, self.img = cv2.threshold(self.img,
                                      0, 255,
                                      cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        if is_ratio:
            self.img = cv2.copyMakeBorder(self.img,
                                          0, self.height - self.img.shape[0],
                                          0, self.width - self.img.shape[1],
                                          cv2.BORDER_CONSTANT, value=[255])
        self.arr = np.array(self.img) // 255
        return self.arr

    def trans(self):

        # self.arr = self.arr.resize(self.byte_len, 8)
        # self.arr = np.resize(self.arr, (self.byte_len, 8))
        return self.arr

    def len(self):
        return self.byte_len

    def show(self):
        cv2.imshow('Image', self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


class Signal:
    def __init__(self, data, byte_len=0):
        self.START = 0xAA
        self.TYPE = 0x01
        self.WIDTH = 0x00
        self.HEIGHT = 0x00
        self.DATA = data
        self.PARITY = 0xBB
        self.END = 0xEE

        self.LEN = byte_len

    def package(self):
        return struct.pack('7b', self.START, self.TYPE, self.WIDTH, self.HEIGHT,
                           self.DATA, self.PARITY, self.END)


img = ImgTrans('pic/VoV.jpg', 52, 33)
img.trans_img(True)
print('二进制数据：%s' % img.trans())
# p = Signal(img.data)
# print(p.package())
