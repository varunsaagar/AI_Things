import cv2
import numpy as np
###############################
frameWidth = 640
frameHeight= 480
nPlateCascade = cv2.CascadeClassifier("Resource/haarcascade_russian_plate_number.xml")
minArea= 500
color = (255 , 0 , 0)
count = 0
###############################
cap = cv2.VideoCapture("http://192.168.1.102:4747/video")
# cap = cv2.VideoCapture(0)
cap.set(5,frameWidth)
cap.set(6,frameHeight)
cap.set(10,150)

while True:
    success,img = cap.read()
    img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.CascadeClassifier("Resource/haarcascade_frontalface_default.xml")

    numberPlates  = nPlateCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in numberPlates:
        area = w* h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 250), 2)
            cv2.putText(img , "Number Plate" , (x,y-5) ,
                        cv2.FONT_HERSHEY_TRIPLEX ,1 ,color , 2 )
            imgROI = img[y :y+h , x :x+w]
            cv2.imshow("ROI" , imgROI)

    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("Resource/Chapter_1to10" + str(count)+".jpg" , imgROI )
        cv2.rectangle(img ,(0,200), ( 640 , 300) ,(0,255,0) , cv2.FILLED )
        cv2.putText( img , "scanSaved" , (150 , 265) , cv2.FONT_HERSHEY_COMPLEX , 2 ,
                     (0,0,255) , 2)
        cv2.imshow("Video", img)
        cv2.waitKey((500))
        count +=1
        break