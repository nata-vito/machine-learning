import cv2
import numpy as np

# Sources
img = cv2.imread("Resources/rostos.jpg")

# Kernel definition to dilatation an erode images
kernel = np.ones((5,5), np.uint8)

# Convert image 
imgGray         = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                     # BGR to Gray
imgBlur         = cv2.GaussianBlur(imgGray, (7,7), 0)                       # Img to blur
imgCanny        = cv2.Canny(img, 150, 200)                                  # Canny visualization
imgDilatation   = cv2.dilate(imgCanny, kernel, iterations=1)                # Dilatation visualization
imgEroded       = cv2.erode(imgDilatation, kernel, iterations=1)            # Eroded visualization

# Show Images
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilation Image", imgDilatation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)