import cv2
import numpy as np


img =np.zeros((512,512,3) , np.uint8)
#print(img)
#img[200:300 , 300:500] = 255,255,250
#cv2.line(img,(0,0) , (300,300) , (0,255,0) ,  3)
cv2.line(img,(0,0) , (img.shape[1],img.shape[0]) , (0,255,0) ,  5)
cv2.rectangle(img,(0,0) , (230,350) , (0,0,255) ,  2)
#cv2.rectangle(img,(0,0) , (230,350) , (0,0,255)  , cv2.FILLED)
cv2.circle(img,(400,250) , 100 , (250,0,255) , 7 )
cv2.putText(img , "Varun" , (150 , 200) , cv2.FONT_ITALIC ,2, (240 , 158 , 215) , 3 )

cv2.imshow("out" , img)

cv2.waitKey(0)