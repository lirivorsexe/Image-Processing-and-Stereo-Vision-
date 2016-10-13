# -*- coding: utf-8 -*-
import numpy as np
import cv2

img = cv2.imread('lena_gray.jpg',0)
gxinit= np.zeros((514,514))
gyinit= np.zeros((514,514))
gx= np.zeros((514,514))
gy= np.zeros((514,514))
mag= np.zeros((514,514))

iniarry= np.array( [[-1 , -2 , -1] , [0 , 0 , 0] , [1 , 2 , 1] ])
iniarrx= np.array( [[-1 , 0 , 1] , [-2 , 0 , 2] , [-1 , 0 , 1] ])
orgimg=cv2.copyMakeBorder(img,1,1,1,1,cv2.BORDER_REPLICATE)

for xcord in range(1,511):
 for ycord in range(1,511):
   gxinit[xcord,ycord]= orgimg[xcord-1,ycord-1]*iniarrx[0,0] + orgimg[xcord,ycord-1]*iniarrx[1,0] + orgimg[xcord+1,ycord-1]*iniarrx[2,0] + orgimg[xcord-1,ycord]*iniarrx[0,1] + orgimg[xcord,ycord]*iniarrx[1,1] + orgimg[xcord+1,ycord]*iniarrx[2,1] + orgimg[xcord-1,ycord+1]*iniarrx[0,2] + orgimg[xcord,ycord+1]*iniarrx[1,2] + orgimg[xcord+1,ycord+1]*iniarrx[2,2] 
   gyinit[xcord,ycord]= orgimg[xcord-1,ycord-1]*iniarry[0,0] + orgimg[xcord,ycord-1]*iniarry[1,0] + orgimg[xcord+1,ycord-1]*iniarry[2,0] + orgimg[xcord-1,ycord]*iniarry[0,1] + orgimg[xcord,ycord]*iniarry[1,1] + orgimg[xcord+1,ycord]*iniarry[2,1] + orgimg[xcord-1,ycord+1]*iniarry[0,2] + orgimg[xcord,ycord+1]*iniarry[1,2] + orgimg[xcord+1,ycord+1]*iniarry[2,2]
   gx[xcord,ycord]= np.absolute(gxinit[xcord,ycord])
   gy[xcord,ycord]= np.absolute(gyinit[xcord,ycord])
   curgx=np.power(gx[xcord,ycord],2)
   curgy=np.power(gy[xcord,ycord],2)
   curr=curgx + curgy
   mag[xcord,ycord]= np.power(curr,0.5)
   
gxmax =gx.max()
gymax =gy.max()
magmax= mag.max()   
cv2.namedWindow('2D:x-Gradient', cv2.WINDOW_NORMAL)
cv2.namedWindow('2D:y-Gradient', cv2.WINDOW_NORMAL)
cv2.namedWindow('2D:Gradient_Magnitude', cv2.WINDOW_NORMAL)
cv2.imshow('2D:x-Gradient',gx/gxmax)
cv2.imshow('2D:y-Gradient',gy/gymax)
cv2.imshow('2D:Gradient_Magnitude',mag/magmax)