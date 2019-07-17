from __future__ import print_function
import numpy as np
import cv2
img = cv2.imread('first.jpg',0)
cv2.imshow('original',img)
h=img.shape[0]
w=img.shape[1]
#instead of above 2lines:(h,w)=img.shape[:2]
#print (h,w)
if h>1000 and w>1000:
    r=500.0/img.shape[1]
    dim=(500,int(img.shape[0]*r))
    res=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
else:
    r=500.0/img.shape[1]
    dim=(500,int(img.shape[0]*r))
    res=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
cv2.imshow('resized',res)
#print (dim) 
cv2.waitKey(0)
cv2.destroyAllWindows()
