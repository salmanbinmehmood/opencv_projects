import cv2
import numpy as np

img=cv2.imread(r'D:\SALMAN\pythonProject\computer_vision\balls.jpg')
while True:
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    u_v=np.array([72, 250, 244])
    l_v=np.array([36, 130, 127])
    mask=cv2.inRange(hsv,l_v,u_v)
    res=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow('img',img)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k=cv2.waitKey(1)
    if k==27:
        break

cv2.destroyAllWindows()