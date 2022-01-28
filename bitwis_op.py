import cv2
import numpy as np

img1=np.zeros((250,500,3),np.uint8)
img1=cv2.rectangle(img1,(100,150),(200,250),(255, 255, 255),-1)


img2=np.zeros((250,500,3),np.uint8)
img2=cv2.rectangle(img2,(150,100),(200,300),(255, 255, 255),-1)
cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
# bit_and=cv2.bitwise_and(img1,img2)
# cv2.imshow('bt_and',bit_and)


# bit_or=cv2.bitwise_or(img1,img2)
# cv2.imshow('bt_and',bit_or)

# bit_not=cv2.bitwise_not(img1)
# cv2.imshow('bt_not',bit_not)
# bit_not2=cv2.bitwise_not(img2)
# cv2.imshow('bt_not2',bit_not2)


bit_xor=cv2.bitwise_xor(img1,img2)
cv2.imshow('bt_xor',bit_xor)
cv2.waitKey(0)
cv2.destroyAllWindows()



