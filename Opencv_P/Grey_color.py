import cv2
import numpy as np

img = cv2.imread("Open_CV/Resource/IMG_20200328_054229_553.jpg")
kernel = np.ones((5,5) , np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray , (7,7) , sigmaX= 0 )
imgCanny = cv2.Canny(img , 150 , 200)
imgDialation =  cv2.dilate(imgCanny , kernel , iterations= 1 )
imgEroded = cv2.erode(imgDialation , kernel , iterations= 1)

cv2.imshow("out" , imgGray)
cv2.imshow("BLur" , imgBlur)
cv2.imshow("Canny" , imgCanny)
cv2.imshow("Dilation" , imgDialation)
cv2.imshow("Erode",imgEroded)
cv2.waitKey(0)