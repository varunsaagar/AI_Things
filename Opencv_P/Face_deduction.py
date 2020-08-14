import cv2

faceCascade = cv2.CascadeClassifier("Resource/haarcascade_frontalface_default.xml")
img = cv2.imread("Open_CV/Resource/IMG_20200328_054229_553.jpg")
imgGray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1 , 4)

for (x,y,w,h) in faces:
    cv2.rectangle(img , (x,y) , (x+w , y+h) ,(255,0,0) , 2 )

cv2.imshow("Out",img)
cv2.waitKey(0)