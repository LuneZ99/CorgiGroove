import cv2
import numpy as np
import serial
import serial.tools.list_ports
'''
port_list = list(serial.tools.list_ports.comports())
print(port_list)

print(1)

a = bytes([0, 1, 0])
print(a)
'''
# img = cv2.imread('pic/VoV.jpg', 0)
img = cv2.imread('', 0)
# ret, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# arr = np.array(img).flatten()
# s = ''.join(str(x//255) for x in arr)
# print(s)


START = 0xAA
TYPE = 0x01
