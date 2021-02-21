import cv2
import numpy as np

img =np.zeros((512,512,3),np.uint8)
# print(img.shape)
# img[100:300,200:400]=255,0,0
# cv2.line(img,(0,0),(300,300),(0,255,0),5)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
cv2.rectangle(img,(100,100),(250,350),(0,0,255),2)
# cv2.rectangle(img,(100,100),(250,350),(0,0,255),cv2.FILLED)
cv2.circle(img,(200,100),100,(255,255,0),2)
cv2.putText(img,"OpenCV",(200,100),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,150,250),2)
cv2.imshow("image",img)
cv2.waitKey(0)