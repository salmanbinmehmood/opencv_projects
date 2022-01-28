# import numpy as np
# import cv2
#
# img=cv2.imread(r'D:\SALMAN\pythonProject\computer_vision\black_white.jpg',0)
#
# img=cv2.resize(img,(300,300))
#
# cv2.imshow('img',img)
#
# _,th1=cv2.threshold(img,50,255,cv2.THRESH_BINARY)
# cv2.imshow('th1',th1)
#
# _,th2=cv2.threshold(img,50,255,cv2.THRESH_BINARY_INV)
# cv2.imshow('th2',th2)
#
# _,th3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
# cv2.imshow('th3',th3)
#
# _,th4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
# cv2.imshow('th4',th4)
#
#
# _,th5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
# cv2.imshow('th5',th5)
# cv2.waitKey()
# cv2.destroyAllWindows()



####################### adaptive


import numpy as np
import cv2

img=cv2.imread(r'D:\SALMAN\pythonProject\computer_vision\suduko.png',0)

img=cv2.resize(img,(300,300))

cv2.imshow('img',img)

_,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow('th1',th1)

th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow('th2',th2)
cv2.imshow('th3',th3)
cv2.waitKey()
cv2.destroyAllWindows()