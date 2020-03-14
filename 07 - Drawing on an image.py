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

# draw a blue 20px (filled in) circle on the image centered at
# x=300,y=150
output = image.copy()
cv2.circle(output, (300, 150), 20, (255, 0, 0), -1)
cv2.imshow("Circle", output)

# draw a 5px thick red line from x=60,y=20 to x=400,y=200
output = image.copy()
cv2.line(output, (60, 20), (400, 200), (0, 0, 255), 5)
cv2.imshow("Line", output)

# draw green text on the image
output = image.copy()
cv2.putText(output, "OpenCV + Jurassic Park!!!", (10, 25), 
	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Text", output)

#BREAKE THE LOOP
cv2.waitKey()