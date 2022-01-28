import numpy as np

import cv2

img1=cv2.imread('shapes.png')

img1=cv2.resize(img1,(600,700))

img_gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

ret,threashold=cv2.threshold(img_gray,220,255,cv2.THRESH_BINARY_INV)
# find continous contours points
cnts,hier=cv2.findContours(threashold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# img1=cv2.drawContours(img1,cnts,-1,(10,20,100),4)

area_list=[]
for c in cnts:
    # calculate thr center point of contours
    m=cv2.moments(c)
    cx=int(m['m10']/ m['m00'])
    cy=int(m['m01']/ m['m00'])
    cv2.drawContours(img1, [c], -1, (10, 20, 100), 2)
    cv2.circle(img1,(cx,cy),7,(255,255,255),-1)
    cv2.putText(img1, 'center', (cx-20, cy-20), cv2.FONT_ITALIC, 0.5,
                (0, 87, 211), 2)
    # calculate thr contours area
    area=cv2.contourArea(c)
    area_list.append(area)
    if area >10000:

    # approx - it is use to approx shape with less number of vertices
        esp=0.01*cv2.arcLength(c,True)
        data=cv2.approxPolyDP(c,esp,True)
        # convex hull - it is used to provide proper convexity and bounding contours
        # this function analyze how much area covered by contours
        hull=cv2.convexHull(data)
        x,y,w,h=cv2.boundingRect(hull)
        cv2.rectangle(img1, (x, y), (x+w , y+h), (125, 44, 21), 5)

cv2.imshow('img',img1)

cv2.imshow('img_dray',img_gray)

cv2.imshow('threashold',threashold)

print(area_list)
cv2.waitKey()

cv2.destroyAllWindows()