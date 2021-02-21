import cv2
import numpy as np

img = cv2.imread("Resources/lambo.jpg")
print(img.shape)
imgResize = cv2.resize(img,(250,300))
imgCropped = img[0:100,100:300]

print(imgResize.shape)
cv2.imshow("Output",img)
# cv2.imshow("Resize",imgResize)
cv2.imshow("Cropped",imgCropped)
cv2.waitKey(0)