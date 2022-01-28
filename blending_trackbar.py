import cv2
import numpy as np
img1=cv2.imread('thor2.jpg')
img2=cv2.imread('thor3.jpg')
img1=cv2.resize(img1,(500,700))
img2=cv2.resize(img2,(500,700))
def blend(x):
    pass
img=np.zeros((400,400,3),np.uint8)
cv2.namedWindow('win')
cv2.createTrackbar('alpha','win',1,100,blend)
switch='0 : OFF \n 1 : ON'
cv2.createTrackbar(switch,'win',0,1,blend)

while True:
    a=cv2.getTrackbarPos('alpha','win')
    s=cv2.getTrackbarPos(switch,'win')
    n=float(a/100)
    print(n)
    if s==0:
        dst=img[:]
    else:
        dst=cv2.addWeighted(img1,1-n,img2,n,0)
        cv2.putText(dst, str(a), (20, 50),cv2.FONT_ITALIC, 2,
                    (0, 87, 211), 2)
    cv2.imshow('dst', dst)
    k=cv2.waitKey(1)& 0XFF
    if k==27:
        break


cv2.waitKey(0)
cv2.destroyAllWindows()