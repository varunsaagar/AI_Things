import cv2
import numpy as np

img = cv2.imread("Open_CV/Resource/IMG_20200328_054229_553.jpg")

imgHor = np.hstack((img,img ))

imgVer = np.vstack((img,img))

cv2.imshow("OutH" , imgHor )
cv2.imshow("OutV" , imgVer )

cv2.waitKey(0)