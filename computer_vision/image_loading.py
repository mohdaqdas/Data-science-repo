import cv2

imp = cv2.imread('example.jpg')
if img is None:
    print("error file not found")
else:
    bwimg = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("output",imp)
    cv2.imshow("BW",bwing)
    print(img.shape)
    cv2.waikey(0)