import cv2
import numpy as np
import matplotlib as plt
from tkinter import *
import tkinter as tk
import sys
from PIL import Image
from PIL import ImageTk
import tkinter.filedialog
#global cv2
i=0
root = tk.Tk()
def select_image():
    
    path = tkinter.filedialog.askopenfilename()
    if len(path) > 0:
        #image = cv2.imread(path)
        image1=cv2.imread(path,1)
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
        mask=cv2.bitwise_and(image1,image1,mask=thresh)
        img1=cv2.Canny(img1,100,200)
        cv2.imshow('mask',mask)
        t=cv2.countNonZero(thresh)
        print (t)
        if t>8000:
            print "ACUTE STAGE OF LEUKEMIA"
        else:
            print "CHRONIC STAGE OF LEUKEMIA"

        cnts,_=cv2.findContours(img1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
        for c in cnts :
            peri=cv2.arcLength(c,True)
            approx=cv2.approxPolyDP(c,0.02*peri,True)
            cv2.drawContours(image2,[approx],-1,(0,255,0),2)
            if cv2.contourArea(c)<25 :
                continue
            else:
                i=i+1
        print i
        cv2.imshow("contours",image2)
        cv2.imshow("img",thresh)

def print_out(i):
    
    Entry(root,text = "%d" %(i)).grid(row=2,column =1)
    


print_out(i)
blank = Entry(root)
blank.grid(row=2, column=1)
#root = tk.Tk()
Label(root,text ="Number of white blood cells is/are").grid(row = 0)
frame = tk.Frame(root)
frame.pack()
path = 'logo1.jpg'
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
button = tk.Button(frame, 
                       text="select an image", 
                       command=select_image)
button.pack(side="bottom",fill= "both", expand="yes", padx="50", pady="50")


root.mainloop()

