import cv2
import numpy as np

img = cv2.imread("Resources/lena.jpg")
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(imgGray,100,200)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
cv2.imshow("Output",imgGray)
# cv2.waitKey(0)

cv2.imshow("Blurr_Output",imgBlur)
cv2.imshow("Canny Output",imgCanny)
cv2.imshow("Dialation Output",imgDialation)
cv2.imshow("Eroded Output",imgEroded)
cv2.waitKey(0)