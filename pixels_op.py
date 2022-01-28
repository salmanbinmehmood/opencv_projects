import cv2
import numpy as np
img=cv2.imread('D:\\SALMAN\\spyder\\spacejam.jpg')
img=cv2.resize(img,(600,600))
# cv2.namedWindow('pixels')

# print('no of pixels',img.size)
# print('shape ',img.shape)
# print('datatype',img.dtype)
# print('type of image',type(img))
b,g,r=cv2.split(img)
# print(cv2.split(img))
mrg=cv2.merge((r,g,b))
mrg2=cv2.merge((r,b,g))
mrg3=cv2.merge((g,b,r))
cv2.imshow('original',img)
px=img[210,322]
blue=img[210,322,0]
green=img[210,322,1]
red=img[210,322,2]
print('the pixels of the coordinates',px)
print('the pixels having blue color',blue)
print('the pixels having green ',green)
print('the pixels having red color',red)
# cv2.imshow('rgb',mrg)
# cv2.imshow('rbg',mrg2)
# cv2.imshow('gbr',mrg3)
# cv2.imshow('blue',b)
# cv2.imshow('green',g)
# cv2.imshow('red',r)
cv2.waitKey(0)
cv2.destroyAllWindows()
