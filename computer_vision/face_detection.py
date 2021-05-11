import cv2
vid = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier()
face_cascade.load('haarcascade_frontalface_default.xml')


if face_cascade is None:
    print('somthing is fishy')

while True:
    state,frame = vid.read()
    if not state:
        print('cant find any frame in video , exiting')
        break
    #face detection logic
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    print("faces",len("faces"))
    if len(faces) > 0:
        for x,y,w,h, in faces:
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)

    cv2.imshow("video",frame)
    key=cv2.waitKey(1)

    if key==ord('q'):
        break

vid.release()
cv2.destroyAllWindows() 