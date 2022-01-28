import numpy as np
import cv2
img1=cv2.imread(r'D:\SALMAN\pythonProject\computer_vision\avengers.jpg')

img1=cv2.resize(img1,(700,700))


# pyramid_up=cv2.pyrUp(img1)
# pyramid_up2=cv2.pyrUp(pyramid_up)
# pyramid_down=cv2.pyrDown(pyramid_up2)
# cv2.imshow('img',img1)
# cv2.imshow('pyramid_up',pyramid_up)
# cv2.imshow('pyramid_up2',pyramid_up2)
# cv2.imshow('pyramid_down',pyramid_down)
#

# using forloop
# images=[img2]
img2=img1.copy()
for i in range(3):
    img2= cv2.pyrDown( img2)

    # images.append(img2)

    cv2.imshow('pyramid_down'+str(i), img2)

cv2.waitKey()
cv2.destroyAllWindows()