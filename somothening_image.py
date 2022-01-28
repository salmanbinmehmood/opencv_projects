
import numpy as np
import cv2
from  matplotlib import pyplot as plt

img1=cv2.imread(r'D:\SALMAN\pythonProject\computer_vision\noisy.jpg')
# img1=cv2.resize(img1,(300,300))
kernal=np.ones((5,5),np.float32)/25
# hemogenius filtering

h_fil=cv2.filter2D(img1,-1,kernal)
# takes the all average of pixels and replace average of central average
blur=cv2.blur(img1,(5,5),)
# there are different weight
# there is small side values than center
gaus=cv2.GaussianBlur(img1,(5,5),0)
# this is highly effective  to remove salt-and-paper noise
# kernal must be odd value except one
med_bl=cv2.medianBlur(img1,5)

# this works like gaussian filter but more effective for edges
# this is low filtering method
# arguments(neighbour_pixel_diameter, sigma_color,sigma_space)
bi_l=cv2.bilateralFilter(img1,9,75,75)
cv2.imshow('img1',img1)
cv2.imshow('hemogenius',h_fil)
cv2.imshow('blur',blur)
cv2.imshow('gausian',gaus)
cv2.imshow('median blur',med_bl)
cv2.imshow('bilateralFilter',bi_l)


titles=['img','filter2D','blur','GaussianBlur','medianBlur','bilateralFilter']
images=[img1,h_fil,blur,gaus,med_bl,bi_l]

for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()