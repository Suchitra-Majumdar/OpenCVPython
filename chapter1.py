import cv2
print("Package Imported")
# img = cv2.imread("Resources/lena.jpg")
# cv2.imshow("Output",img)
# cv2.waitKey(0)

# cap = cv2.VideoCapture("Resources/test_video.mp4")
# while True:
#     success,img=cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) &0xFF==ord('q'):
#         break

cap1 = cv2.VideoCapture(0)
cap1.set(3,640)
cap1.set(4,480)
cap1.set(10,200)
while True:
    success,img=cap1.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break