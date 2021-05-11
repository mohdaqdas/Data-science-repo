import cv2 

vid = cv2.VideoCapture(0)

while True:
    state,frame = vid.read()
    if not state:
        print('cant find any frame in video, exiting')
        break
    cv2.imshow("video",frame)
    if cv2.waitKey(1) == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()