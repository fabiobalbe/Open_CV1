import imutils
import cv2

#LOADING IMAGE INTO MEMORY
image = cv2.imread("jp.png")

#IMAGE.SHAPE EXTRACT SIZE INFO OF THE IMAGE (NUMPY ARRAY)
(h, w, d) = image.shape

#DISPLAY THE INFO IN THE TERMINAL
#WIDTH = COLUMNS; HEIGHT = ROWS; DEPTH = IMAGE CHANNES (RGB)
print("width={}, height={}, depth={}".format(w, h, d))

#DISPLAY IMAGE ON THE SCREEN ["WINDOWS TITLE," SOURCE]
cv2.imshow("Image,", image)

#BREAKE THE LOOP
cv2.waitKey()
