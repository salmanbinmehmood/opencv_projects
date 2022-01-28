# import cv2
# import numpy as np
#
# def draw(event,x,y,flags,param):
#     print('event',event)
#     print('x',x)
#     print('y',y)
#     print('flags',flags)
#     print('param',param)
#     if event==cv2.EVENT_LBUTTONDBLCLK:
#
#         cv2.rectangle(img,(x,y),(x+100,y+75),(125, 44, 21),5)
#
#     if event == cv2.EVENT_RBUTTONDBLCLK:
#
#         cv2.circle(img,(y,y),100,(125, 44, 21),-5)
# cv2.namedWindow(winname='res')
# img=np.zeros([515,600,3],np.uint8)
# cv2.setMouseCallback('res',draw)
#
#
# while True:
#     cv2.imshow('res',img)
#     if cv2.waitKey(1)==27:
#         break
#
# cv2.destroyAllWindows()



import cv2
import numpy as np

def mouse_events(event,x,y,flags,param):
    print('event',event)
    print('x',x)
    print('y',y)
    print('flags',flags)
    print('param',param)
    font=cv2.FONT_HERSHEY_DUPLEX


    if event==cv2.EVENT_RBUTTONDOWN:
        cord = f'{x},{y}'

        cv2.putText(img, cord, (x, y), font, 1,
                    (0, 87, 211), 2)

    if event == cv2.EVENT_LBUTTONDOWN:
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        color_bgr = '.'+str(b)+','+str(g)+','+str(r)
        cv2.putText(img, color_bgr, (x, y), font, 1,
                    (152, 255, 130), 2)
cv2.namedWindow(winname='res')
# img=np.zeros([515,512,3],np.uint8)
img=cv2.imread('venom.jpg')
cv2.setMouseCallback('res',mouse_events)


while True:
    cv2.imshow('res',img)
    if cv2.waitKey(1)==27:
        break

cv2.destroyAllWindows()