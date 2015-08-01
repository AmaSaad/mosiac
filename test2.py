'''
Created on Apr 17, 2013

@author: ahmed
'''
from numpy import *
nx, ny = (3, 2)
x = linspace(0, 1, nx)
y = linspace(0, 1, ny)
xv, yv = meshgrid(x, y)
print xv,yv