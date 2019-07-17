import cv2
import numpy as np
i=0
image1= cv2.imread("seventh.jpg")
cv2.imshow("original",image1)
image2=image1
image = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
img1=image
"""circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT,  2, 32, param1=200, param2=100)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
      # draw the outer circle
    cv2.circle(img1,(i[0],i[1]),i[2],(0,255,0),2)
      # draw the center of the circle
    cv2.circle(img1,(i[0],i[1]),2,(0,0,255),3)
cv2.imshow('detected circles',img1)
if circles is not None:
      circles = np.round(circles[0, :]).astype("int")
      for (x, y, r) in circles:
         cv2.circle(circles, (x, y), r, (0, 255, 0), 4)
      cv2.imshow("WBC NUCLEII", np.hstack([image]))"""

thresh2=cv2.bilateralFilter(image,11,17,17)
cv2.imshow("NOISE ELIMINATION",thresh2)
_, thresh= cv2.threshold(thresh2,130,255,cv2.THRESH_BINARY_INV)
cv2.imshow("AREA OF INTEREST",thresh)

"""img1=cv2.Canny(thresh,100,200)
cv2.imshow('canny',img1)
cv2.imshow('fasak',th3)"""
kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
cv2.imshow('close',closing)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
cv2.imshow('open',opening)
cnts,hiearchy=cv2.findContours(opening,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for c in cnts :
    perimeter=cv2.arcLength(c,True)
    print(perimeter)

    if perimeter<70 :
        continue
    else:
        i=i+1

    peri=cv2.arcLength(c,True)
    approx=cv2.approxPolyDP(c,0.01*peri,True)
    cv2.drawContours(image2,[approx],-1,(0,255,0),2)
i=i+1    
print i
cv2.imshow("contours",image2)
cv2.waitKey()
cv2.destroyAllWindows()
