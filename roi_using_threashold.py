import numpy as np
import cv2

img1=cv2.imread(r'D:\SALMAN\pythonProject\computer_vision\thor.jpg')
img2=cv2.imread(r'D:\SALMAN\pythonProject\computer_vision\ironman3.jpg')

img1=cv2.resize(img1,(1050,650))
img2=cv2.resize(img2,(600,650))

# cv2.imshow('img1z+',img1)
# cv2.imshow('img2',img2)

r,c,ch=img2.shape
print(r,c,ch)
roi=img1[0:r,0:c]

img_gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

_,mask=cv2.threshold(img_gray,50,255,cv2.THRESH_BINARY)
mask_inv=cv2.bitwise_not(mask)
img1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
img2_fg=cv2.bitwise_and(img2,img2,mask=mask)
res=cv2.add(img2_fg,img1_bg)
final=img1

final[0:r,0:c]=res
#
# _,th1=cv2.threshold(img1,127,255,cv2.THRESH_BINARY)
# cv2.imshow('th1',th1)
#
# th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
# th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
# cv2.imshow('th2',th2)
# cv2.imshow('th3',th3)

cv2.imshow('img_gray -step1',img_gray)
cv2.imshow('mask -step2',mask)
cv2.imshow('mask_inv -step3',mask_inv)
cv2.imshow('mask_bg -step4',img1_bg)
cv2.imshow('mask_fg -step5',img2_fg)
cv2.imshow('res -step6',res)
cv2.imshow('final-result -step7',final)
cv2.waitKey()
cv2.destroyAllWindows()