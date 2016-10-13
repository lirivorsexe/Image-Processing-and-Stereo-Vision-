# -*- coding: utf-8 -*-
import numpy as np
import cv2
import math
g = cv2.imread('view1.png',1)
f = cv2.imread('view5.png',1)
dp1 = cv2.imread('disp1.png',1)
dp2 = cv2.imread('disp5.png',1)
g=cv2.copyMakeBorder(g,1,1,1,1,cv2.BORDER_REPLICATE)
f=cv2.copyMakeBorder(f,1,1,1,1,cv2.BORDER_REPLICATE)
dp1=cv2.copyMakeBorder(dp1,1,1,1,1,cv2.BORDER_REPLICATE)
dp2=cv2.copyMakeBorder(dp2,1,1,1,1,cv2.BORDER_REPLICATE)
new=np.zeros((372,465,3))
new1=np.zeros((372,465,3))
new2=np.zeros((372,465,3))
new3=np.zeros((372,465,3))
new3=np.zeros((372,465,3))
new4=np.zeros((372,465,3))
new5=np.zeros((372,465,3))
new6=np.zeros((372,465,3))
view3=np.zeros((372,465,3))

for i in range(1,371):         # left
    for j in range(1,464):
        m=dp1[i][j][1]
        n=int(m/2)
        if(j-n>=1):
            new[i][j-n]=g[i][j]
                          
for i in range(1,371):             
    for j in range(1,464):
     o=dp2[i][j][1]
     n=int(o/2)
     if(j+n<463):  
        p=dp2[i][j+n][1]
        m=int(p/2)
        if(o>p):
            if(new[i][j+n][1]==0)and (new[i][j+n][0]==0) and(new[i][j+n][2]==0):  
                new1[i][j+n]=f[i][j] 

for i in range(1,371):
    for j in range(1,464):
        new2[i][j]=new[i][j]+new1[i][j]                  
                            
for i in range(1,371):                    
    for j in range(1,464):
        o=dp2[i][j][1]
        n=int(o/2)
        if(j+n<463):
            if(new2[i][j+n][1]==0)and (new2[i][j+n][0]==0) and(new2[i][j+n][2]==0):    
                new3[i][j+n]=f[i][j]  

for i in range(1,371):
    for j in range(1,464):
        new4[i][j]=new2[i][j]+new3[i][j] 

for i in range(1,371):               
    for j in range(1,464):
        o=dp1[i][j][1]
        n=int(o/2)
        if(j+n<463):
            if(new4[i][j+n][1]==0)and (new4[i][j+n][0]==0) and(new4[i][j+n][2]==0):    
                new5[i][j+n]=f[i][j]
 
for i in range(1,371):
    for j in range(1,464):
        new6[i][j]=new1[i][j]+new3[i][j]+new5[i][j] 
for i in range(1,371):
    for j in range(1,464):
        view3[i][j]=new[i][j]+new6[i][j]                
        

cv2.namedWindow('view1', cv2.WINDOW_NORMAL)
cv2.namedWindow('view5', cv2.WINDOW_NORMAL)
cv2.namedWindow('image from view1', cv2.WINDOW_NORMAL)
cv2.namedWindow('image from view2', cv2.WINDOW_NORMAL)
cv2.namedWindow('view3', cv2.WINDOW_NORMAL)

cv2.imshow('view1',g)
cv2.imshow('view5',f)
cv2.imshow('image from view1',new/new.max())
cv2.imshow('image from view2',new6/new6.max())
cv2.imshow('view3',view3/view3.max())
