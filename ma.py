import numpy as np
import cv2
img=cv2.imread('eight.jpg',1)

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
print hsv
lower=np.array([155,50,50])
upper=np.array([175,255,255])
mask=cv2.inRange(img,lower,upper)
res = cv2.bitwise_not(mask)
fin=cv2.bitwise_and(img,img,mask = res)
##cv2.imshow('img',img)
#cv2.imshow('mask',mask)
cv2.imshow('hsv',hsv)
#cv2.imshow('res',res)
cv2.imshow('fin',fin)
# cv2.imshow('red',red)
cv2.waitKey()
cv2.destroyAllWindows()
