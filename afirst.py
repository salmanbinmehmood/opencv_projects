import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
print('cap', cap)
fourcc=cv2.VideoWriter_fourcc(*"XVID")
output=cv2.VideoWriter('output.avi',fourcc,21.0,(640,480))
while cap.isOpened:
    ret, frame = cap.read()
    if ret == True:

        cv2.imshow('rame', frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('gray', gray)
        output.write(frame)

        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
output.release()
cv2.destroyAllWindows()