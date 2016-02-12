import cv2
import numpy as np
from numpy import unravel_index

image=raw_input("Enter the path of the grayscale image:")
img=cv2.imread(image)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # convert image to grayscale

r,c=gray.shape
matrix=np.zeros((r+1,c+1),int) 
output0=np.zeros((r+1,c+1),int) # Stores the largest square of zeros
output1=np.zeros((r+1,c+1),int) # Stores the largest square of ones

for i in range(r):
	for j in range(c):
		matrix[i+1,j+1]=gray[i,j]

for i in range(1,r+1): # Initialize first row
	if matrix[i,1]>=0 and matrix[i,1]<=63:
		output0[i,1]=0
		output1[i,1]=0

	elif matrix[i,1]>=192 and matrix[i,1]<=255:
		output0[i,1]=1
		output1[i,1]=1

for i in range(1,c+1): # Initialize first column
	if matrix[1,i]>=0 and matrix[1,i]<=63:
		output0[1,i]=0
		output1[1,i]=0

	elif matrix[1,i]>=192 and matrix[1,i]<=255:
		output0[1,i]=1
		output1[1,i]=1

for i in xrange(2,r+1):
	for j in xrange(2,c+1):
		if matrix[i,j]>=0 and matrix[i,j]<=63: # Pixel range to be considered for Dark pixels
			output0[i][j]=min(output0[i][j-1],output0[i-1][j],output0[i-1][j-1])+1; # Check whether this pixel is part of the square or not

for i in xrange(2,r+1):
	for j in xrange(2,c+1):
		if matrix[i,j]>=192 and matrix[i,j]<=255: # Pixel range to be considered for Light pixels
			output1[i][j]=min(output1[i][j-1],output1[i-1][j],output1[i-1][j-1])+1;

# Max size of squres
max0=np.amax(output0) 
max1=np.amax(output1)
# Position of the max size square
max0_row,max0_col=unravel_index(output0.argmax(),output0.shape) 
max1_row,max1_col=unravel_index(output1.argmax(),output1.shape)

print "\nLargest Monochromatic Square is of 0's. Size is:%d\n"%max0
print "At index:["+str(max0_row)+","+str(max0_col)+"]\n"
cv2.rectangle(img,(max0_col-max0,max0_row-max0),(max0_col,max0_row),[0,255,255],2) # Draw a square on the answer found

print "\nLargest Monochromatic Square is of 1's. Size is:%d\n"%max1
print "At index:["+str(max1_row)+","+str(max1_col)+"]\n"
cv2.rectangle(img,(max1_col-max1,max1_row-max1),(max1_col,max1_row),[0,0,255],2)

cv2.imshow('Largest Square',img) # Display the resultant image
cv2.waitKey(0)
