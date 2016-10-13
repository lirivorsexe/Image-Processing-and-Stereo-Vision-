# -*- coding: utf-8 -*-
import numpy as np
import cv2

img = cv2.imread('lenagray.png',0)
gxinit_1= np.zeros((514,514))
gyinit_1= np.zeros((514,514))
gxinit_2= np.zeros((514,514))
gyinit_2= np.zeros((514,514))
gx= np.zeros((514,514))
gy= np.zeros((514,514))
mag= np.zeros((514,514))

iniarrx_1= np.array((1,2,1))
iniarrx_1= np.reshape(iniarrx_1,[3,1])
iniarrx_2= np.array((-1,0,1))
iniarrx_2= np.reshape(iniarrx_2,[1,3])
iniarry_1=np.array((-1,0,1))
iniarry_1=np.reshape(iniarry_1,[3,1])
iniarry_2=np.array((1,2,1))
iniarry_2=np.reshape(iniarry_2,[1,3])
orgimg= cv2.copyMakeBorder(img,1,1,1,1,cv2.BORDER_REPLICATE)

for xcord in range(1,511):
    for ycord in range(1,511):
        gxinit_1[xcord,ycord]= orgimg[xcord-1,ycord]*iniarrx_1[0,0] + orgimg[xcord,ycord]*iniarrx_1[1,0] + orgimg[xcord+1,ycord]*iniarrx_1[2,0]
        gyinit_1[xcord,ycord]= orgimg[xcord-1,ycord]*iniarry_1[0,0] + orgimg[xcord,ycord]*iniarry_1[1,0] + orgimg[xcord+1,ycord]*iniarry_1[2,0]
     
for xcord in range(1,511):
 for ycord in range(1,511):
     gxinit_2[xcord,ycord]= gxinit_1[xcord,ycord-1]*iniarrx_2[0,0] + gxinit_1[xcord,ycord]*iniarrx_2[0,1] + gxinit_1[xcord,ycord+1]*iniarrx_2[0,2]
     gyinit_2[xcord,ycord]= gyinit_1[xcord,ycord-1]*iniarry_2[0,0] + gyinit_1[xcord,ycord]*iniarry_2[0,1] + gyinit_1[xcord,ycord+1]*iniarry_2[0,2]
     gx[xcord,ycord]= np.absolute(gxinit_2[xcord,ycord])
     gy[xcord,ycord]= np.absolute(gyinit_2[xcord,ycord])
     curgx=np.power(gx[xcord,ycord],2)
     curgy=np.power(gy[xcord,ycord],2)
     curr=curgx + curgy
     mag[xcord,ycord]= np.power(curr,0.5)
   
gxmax =gx.max()
gymax =gy.max()
magmax= mag.max()
cv2.namedWindow('1D:x-Gradient', cv2.WINDOW_NORMAL)
cv2.namedWindow('1D:y-Gradient', cv2.WINDOW_NORMAL)
cv2.namedWindow('1D:Gradient_Magnitude', cv2.WINDOW_NORMAL)
cv2.imshow('1D:x-Gradient',gx/gxmax)
cv2.imshow('1D:y-Gradient',gy/gymax)
cv2.imshow('1D:Gradient_Magnitude',mag/magmax)
