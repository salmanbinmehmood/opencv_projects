import cv2
img=cv2.imread('D:\\SALMAN\\spyder\\superman.jpg')

img=cv2.resize(img,(800,800))
brdr=cv2.copyMakeBorder(img,15,15,10,10,
                        cv2.BORDER_CONSTANT,value=[251,0,12])

cv2.imshow('brdr',brdr)
cv2.waitKey(0)
cv2.destroyAllWindows()