import cv2
import numpy as np

frameWidth = 640
frameHeight= 480

cap = cv2.VideoCapture("http://192.168.1.106:4747/video")
# cap = cv2.VideoCapture(0)
cap.set(5,frameWidth)
cap.set(6,frameHeight)
cap.set(10,150)

myColors= [[5,107,0,19,255,255],
            [133,56,0,159,156,255],
            [57,76,0,100,255,255],
            [90,48,0,118,255,255]]

myColourValues = [[21,153,253],   #BGR
             [255,0,255],
             [0,255,0],
                  [255,0,0]]

myPoints = [] #[ x,y, colourID ]

def findColour(img, myColours,myColourValues ):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints= []
    for colour in myColours:
        lower = np.array(colour[0:3])
        upper = np.array(colour [3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y = getContours(mask)
        cv2.circle(imgResult , (x,y) , 15 , myColourValues[count] , cv2.CHAIN_APPROX_NONE)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count +=1
        #cv2.imshow(str(colour[0]), mask)
    return newPoints

def getContours(img):
    contours , hierarchy =cv2.findContours(img , cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #print(area)
        if area > 500:
            cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt , True )
            #print(peri)
            approx = cv2.approxPolyDP(cnt , 0.02 * peri , True)
            # print(len(approx))
            # objCor = len(approx)
            x , y , w , h = cv2.boundingRect(approx)
    return x+w // 2 , y
def drawOnCanvas(myPoints , myColorValues) :
    for point in myPoints:
        cv2.circle(imgResult , (point[0] , point[1]) , 10 , myColourValues[point[2]] , cv2.FILLED)

while True:
    success,img = cap.read()
    #img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    imgResult = img.copy()
    newPoints = findColour(img,myColors , myColourValues)
    if len(newPoints)!=0:
        for newP in newPoints :
            myPoints.append(newP)

    if len(myPoints) !=0:
        drawOnCanvas(myPoints , myColourValues)


    #img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imshow("Video",imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break