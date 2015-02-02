import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import savefig
import numpy as np
# Starting point
X = [0]
Y = [0]
Z = [0]
# Size of step
s = 1
# Number of steps to process
steps = 10000
# Movement functions, here there are 3*3*3-1 possibilities
def moveForward(x, y, z) : return x, y + s, z
def moveBackward(x, y, z): return x, y - s, z
def moveLeft(x, y, z) : return x - s, y, z
def moveRight(x, y, z) : return x + s, y, z
def moveUp(x, y, z) : return x, y, z + s
def moveDown(x, y, z): return x, y, z - s
def moveForwardLeft(x, y, z): return x - s / 2, y + s / 2, z
def moveForwardRight(x, y, z): return x + s / 2, y + s / 2, z
def moveBackwardLeft(x, y, z): return x - s / 2, y - s / 2, z
def moveBackwardRight(x, y, z): return x + s / 2, y - s / 2, z
def moveForwardUp(x, y, z): return x, y + s / 2, z + s / 2
def moveForwardDown(x, y, z): return x, y + s / 2, z - s / 2
def moveBackwardUp(x, y, z): return x, y - s / 2, z + s / 2
def moveBackwardDown(x, y, z): return x, y - s / 2, z - s / 2
def moveLeftUp(x, y, z): return x - s / 2, y, z + s / 2
def moveLeftDown(x, y, z): return x - s / 2, y, z - s / 2
def moveRightUp(x, y, z): return x + s / 2, y, z + s / 2
def moveRightDown(x, y, z): return x + s / 2, y, z - s / 2
def moveForwardUpLeft(x, y, z): return x - s / 3, y + s / 3, z + s / 3
def moveForwardUpRight(x, y, z): return x + s / 3, y + s / 3, z + s / 3
def moveForwardDownLeft(x, y, z): return x - s / 3, y + s / 3, z - s / 3
def moveForwardDownRight(x, y, z): return x + s / 3, y + s / 3, z - s / 3
def moveBackwardUpLeft(x, y, z): return x - s / 3, y - s / 3, z + s / 3
def moveBackwardUpRight(x, y, z): return x + s / 3, y - s / 3, z + s / 3
def moveBackwardDownLeft(x, y, z): return x - s / 3, y - s / 3, z - s / 3
def moveBackwardDownRight(x, y, z): return x + s / 3, y - s / 3, z - s / 3
# Dictionary of movements
moves = {
'f':moveForward, 'b':moveBackward, 'l':moveLeft, 'r':moveRight, 'u':moveUp, 'd':moveDown, 'fl':moveForwardLeft, 'fr':moveForwardRight, 'bl':moveBackwardLeft, 'br':moveBackwardRight, 'fu':moveForwardUp, 'fd':moveForwardDown, 'bu':moveBackwardUp, 'bd':moveBackwardDown, 'lu':moveLeftUp, 'ld':moveLeftDown, 'ru':moveRightUp, 'rd':moveRightDown, 'ful':moveForwardUpLeft, 'fur':moveForwardUpRight, 'fdl':moveForwardDownLeft, 'fdr':moveForwardDownRight, 'bul':moveBackwardUpLeft, 'bur':moveBackwardUpRight, 'bdl':moveBackwardDownLeft, 'ddr':moveBackwardDownRight}
# Store the possibles movements in a set
moveSet = set(list(moves.keys()))
# Move randomly 'steps' times
for step in range(1, steps):
    movement = random.sample(moveSet, 1)[0]
    # get the new point according to the random movement
    newPoint = moves[movement](X[step - 1], Y[step - 1], Z[step - 1])
    X.append(newPoint[0])
    Y.append(newPoint[1])
    Z.append(newPoint[2])
# Interpolate between the points
points = 1
X2 = np.interp(np.arange(steps * points), np.arange(steps) * points, X)
Y2 = np.interp(np.arange(steps * points), np.arange(steps) * points, Y)
Z2 = np.interp(np.arange(steps * points), np.arange(steps) * points, Z)
ax = plt.axes(projection='3d')
ax.scatter(X2, Y2, Z2, c=range(steps * points), linewidths=0, s=3)
ax.axis('equal')
plt.title("3D Random Walk with " + str(steps) + " steps")
plt.show()
# savefig('foo.pdf', bbox_inches='tight')
