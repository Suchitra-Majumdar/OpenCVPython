import cv2
import numpy as np

# img = cv2.imread("Resources/lena.jpg")
img = cv2.imread("Resources/shapes.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),2)
imgCanny = cv2.Canny(imgBlur,50,50)
imgContour = img.copy()
ret,thresh= cv2.threshold(imgGray,200,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 500:
        cv2.drawContours(img,cnt,-1,(0,0,0),2)
        peri = cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,0.02*peri,True)#corner points
        print(len(approx))
        objCor = len(approx)
        x,y,w,h=cv2.boundingRect(approx)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        if objCor==3:
            ObjectType='Tri'
        elif objCor==4:
            ObjectType="Rect"
        elif objCor==5:
            ObjectType="Pent"
        elif objCor==6:
            ObjectType="Hex"
        else:
            ObjectType="Poly"
        cv2.putText(img,ObjectType,(x+(w//2)-10,y+(h//2)),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0),1)




cv2.imshow("Output",img)
cv2.imshow("Gray output",imgGray)
cv2.imshow("blurred Output",imgBlur)
cv2.imshow("Canny",imgCanny)
cv2.imshow("Contour image",imgContour)
cv2.waitKey(0)