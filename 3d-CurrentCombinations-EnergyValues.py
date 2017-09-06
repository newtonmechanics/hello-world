
# coding: utf-8

# In[ ]:

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

l = input("L1: ")
l = float(l)
i = input("L2: ")
i = float(i)
k = input("Kopplungsfaktor: ")
k = float(k)
M = k*((l*i)**(1/2))
fig = plt.figure()
ax = fig.gca(projection='3d')


X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
Z = 0.5*l*X + 0.5*i*Y + M*X*Y
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.seismic,
                       linewidth=0, antialiased=True)
ax.set_zlim(-20, 20)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=1, aspect=5)
ax.set_xlabel('Strom in der Primärspule in Ampere')
ax.set_ylabel('Strom in der Sekundärspule in Ampere')
ax.set_zlabel('Energie im Transformator in Joul')
ax.set_title('Kombination von Strömen und die dazugehörige Energie')
plt.show()

