import cv2
import numpy as np
###########################

widthImg = 480
heigthImg = 640

###########################

cap = cv2.VideoCapture("http://192.168.1.104:4747/video")
#cap = cv2.VideoCapture(0)
cap.set(5,widthImg)
cap.set(6,heigthImg)
cap.set(10,150)

def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


def preProcessing(img) :
    imgGray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray , (5,5) , 1 )
    imgCanny = cv2.Canny(imgBlur , 200 , 200)
    kernel = np.ones((5,5))
    imgDail = cv2.dilate(imgCanny , kernel , iterations = 2)
    imgThres = cv2.erode(imgDail , kernel , iterations=1)

    return imgThres

def getContours(img):
    biggest = np.array([])
    maxArea = 0
    contours , hierarchy =cv2.findContours(img , cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 5000:
            #cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt , True )
            #print(peri)
            approx = cv2.approxPolyDP(cnt , 0.02 * peri , True)
            if area > maxArea and (approx) == 4:
                biggest = approx
                maxArea = area
    cv2.drawContours(imgContour, biggest, -1, (255, 0, 0), 20)
    return biggest


def reorder( myPoints):
    myPoints = myPoints.reshape((4,2))
    myPointsNew = np.zeros((4,1,2) , np.int32)
    add = myPoints.sum(1)

    myPointsNew[0] =  myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    #print("NewPoints" , myPointsNew)
    diff = np.diff(myPoints , axis = 1)
    myPointsNew[1] = myPoints[np.argmin(add)]
    myPointsNew[2] = myPoints[np.argmax(add)]
    return myPointsNew

def getWrap(img , biggest):
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [widthImg, 0], [0, heigthImg], [widthImg, heigthImg]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (widthImg, heigthImg))

    imgCropped = imgOutput[20:imgOutput.shape[0] - 20 , 20:imgOutput[1] - 20]
    imgCropped  = cv2.resize(imgCropped , (widthImg , heigthImg))

    return imgCropped


while True:
    success,img = cap.read()
    img= cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    imgContour = img.copy()
    img = cv2.resize(img , (widthImg , heigthImg))
    imgThres = preProcessing(img)
    biggest = getContours(imgThres)
    if biggest.size !=0 :

        imgWraped =getWrap(img , biggest)

        imageArray = ([img ,imgThres ] ,
                  [imgContour , imgWraped])
    else:
        imageArray = ([img ,imgThres ] ,
                  [img , img])


    stackedImages = stackImages ( 0.6 , imageArray)

    cv2.imshow("WorkFLow",stackedImages)
    cv2.imshow("ImgWrapped", imgWraped)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break