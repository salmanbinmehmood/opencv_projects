import cv2
img=cv2.imread('D:\\SALMAN\\spyder\\superman.jpg')
img2=cv2.imread('D:\\SALMAN\\spyder\\irpnman.jpg')
img=cv2.resize(img,(800,800))
img2=cv2.resize(img2,(800,800))
# (323,8) (471,292)
# [(y1:y2,x1:x2)]
roi=img[8:292,323:471]
# img[22:269,481:601]=roi
# img[22:269,602:722]=roi

# img[22:269,239:359]=roi
# img[22:269,119:239]=roi
# changing y
# 253  12  403 320
# img[300:547,60:180]=roi
img2[16:300,251:399]=roi
cv2.imshow('im',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()