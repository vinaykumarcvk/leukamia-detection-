import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('eight.jpg',1)
hsv = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
gray = cv2.cvtColor(img,cv2.COLOR_HSV2GRAY)
blur = cv2.GaussianBlur(hsv,(5,5),0)
ret3,im_th = cv2.threshold(hsv,0,255,cv2.THRESH_BINARY)
print ret3
kernel = np.ones((3,3),np.uint8)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
opening = cv2.morphologyEx(im_th, cv2.MORPH_OPEN, kernel)
titles = ['res','thresh','open']
images= [img,im_th,opening]
for i in range(3):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],'gray')
    plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()
