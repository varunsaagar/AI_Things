import cv2
import numpy as np

img = cv2.imread("Open_CV/Resource/cards.jpg")


width,heigth= 250,350


pts1 = np.float32([[111,219] , [287 , 188],[154,482] , [352,440]] )
pts2 = np.float32([[0,0],[width ,0],[0,heigth],[width ,heigth]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img , matrix , (width , heigth))

cv2.imshow("image" , img)
cv2.imshow("output" , imgOutput)

cv2.waitKey(0)