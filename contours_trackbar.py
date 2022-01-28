import numpy as np

import cv2

cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)

cv2.namedWindow('color adjustment')
def nothing(x):
    pass
cv2.createTrackbar('lower_h','color adjustment',0,255,nothing)
cv2.createTrackbar('lower_s','color adjustment',0,255,nothing)
cv2.createTrackbar('lower_v','color adjustment',0,255,nothing)

cv2.createTrackbar('upper_h','color adjustment',255,255,nothing)
cv2.createTrackbar('upper_s','color adjustment',255,255,nothing)
cv2.createTrackbar('upper_v','color adjustment',255,255,nothing)
cv2.createTrackbar('thresh','color adjustment',0,255,nothing)

while True:
    _,frame=cap.read()
    img = cv2.resize(frame, (400, 400))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    l_h= cv2.getTrackbarPos('lower_h', 'color adjustment')
    l_s= cv2.getTrackbarPos('lower_s', 'color adjustment')
    l_v= cv2.getTrackbarPos('lower_v', 'color adjustment')
    u_h = cv2.getTrackbarPos('upper_h', 'color adjustment')
    u_s = cv2.getTrackbarPos('upper_s', 'color adjustment')
    u_v = cv2.getTrackbarPos('upper_v', 'color adjustment')

    lower_bound = np.array([l_h, l_s, l_v])
    upper_bound = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    filter = cv2.bitwise_and(img, img, mask=mask)
    mask_in=cv2.bitwise_not(mask)
    Th=cv2.getTrackbarPos('thresh', 'color adjustment')
    ret,thresh=cv2.threshold(mask_in,Th,255,cv2.THRESH_BINARY)
    dialate=cv2.dilate(thresh,(1,1),iterations=6)


# find continous contours points

    cnts, hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in cnts:
        esp = 0.0001 * cv2.arcLength(c, True)
        data = cv2.approxPolyDP(c, esp, True)

        hull = cv2.convexHull(data)
        cv2.drawContours(img, [c], -1, (10, 20, 100), 2)
        cv2.drawContours(img, [hull], -1, (100, 120, 180), 2)




    cv2.imshow('img==', img)
    cv2.imshow('thresh==',thresh )
    cv2.imshow('mask==',mask )
    cv2.imshow('filter==', filter)
    k = cv2.waitKey(1) & 0XFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()