"""import cv2
import numpy as np
i=0
j=0
k=0
img = cv2.imread("first.py",1)
h = img.shape[0]
w = img.shape[1]
for i in h:
    for j in w:
        if (int(img(i,j)==162,61,192)):
            k = k+1
if k>0:
    print "chronic leukemia"
else:
    print "acute leukemia"""
img = cv2.imread("first.py",1)
t = img.shape[0]
print t
cv2.waitKey()
cv2.destroyAllWindows()



    
