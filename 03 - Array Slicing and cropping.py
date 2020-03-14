import imutils
import cv2

#LOADING IMAGE INTO MEMORY
image = cv2.imread("jp.png")

#DISPLAY IMAGE ON THE SCREEN ["WINDOWS TITLE," SOURCE]
cv2.imshow("Image", image)

# extract a 100x100 pixel square ROI (Region of Interest) from the
# input image starting at x=320,y=60 at ending at x=420,y=160
roi = image[40:140, 250:350]
cv2.imshow("ROI", roi)



#BREAKE THE LOOP
cv2.waitKey()
