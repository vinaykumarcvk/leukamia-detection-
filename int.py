import cv2
import numpy as np
i=0
j=0
k=0
img=cv2.imread('eight.jpg')
h=img.shape[0]
w=img.shape[1]
for i in range(h):
    for j in range(w):
        if int(img(i,j))==(162,61,192) :
            k+=1
if k>0 :
    print "chronic leukemia"

else :
    print "acute leukemia"
