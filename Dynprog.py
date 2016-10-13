import cv2
import numpy as np

lft = cv2.imread('view1.png', 0)  #read it as a grayscale image
rgt = cv2.imread('view5.png', 0)

#Disparity Computation for Left Image

#OcclusionCost = 20 (You can adjust this, depending on how much threshold you want to give for noise)
oc=20
#For Dynamic Programming you have build a cost matrix. Its dimension will be numcols x numcols
#lft=cv2.copyMakeBorder(left_img,1,1,1,1,cv2.BORDER_REPLICATE)
#rgt=cv2.copyMakeBorder(right_img,1,1,1,1,cv2.BORDER_REPLICATE)


displft=np.zeros((372,465))
disprgt=np.zeros((372,465))
#CostMatrix = zeros(numcols,numcols)
#DirectionMatrix = zeros(numcols,numcols)  (This is important in Dynamic Programming. You need to know which direction you need traverse)

#We first populate the first row and column values of Cost Matri3#x

#for(i=0; i < numcols; i++)
#      CostMatrix(i,0) = i*OcclusionCost
#      CostMatrix(0,i) = i*OcclusionCost


# Now, its time to populate the whole Cost Matrix and DirectionMatrix

# Use the pseudocode from "A Maximum likelihood Stereo Algorithm" paper given as reference
for c in range (0,370):
    print c
    cm=np.zeros((463,463))
    dm=np.zeros((463,463))
    for i in range(0,463):
        cm[i,0] = i*oc
        cm[0,i] = i*oc
    for a in range (0,463):
        for b in range(0,463):
            match_cost=np.absolute(lft[c,a]-rgt[c,b])
           # if (match_cost>=oc):
            #   min1=9999
           # else:
            min1=cm[a-1,b-1]+match_cost
            min2=cm[a-1,b]+oc
            min3=cm[a,b-1]+oc
            cm[a,b]=cmin=min(min1,min2,min3)
            if(min1==cmin):
                dm[a,b]=1;
            if(min2==cmin):
                dm[a,b]=2;
            if(min3==cmin):
                dm[a,b]=3;
           

    p=462
    q=462
    while (p!=0) and  (q!=0):
        if(dm[p,q]==1):
            displft[c,p]=np.absolute(p-q)
            disprgt[c,q]=np.absolute(p-q)
            p=p-1
            q=q-1
        elif(dm[p,q]==2):
            displft[c,p]=0
            displft[c,q]=0
            p=p-1
        elif(dm[p,q]==3):
            displft[c,p]=0
            displft[c,q]=0
            q=q-1

          
        
cv2.namedWindow('displft', cv2.WINDOW_NORMAL)
cv2.imshow('displft',displft/displft.max())

cv2.namedWindow('disprgt', cv2.WINDOW_NORMAL)
cv2.imshow('disprgt',disprgt/disprgt.max())
