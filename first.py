import numpy as np
import cv2
image = cv2.imread('eight.jpg',1)
#conv = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
#hsv1 = cv2.cvtColor(conv,cv2.COLOR_RGB2HSV)
th,im_th = cv2.threshold(hsv,220,255,cv2.THRESH_BINARY_INV)
im_floodfill =im_th.copy()
h,w =im_th.shape[:2]
mask=np.zeros((h+2,w+2),np.uint8)
cv2.floodFill(im_floodfill,mask,(0,0),255)
im_floodfill_inv = cv2.bitwise_not(im_floodfill)
im_out = im_th|im_floodfill_inv
cv2.imshow('original image',image)
cv2.imshow('hsv image',hsv)
#cv2.imshow('hsv1 image',hsv1)
#cv2.imshow('conv image',conv)
cv2.imshow('thresh image',im_th)
cv2.imshow('floodfill img',im_floodfill)
cv2.imshow('inv floodfilled img',im_floodfill_inv)
cv2.imshow('foreground img',im_out)
cv2.waitKey()
cv2.destroyAllWindows()
"""import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('messi4.jpg')
img = cv2.imread('eight.jpg',1)
b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])
plt.subplot(121);plt.imshow(img) # expects distorted color
plt.subplot(122);plt.imshow(img2) # expect true color
plt.show()

cv2.imshow('bgr image',img) # expects true color
cv2.imshow('rgb image',img2) # expects distorted color
cv2.waitKey(0)
cv2.destroyAllWindows()"""
