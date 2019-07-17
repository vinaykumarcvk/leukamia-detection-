import cv2
import numpy as np
img = cv2.imread('eight.jpg',0)
th,im_th = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
im_floodfill =im_th.copy()
h,w =im_th.shape[:2]
mask=np.zeros((h+2,w+2),np.uint8)
cv2.floodFill(im_floodfill,mask,(0,0),255)
im_floodfill_inv = cv2.bitwise_not(im_floodfill)
im_out = im_th|im_floodfill_inv
cv2.imshow('original image',img)
cv2.imshow('thresh img',im_th)
cv2.imshow('floodfill img',im_floodfill)
cv2.imshow('inv floodfilled img',im_floodfill_inv)
cv2.imshow('foreground img',im_out)
cv2.waitKey()


