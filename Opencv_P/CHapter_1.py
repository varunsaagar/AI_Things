import cv2
print("package Imported")

img = cv2.imread("Open_CV/Resource/IMG_20200328_054229_553.jpg")

cv2.imshow("Output",img)

cv2.waitKey(5000)