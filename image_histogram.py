import numpy as np
import cv2
import matplotlib.pyplot as plt

# image histogram
# in this case all histogram helps for distributing data points
# x axis - contains the color values
# y axis - contains pixels values
# we use these methods to extract distortions,color intensity,pixels behaviour
'''
img=np.zeros((200,200),np.uint8)
# this method accepts data in list type
cv2.rectangle(img,(0,122),(200,200),(256),-1)
cv2.rectangle(img,(0,50),(50,100),(127),-1)
calhist=cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(calhist)
plt.show()
cv2.imshow('res',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
# colored image

# img=cv2.imread('ironman2.jpg')
# img=cv2.resize(img,(600,600))
# b,g,r=cv2.split(img)
# cv2.imshow('img',img)
# cv2.imshow('b',b)
# cv2.imshow('g',g)
# cv2.imshow('r',r)
# plt.hist(b.ravel(),256,[0,256])
# plt.hist(g.ravel(),256,[0,256])
# plt.hist(r.ravel(),256,[0,256])
# plt.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# grey scale
# img=cv2.imread('ironman2.jpg')
# img=cv2.resize(img,(600,600))
# grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# calhist=cv2.calcHist([grey_img],[0],None,[256],[0,256])
# plt.plot(calhist)
# plt.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# histogram equalization
#  this methods is good for when confined particular region are same by nearest pixels
# accepts gray scale image

# img=cv2.imread('ironman2.jpg')
# # img=cv2.resize(img,(600,600))
# grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# eql=cv2.equalizeHist(grey_img)
# compare=np.hstack((grey_img,eql))
# calhist=cv2.calcHist([eql],[0],None,[256],[0,256])
# plt.plot(calhist)
# plt.show()
# cv2.imshow('compare',compare)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# CLAHE contrast limited adaptive histogram equalization
# creating CLAHE object (argument is optional)
# this function is used to enhance image and remove noise from image
# gray scale image is required

img=cv2.imread('ironman2.jpg')
# img=cv2.resize(img,(600,600))
grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cl=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
cl=cl.apply(grey_img)
compare=np.hstack((grey_img,cl))
calhist=cv2.calcHist([cl],[0],None,[256],[0,256])
plt.plot(calhist)
plt.title('CLAHE')
plt.show()
cv2.imshow('compare',compare)
cv2.waitKey(0)
cv2.destroyAllWindows()

