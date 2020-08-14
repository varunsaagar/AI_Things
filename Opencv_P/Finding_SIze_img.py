import cv2
import numpy as np

img = cv2.imread("Open_CV/Resource/IMG_20200328_054229_553.jpg")
print(img.shape)

imaResize = cv2.resize(img , (800,800))
print(imaResize.shape)

imgCropped = img[0:300,0:400]

cv2.imshow("out" , img)
#cv2.imshow("out2" , imaResize )
cv2.imshow("Croped" , imgCropped)

cv2.waitKey(0)