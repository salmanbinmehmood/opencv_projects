import cv2
img=cv2.imread('D:\\SALMAN\\spyder\\thor2.jpg')
img2=cv2.imread('D:\\SALMAN\\spyder\\thor3.jpg')
img=cv2.resize(img,(500,700))
img2=cv2.resize(img2,(500,700))

cv2.imshow('img1',img)
cv2.imshow('img2',img2)
# result=cv2.add(img,img2)
result=cv2.addWeighted(img,0.5,img2,0.5,0)
cv2.imshow('rst',result)
cv2.waitKey(0)
cv2.destroyAllWindows()