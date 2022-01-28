# import numpy as np
# import cv2
# from  matplotlib import pyplot as plt
# # erosion
# img1=cv2.imread(r'D:\SALMAN\pythonProject\computer_vision\multi_balls.jpg',0)
# img1=cv2.resize(img1,(500,400))
# _,mask=cv2.threshold(img1,230,255,cv2.THRESH_BINARY_INV)
# kernal=np.ones((5,5),np.uint8)
# e=cv2.erode(mask,kernal)
# cv2.imshow('img1',img1)
# cv2.imshow('mask',mask)
# cv2.imshow('e',e)
#
# # dilation
# kernal=np.ones((3,3),np.uint8)
# d=cv2.dilate(mask,kernal)
# cv2.imshow('d',d)
#
#
# titles=['image1','mask','erosion','dilation']
# images=[img1,mask,e,d]
#
# for i in range(len(images)):
#     plt.subplot(2,2,i+1)
#     plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()
# cv2.waitKey()
# cv2.destroyAllWindows()



######## morpho;ogical another operations


import numpy as np
import cv2
from  matplotlib import pyplot as plt

img1=cv2.imread(r'D:\SALMAN\pythonProject\computer_vision\girl13.jpg',0)
img1=cv2.resize(img1,(300,300))
_,mask=cv2.threshold(img1,230,255,cv2.THRESH_BINARY_INV)
kernal=np.ones((2,2),np.uint8)
e=cv2.erode(mask,kernal)
d=cv2.dilate(mask,kernal)

op=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)
cl=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)
tph=cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernal)
gr=cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal)
blh=cv2.morphologyEx(mask,cv2.MORPH_BLACKHAT,kernal)

cv2.imshow('img1',img1)
cv2.imshow('mask',mask)
cv2.imshow('e',e)
cv2.imshow('d',d)
cv2.imshow('opening',op)
cv2.imshow('closing',cl)
cv2.imshow('tophat',tph)
cv2.imshow('grediant',gr)
cv2.imshow('blackhat',blh)


titles=['image1','mask','erosion','dilation','opening','closing','tophaat','grediand','blackhat']
images=[img1,mask,e,d,op,cl,tph,gr,blh]

for i in range(len(images)):
    plt.subplot(3,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()