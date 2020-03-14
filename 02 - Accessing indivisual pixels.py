import imutils
import cv2

#LOADING IMAGE INTO MEMORY
image = cv2.imread("jp.png")

#DISPLAY IMAGE ON THE SCREEN ["WINDOWS TITLE," SOURCE]
cv2.imshow("Image", image)

#PICK THE BGR VALUES AT X=50 Y=100
(B, G, R) = image[100, 50]
#DISPLAY THE VALUES IN  RGB
print("R={}, G={}, B={} @ 50X100".format(R, G, B))

#BREAKE THE LOOP
cv2.waitKey()
