import cv2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
import mosiac
from numpy.linalg.linalg import dot,inv
from matplotlib.pyplot import plot
fig = plt.figure()
figA = fig.add_subplot(1,2,1)
figB = fig.add_subplot(1,2,2)
# Manually identifies corresponding points from two views
def getCorrespondence(imageA, imageB,pts):
	# Display images, select matching points
	# Display the image
	figA.imshow(imageA,origin='lower')
	figB.imshow(imageB,origin='lower')
	plt.axis('image')
	pts = plt.ginput(n=pts*2, timeout=0)
	pts = np.reshape(pts, (2, pts, 2))
	return pts

if __name__ == "__main__":
	# Read image file names
	fileA ="uttower1.jpg"# raw_input("please read ur image name here: ")
	fileB ="uttower2.jpg"#raw_input("please read ur image name here: ")
	imageA = mpimg.imread(fileA)
	imageB = mpimg.imread(fileB)
	pts = getCorrespondence(imageA, imageB,8)
	mos=mosiac.mos()
	#H=mos.getH_2(pts)#(pts[0], pts[1])
	#print H
	H=mos.getH(pts[0], pts[1])#(pts, 8)#(pts[0], pts[1])
	
	
	invH=inv(H)
	
	newImg=mos.applyMosiac(imageB,imageA,invH,H)
	
	#    fig = plt.figure()
	plt.show();
	for pt in pts[0]:
		p=np.dot(H,[pt[0],pt[1],1])
		p[0]=int(float(p[0])/float(p[2]))
		p[1]=int(float(p[1])/float(p[2]))
		p[2]=1
		plt.plot(p[0]-mos.minX,p[1]-mos.minY,'xr',)
	#   
	plt.imshow(newImg)
	plt.axis('image')
	
	plt.show()
		
