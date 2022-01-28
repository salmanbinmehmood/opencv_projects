import cv2
import datetime
# capturing video
# cap = cv2.VideoCapture('D:\SALMAN\pythonProject\computer_vision\pirates.crdownload')
# capturing video from webcam
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
print('cap', cap)
print('width=',cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print('hiegth=',cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
while cap.isOpened:
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame, (700, 600))
        date_data=datetime.datetime.now()
        font = cv2.FONT_HERSHEY_DUPLEX
        text=f'Height {str(cap.get(4))} Width= {str(cap.get(3))} '

        frame = cv2.putText(frame, text, (0, 30), font, 1,
                          (0, 87, 211), 2, cv2.LINE_AA)
        text=f'dateTime {date_data}'
        frame = cv2.putText(frame, text, (0, 80), font, 1,
                            (15, 87, 211), 2, cv2.LINE_AA)
        cv2.imshow('rame', frame)
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('gray', gray)


        if cv2.waitKey(30) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
