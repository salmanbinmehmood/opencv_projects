import cv2
import numpy as np
# img=cv2.imread('D:\\SALMAN\\spyder\\venom.jpg')

# img=np.zeros([515,600,3],np.uint8)*255
img=np.ones([515,600,3],np.uint8)*255
# img=cv2.resize(img,(700,700))
img=cv2.line(img,(0,0),(200,200),(125, 44, 21),5)
img=cv2.arrowedLine(img,(0,120),(250,300),(125, 44, 21),5)
img=cv2.rectangle(img,(300,0),(400,120),(125, 44, 21),5)
#img=cv2.circle(img,(200,300),65,(125, 44, 21),-5)
font=cv2.FONT_HERSHEY_DUPLEX
img=cv2.putText(img,'Venom',(200,300),font,4,
                (0,87,211),10,cv2.LINE_AA)
img=cv2.ellipse(img,(300,400),(100,50),0,0,270,150,5)
cv2.imshow('res',img)
cv2.waitKeyEx(0)
cv2.destroyAllWindows()