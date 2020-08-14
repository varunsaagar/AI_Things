import cv2

cap = cv2.VideoCapture("Resource/107048815_2695818544010275_5004185914975757751_n.mp4")

while True:
    success,img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
