import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('eight.jpg')
image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(img, cv2.cv.CV_HOUGH_GRADIENT,  2, 32, param1=200, param2=100)


if circles is not None:
    
    circles = np.round(circles[0, :]).astype("int")

    for (x, y, r) in circles:
        
        cv2.circle(circles, (x, y), r, (0, 255, 0), 4)
        
    cv2.imshow("circles", np.hstack([image]))
mask = np.zeros(np.hstack([image]).shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (50,50,450,290)
cv2.grabCut(np.hstack([image]),mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
imag = np.hstack([image])*mask2[:,:,np.newaxis]
plt.imshow(imag),plt.colorbar(),plt.show()
