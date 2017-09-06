
# coding: utf-8

# In[ ]:

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import *
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
import mpl_toolkits.mplot3d.art3d as art3d
from matplotlib import interactive



# In[ ]:

R = input("Radius: ")
R = float(R)
n = input("Durchgänge: ")
n = int(n)
a = input("negative Spulenbegrenzung: ")
a = float(a)
b = input("positive Spulenbegrenzung: ")
b = float(b)
n = input("Windungsdichte: ")
n = int(n)

fig = plt.figure()
ax = fig.gca(projection='3d')
y = np.linspace(-R-5,R+5,n)
z = np.linspace(a-2,b+2,n)
X = np.zeros((n,n), dtype=float, order='C')
Y, Z = np.meshgrid(y,z)

def dByring(phi, y, z):    
    dB = (np.sin(phi)*z)/((R**2+y**2+z**2-2*y*R*np.sin(phi))**(3/2))
    return dB

def dBzring(phi, y, z):
    return (R-y*np.sin(phi))/((R**2+y**2+z**2-2*y*R*np.sin(phi))**(3/2))

def dBy(zWert, yWert):
    var, err = quad(dByring, 0, 2*np.pi, args=(yWert,zWert))
    return var

def dBz(zWert, yWert):
    var, err = quad(dBzring, 0, 2*np.pi, args=(yWert,zWert))
    return var

@np.vectorize
def By(zPos, yPos):
    var, err = quad(dBy, a+zPos, b+zPos, args=(yPos))
    return var

@np.vectorize
def Bz(zPos, yPos):
    var, err = quad(dBz, a+zPos, b+zPos, args=(yPos))
    return var

XFeld = np.zeros((n,n,n), dtype=float, order='C')
YFeld = By(Z,Y)
ZFeld = Bz(Z,Y)

ax.quiver(X,Y,Z,XFeld,YFeld,ZFeld,color='tomato', length=(R/n))
i = a
#i = Zählvariable
while i<=b:    
    conductor = plt.Circle((0, 0), R,color='black',clip_on=False, fill=False)
    ax.add_patch(conductor)
    art3d.pathpatch_2d_to_3d(conductor, z=i, zdir="z")
    
    #Ringleiter erstellen
    class Arrow3D(FancyArrowPatch):
        def __init__(self, xs, ys, zs, *args, **kwargs):
            FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
            self._verts3d = xs, ys, zs
    
        def draw(self, renderer):
            xs3d, ys3d, zs3d = self._verts3d
            xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
            self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
            FancyArrowPatch.draw(self, renderer)
    i = i + ((b-a)/n)
#geplottete Ringleiter nähern die Spule als mehrere Ringleiter aufgereiht
ax.set_xlim3d(-2*R, 2*R)
ax.set_ylim3d(-2*R, 2*R)
ax.set_zlim3d(a, b)
ax.set_xlabel('X-Wert in Meter')
ax.set_ylabel('Y-Wert in Meter')
ax.set_zlabel('Z-Wert in Meter')
interactive(True)
plt.show()

