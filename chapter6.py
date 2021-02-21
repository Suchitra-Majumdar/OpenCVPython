import cv2
import numpy as np

img = cv2.imread("Resources/lena.jpg")
imgHor =  np.hstack((img,img))
imgVer = np.vstack((img,img))


# cv2.imshow("Horrizontal",imgHor)
# cv2.imshow("Vertical",imgVer)
# cv2.imshow("Stack Images",imgStack)
cv2.waitKey(0)