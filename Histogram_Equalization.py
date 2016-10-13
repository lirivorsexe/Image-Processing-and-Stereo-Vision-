import numpy as np
import cv2
import math
from matplotlib import pyplot as plt

orgimg= cv2.imread('pic.jpg',0)
img=cv2.copyMakeBorder(orgimg,1,1,1,1,cv2.BORDER_REPLICATE)

#### Step 1: Create an array H of length G initialzed with 0
H=np.zeros((1,256))
Hc=np.zeros((1,256))
F=np.zeros((1,256))
T=np.zeros((1,256))

#### Step 2: Form the image histogram
for x in range(0,256):
    for y in range(0,256):
        gp= img[x][y]
        H[0][gp] = H[0][gp] + 1
cv2.imshow('Original Image',img)
#Htp=np.transpose(H)
plt.figure('H: Image Histogram')
plt.plot(np.transpose(H))
plt.show()

#### Step 3: Form the cummulative image histogram
Hc[0][0]= H[0][0]
for z in range(1,256):
    Hc[0][z]=Hc[0][z-1] + H[0][z]

#Hctp=np.transpose(Hc)
plt.figure('Hc: Cummulative Image Histogram')
plt.plot(np.transpose(Hc))
plt.show()

#### Step 4: Set Transformation function
for a in range(1,256):
    T[0][a]= round((255 * Hc[0][a])/(256*256)) 
#Ttp=np.transpose(T)
plt.figure('T: Transformation Function')
plt.plot(np.transpose(T))
plt.show()

####6 Step 5: Rescan image and write output image with gray levels
for i in range(1,256):
    for j in range(1,256):
        x= img[i][j]
        img[i][j] = T[0][x]

cv2.imshow('Enhanced Image', img)
for i in range(1,256):
    for j in range(1,256):
        b= T[0][j]
        F[0][b] = F[0][b] + 1

#Ftp=np.transpose(F)                 
plt.figure('Histogram of enhanced Image')
plt.plot(np.transpose(F))
plt.show()