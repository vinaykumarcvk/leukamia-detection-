import cv2
import numpy as np
i=0
image1= cv2.imread("eight.jpg")
cv2.imshow("original",image1)
image2=image1
image = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(image, cv2.cv.CV_HOUGH_GRADIENT,  2, 32, param1=200, param2=100)
if circles is not None:
      circles = np.round(circles[0, :]).astype("int")
      for (x, y, r) in circles:
         cv2.circle(circles, (x, y), r, (0, 255, 0), 4)
      cv2.imshow("WBC NUCLEII", np.hstack([image]))

thresh2=cv2.bilateralFilter(image,11,17,17)
cv2.imshow("NOISE ELIMINATION",thresh2)
_, thresh= cv2.threshold(thresh2,130,255,cv2.THRESH_BINARY_INV)
cv2.imshow("AREA OF INTEREST",thresh)
img1=cv2.Canny(thresh,100.200)
cnts,_=cv2.findContours(img1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for c in cnts :
    peri=cv2.arcLength(c,True)
    approx=cv2.approxPolyDP(c,0.02*peri,True)
    cv2.drawContours(image2,[approx],-1,(0,255,0),2)
    if cv2.contourArea(c)<15 :
        continue
    else:
        i=i+1
print i
cv2.imshow("contours",image2)
cv2.imshow("img",thresh)
cv2.waitKey()
cv2.destroyAllWindows()
