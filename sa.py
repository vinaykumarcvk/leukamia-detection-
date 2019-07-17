import cv2
import numpy as np
from matplotlib import pyplot as plt
from tkinter import *
import tkinter as tk
import sys
from PIL import Image
from copy import deepcopy
from PIL import ImageTk
import tkinter.filedialog
#global cv2
def select_image():
    
    path = tkinter.filedialog.askopenfilename()
    if len(path) > 0:
        #image = cv2.imread(path)
        image1=cv2.imread(path,1)
        image_1=deepcopy(image1)
        #cv2.imshow("original",image1)
        image2=deepcopy(image1)
        image = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        circles = cv2.HoughCircles(image, cv2.cv.CV_HOUGH_GRADIENT,  2, 32, param1=200, param2=100)
        if circles is not None:
              circles = np.round(circles[0, :]).astype("int")
              for (x, y, r) in circles:
                 cv2.circle(circles, (x, y), r, (0, 255, 0), 4)
              
              img = np.hstack([image])
        

        thresh2=cv2.bilateralFilter(image,11,17,17)
        
        _, thresh= cv2.threshold(thresh2,130,255,cv2.THRESH_BINARY_INV)
        
        thresh3=deepcopy(thresh)
        t=cv2.countNonZero(thresh)
        #print t
        if t<1000:
            print "NO TYPE OF  LEUKEMIA DETECTED"
        elif t>1000 and t<8000:
            print "CHRONIC STAGE OF LEUKEMIA"
        else:
            print "ACUTE LEUKEMIA"
            
                
        cnts,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        i=0
        for c in cnts :
            peri=cv2.arcLength(c,True)
            approx=cv2.approxPolyDP(c,0.02*peri,True)
            cv2.drawContours(image2,[approx],-1,(0,255,0),2)
            if cv2.contourArea(c)<25:
                continue
            else:
                i=i+1
        print i
        titles = ['Original Image','WBC Nucleii','Noise Elimination',
                  'Area of Interest','Contours']
        images = [image_1,img,thresh2,thresh3,image2]
        for i in range(5):
            plt.subplot(2,3,i+1)
            plt.imshow(images[i],'gray')
            plt.xticks([]),plt.yticks([])
        plt.show()
        
root =  tk.Tk()
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
