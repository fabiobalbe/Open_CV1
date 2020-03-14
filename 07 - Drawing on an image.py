import imutils
import cv2

#LOADING IMAGE INTO MEMORY
image = cv2.imread("jp.png")
cv2.imshow("Original Image", image)
(h, w, d) = image.shape

# draw a 2px thick red rectangle surrounding the face
#cv2.rectangle(output, (Xa, Ya), (Xb, Yb), (B, G, R), 2)
output = image.copy()
cv2.rectangle(output, (260, 20), (360, 120), (0, 0, 255), 2)
cv2.imshow("Rectangle", output)

#BREAKE THE LOOP
cv2.waitKey()