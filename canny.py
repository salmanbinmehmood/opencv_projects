import numpy as np
import cv2
from  matplotlib import pyplot as plt

def nothing(x):
    pass

img1=cv2.imread(r'D:\SALMAN\pythonProject\computer_vision\biulding.jpg')
img1=cv2.resize(img1,(600,600))

img_gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
cv2.namedWindow('canny adjustment')

cv2.createTrackbar('threshold','canny adjustment',0,255,nothing)
while True:
    lower_threashold=cv2.getTrackbarPos('threshold','canny adjustment')

    canny=cv2.Canny(img_gray,lower_threashold,255)
    cv2.imshow('img',img1)
    cv2.imshow('gray img',img_gray)
    cv2.imshow('canny',canny)
    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()