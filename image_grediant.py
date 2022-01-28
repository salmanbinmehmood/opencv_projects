import numpy as np
import cv2
from  matplotlib import pyplot as plt

img1=cv2.imread(r'D:\SALMAN\pythonProject\computer_vision\biulding.jpg')
img1=cv2.resize(img1,(300,300))
img_gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
lap=cv2.Laplacian(img_gray,cv2.CV_64F,ksize=3)
lap=np.uint8(np.absolute(lap))
sobelx=cv2.Sobel(img_gray,cv2.CV_64F,1,0,ksize=3)
sobely=cv2.Sobel(img_gray,cv2.CV_64F,0,1,ksize=3)
sobelx=np.uint8(np.absolute(sobelx))
sobely=np.uint8(np.absolute(sobely))
combine_sobel=cv2.bitwise_or(sobelx,sobely)
cv2.imshow('img1',img1)
cv2.imshow('gray',img_gray)
cv2.imshow('lap',lap)
cv2.imshow('sobalx',sobelx)
cv2.imshow('sobaly',sobely)
cv2.imshow('combo',combine_sobel)


titles=['img1','gray','lap','sobalx','sobaly','sobel combo']
images=[img1,img_gray,lap,sobelx,sobely,combine_sobel]

for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()