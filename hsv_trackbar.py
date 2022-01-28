#
# import cv2
# import numpy as np
#
# img=cv2.imread(r'D:\SALMAN\pythonProject\computer_vision\balls.jpg')
# img=cv2.resize(img,(600,400))
# cv2.namedWindow('color adjustment')
# def nothing(x):
#     pass
# cv2.createTrackbar('lower_h','color adjustment',0,255,nothing)
# cv2.createTrackbar('lower_s','color adjustment',0,255,nothing)
# cv2.createTrackbar('lower_v','color adjustment',0,255,nothing)
#
# cv2.createTrackbar('upper_h','color adjustment',255,255,nothing)
# cv2.createTrackbar('upper_s','color adjustment',255,255,nothing)
# cv2.createTrackbar('upper_v','color adjustment',255,255,nothing)
# while True:
#     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     l_h= cv2.getTrackbarPos('lower_h', 'color adjustment')
#     l_s= cv2.getTrackbarPos('lower_s', 'color adjustment')
#     l_v= cv2.getTrackbarPos('lower_v', 'color adjustment')
#
#
#
#     u_h= cv2.getTrackbarPos('upper_h', 'color adjustment')
#     u_s= cv2.getTrackbarPos('upper_s', 'color adjustment')
#     u_v= cv2.getTrackbarPos('upper_v', 'color adjustment')
#
#
#     lower_bound=np.array([l_h, l_s, l_v])
#     upper_bound=np.array([u_h, u_s, u_v])
#     mask=cv2.inRange(hsv,lower_bound,upper_bound)
#     res=cv2.bitwise_and(img,img,mask=mask)
#     cv2.imshow('img',img)
#     cv2.imshow('mask',mask)
#     cv2.imshow('res',res)
#     k=cv2.waitKey(1)
#     if k==27:
#         break
#
# cv2.destroyAllWindows()




####################### using camera




import cv2
import numpy as np

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
while True:
    _,frame=cap.read()
    img = cv2.resize(frame, (400, 400))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    l_h= cv2.getTrackbarPos('lower_h', 'color adjustment')
    l_s= cv2.getTrackbarPos('lower_s', 'color adjustment')
    l_v= cv2.getTrackbarPos('lower_v', 'color adjustment')



    u_h= cv2.getTrackbarPos('upper_h', 'color adjustment')
    u_s= cv2.getTrackbarPos('upper_s', 'color adjustment')
    u_v= cv2.getTrackbarPos('upper_v', 'color adjustment')


    lower_bound=np.array([l_h, l_s, l_v])
    upper_bound=np.array([u_h, u_s, u_v])
    mask=cv2.inRange(hsv,lower_bound,upper_bound)
    res=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow('img',img)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k=cv2.waitKey(1)
    if k==27:
        break

cv2.destroyAllWindows()
