import numpy as np

import cv2

img1=cv2.imread(r'D:\SALMAN\pythonProject\computer_vision\hand.jpg')

img1=cv2.resize(img1,(600,700))

img_gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
blur=cv2.medianBlur(img_gray,9)
ret,threashold=cv2.threshold(blur,250,255,cv2.THRESH_BINARY_INV)
# find continous contours points

cnts,hier=cv2.findContours(threashold,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# img1=cv2.drawContours(img1,cnts,-1,(10,20,100),4)


area_list=[]
for c in cnts:
    # calculate thr center point of contours
    # m=cv2.moments(c)
    # cx=int(m['m10']/ m['m00'])
    # cy=int(m['m01']/ m['m00'])

    # cv2.circle(img1,(cx,cy),7,(255,255,255),-1)
    # cv2.putText(img1, 'center', (cx-20, cy-20), cv2.FONT_ITALIC, 0.5,
    #             (0, 87, 211), 2)
    # calculate thr contours area
    area=cv2.contourArea(c)
    area_list.append(area)
    # if area >10000:

    # approx - it is use to approx shape with less number of vertices
    esp=0.0001*cv2.arcLength(c,True)
    data=cv2.approxPolyDP(c,esp,True)

    hull=cv2.convexHull(data)
    cv2.drawContours(img1, [c], -1, (10, 20, 100), 2)
    cv2.drawContours(img1, [hull], -1, (100, 120, 180), 2)

# convexity defect
# this line returns actual cordinnates from contours
'''
hull2=cv2.convexHull(cnts[0],returnPoints=False)
defect=cv2.convexityDefects(cnts[0],hull2)
for i in range(defect.shape[0]):
    s,e,f,a=defect[i,0]
    start_point = tuple(c[s][0])
    ending_point=tuple(c[e][0])
    farthest_point=tuple(c[f][0])
    # app_point=tuple(c[a][0])
    cv2.circle(img1,farthest_point,5,[100,12,20],-1)
    
'''

# extreme points
# it gives topmost,botmost,leftmost, rightmost points of object.

c_max=max(cnts,key=cv2.contourArea)
# determine the extreme points from contours
ex_left=tuple(c_max[c_max[:,:,0].argmin()][0])
ex_right=tuple(c_max[c_max[:,:,0].argmax()][0])

ex_top=tuple(c_max[c_max[:,:,1].argmin()][0])
ex_bot=tuple(c_max[c_max[:,:,1].argmax()][0])

# print('cmax',tuple(c_max[c_max[:,:,0].argmin()][0]))
cv2.circle(img1,ex_left,8,[255,12,255],-1) #pink
cv2.circle(img1,ex_right,8,[0,0,200],-1) # red
cv2.circle(img1,ex_top,8,[120,12,0],-1) # blue
cv2.circle(img1,ex_bot,8,[10,120,20],-1) # green


cv2.imshow('img',img1)

cv2.imshow('img_dray',img_gray)

cv2.imshow('threashold',threashold)

cv2.waitKey()
cv2.destroyAllWindows()