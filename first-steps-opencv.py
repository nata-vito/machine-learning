import cv2
print("Package Imported")

""" 
# Image 
img = cv2.imread("Resources/logo.png")
cv2.imshow("Output", img)
cv2.waitKey(0) """

""" 
# Video
cap = cv2.VideoCapture("Resources/intro.mp4")
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)

    # Finish the execution
    if cv2.waitKey(1) & 0xff == ord('q'):
        break """

# WebCam
cap = cv2.VideoCapture(1)       # Video Source
cap.set(3,640)                  # Width
cap.set(4,480)                  # Height
cap.set(10, 100)                # Brightness

while True:
    success, img = cap.read()
    cv2.imshow("WebCam", img)   # Window to see

    # Finish the execution
    if cv2.waitKey(1) & 0xff == ord('q'):
        break 
