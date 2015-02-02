import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import savefig
import numpy as np
#Starting point
X = [0]
Y = [0]
Z = [0]
#Size of step
s = 1
#Number of steps to process
steps = 1000
#Movement functions
def moveForward(x, y, z) : return x, y + s, z
def moveBackward(x, y, z) : return x, y - s, z
def moveLeft(x, y, z) : return x - s, y , z
def moveRight(x, y, z) : return x + s, y, z
def moveUp(x, y, z): return x, y, z + s
def moveDown(x, y, z): return x, y, z - s
#Dictionary of movements
moves={'f' : moveForward, 'b' : moveBackward, 'l' : moveLeft,
       'r' :moveRight, 'u' : moveUp, 'd' : moveDown}
#Store the possibles movements in a set
moveSet = set(list(moves.keys()))
#Move randomly 'steps' times
for step in range(1, steps):
    movement = random.sample(moveSet, 1)[0]
    #get the new point according to the random movement
    newPoint = moves[movement](X[step - 1], Y[step - 1], Z[step - 1])
    X.append(newPoint[0])
    Y.append(newPoint[1])
    Z.append(newPoint[2])
# Interpolate between the points
points = 10
X2 = np.interp(np.arange(steps * points), np.arange(steps) * points, X)
Y2 = np.interp(np.arange(steps * points), np.arange(steps) * points, Y)
Z2 = np.interp(np.arange(steps * points), np.arange(steps) * points, Z)
ax=plt.axes(projection='3d')
ax.scatter(X2, Y2, Z2, c = range(steps * points), linewidths = 0, s = 3)
ax.axis('equal')
plt.title("3D Random Walk with "+str(steps)+" steps")
plt.show()
#savefig('foo.pdf', bbox_inches='tight')
