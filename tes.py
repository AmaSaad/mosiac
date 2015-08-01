import numpy, scipy
from scipy import interpolate

kernelIn = numpy.array([
    [[0]*3,[-2]*3,[0]*3],
    [[-2]*3,[11]*3,[-2]*3],
    [[0]*3,[-2]*3,[0]*3]])
inKSize = len(kernelIn)
outKSize = 7

kernelOut = numpy.zeros((outKSize),numpy.uint8)

x = numpy.arange(3)
y = numpy.arange(3)
z=numpy.arange(3)

t = kernelIn

xx = numpy.linspace(x.min(),x.max(),outKSize)
yy = numpy.linspace(y.min(),y.max(),outKSize)
zz = numpy.linspace(z.min(),z.max(),outKSize)

print xx
print yy
newKernel = interpolate.RectBivariateSpline(x,y,z,t, kx=3,ky=3,kz=3)

kernelOut = newKernel(xx,yy)
print kernelOut