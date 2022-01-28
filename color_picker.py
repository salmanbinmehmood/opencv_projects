import cv2
import numpy as np
def cross(x):
    pass
cv2.namedWindow('color picker')
s0='0:OFF\n1:ON'
img=np.zeros([512,512,3],np.uint8)
cv2.createTrackbar(s0,'color picker',0,1,cross)
cv2.createTrackbar('R','color picker',0,255,cross)
cv2.createTrackbar('G','color picker',0,255,cross)
cv2.createTrackbar('B','color picker',0,255,cross)
while True:
    cv2.imshow('color picker',img)
    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break
    s1=cv2.getTrackbarPos(s0,'color picker')
    r=cv2.getTrackbarPos('R','color picker')
    g=cv2.getTrackbarPos('G','color picker')
    b=cv2.getTrackbarPos('B','color picker')
    if s1==0:
        img[:] =0
    else:
        img[:]=[r,g,b]

cv2.destroyAllWindows()