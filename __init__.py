import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg.linalg import lstsq, inv
class mos():
    def __init__(self):
        self.minX=0
        self.minY=0
    
        
    def getH(self,p1,p2):
        A=[];
        for j in xrange(len(p1)*2):
            i=int(j/2)
            if(j%2==0):
                A.append([p1[i][0],p1[i][1],1,0,0,0,-p2[i][0]*p1[i][0],-p2[i][0]*p1[i][1]])
            else:
                A.append([0,0,0,p1[i][0],p1[i][1],1,-p2[i][1]*p1[i][0],-p2[i][1]*p1[i][1]])
        B=[];
        for i in xrange(len(p2)):
            B.append(p2[i][0])
            B.append(p2[i][1])
        a,b,c,d,e,f,g,h = np.linalg.lstsq(A, B)[0]
        return [[a,b,c],[d,e,f],[g,h,1]]
    
    def getPoint(self,p1,H):
        p=np.dot(H,[p1[0],p1[1],1])
        p[0]=int(float(p[0])/float(p[2]))
        p[1]=int(float(p[1])/float(p[2]))
        p[2]=1#malhash lazma
        return [p[0],p[1]]
    
    def applyMosiac(self,imgB,imgA,invH,H): 
        WidthB=len(imgB[0])
        HeightB=len(imgB)
        WidthA=len(imgA[0])
        HeightA=len(imgA)
        tl=self.getPoint([0,0],H)
        tr=self.getPoint([WidthA-1,0],H)
        dl=self.getPoint([0,HeightA-1],H)
        dr=self.getPoint([WidthA-1,HeightA-1],H)
        ##should be modified
        maxXT=max(tr[0],dr[0],WidthB-1)#tl[0],dl[0]
        maxYT=max(dr[1],dl[1],HeightB-1)#tr[1],tl[1]
        
        minXT=min(tl[0],dl[0],0)#tr[0],dr[0],
        minYT=min(tr[1],tl[1],0)#,dr[1],dl[1]
        
    
        self.minX=minXT
        self.minY=minYT
        newWidth=int(maxXT-minXT+1);
        newHeight=int(maxYT-minYT+1);
        newImg=np.zeros((newHeight,newWidth,len(imgB[0][0])),dtype=np.uint8)
        newImg[-minYT:HeightB-minYT,-minXT:WidthB-minXT]=imgB
        #pixils=[]
        for i in xrange(int(minYT), int(maxYT) + 1, 1):
            for j in xrange(int(minXT), int(maxXT) + 1, 1):
                p = [j, i, 1]
                pdash = np.dot(invH, p)
                X = pdash[0] / pdash[2]
                Y = pdash[1] / pdash[2]
                if(X >= 0 and X < WidthA and Y >= 0 and Y < HeightA):# and (i - minYT-1) < len(newImg) and (j - int(minXT))<len(newImg[0])) :
                    newImg[i - int(minYT)-1][j - int(minXT)] = imgA[Y][X]

        return newImg
        
                        
    