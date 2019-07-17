import cv2
import numpy as np
import matplotlib as plt
image = cv2.imread("fifth.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(image, cv2.cv.CV_HOUGH_GRADIENT,  2, 32, param1=200, param2=100)

if circles is not None:
    
    circles = np.round(circles[0, :]).astype("int")

    for (x, y, r) in circles:
        
        cv2.circle(circles, (x, y), r, (0, 255, 0), 4)
        
        img = np.hstack([image])
        
    cv2.imshow("circles", img)
    
cv2.waitKey(0)
cv2.destroyAllWindows()
