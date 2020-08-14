import cv2

cap = cv2.VideoCapture("http://192.168.1.102:4747/video")
cap.set(3,640)
cap.set(4,480)

while True:
    success,img = cap.read()
    img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break