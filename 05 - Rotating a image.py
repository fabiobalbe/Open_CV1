import imutils
import cv2

#LOADING IMAGE INTO MEMORY
image = cv2.imread("jp.png")
cv2.imshow("Original Image", image)
(h, w, d) = image.shape

# let's rotate an image 45 degrees clockwise using OpenCV by first
# computing the image center, then constructing the rotation matrix,
# and then finally applying the affine warp
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("OpenCV Rotation", rotated)
cv2.waitKey(0)

#BREAKE THE LOOP
cv2.waitKey()
