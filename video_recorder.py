import cv2 as cv
import os

cap = cv.VideoCapture(0)

codec = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('video_recording.avi',codec, 24.0,(640,480))
print('starting recording')
while True:
    ret, frame = cap.read()
    if not ret:
        print('camera not working')
        break
    out.write(frame)
    cv.imshow('Recording...',frame)
    if cv.waitKey(1) == ord('q'):
        print('stopping recording')
        break
cap.release()
out.release()
cv.destroyAllWindows()
