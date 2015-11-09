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

# Dictionary of movements
moves = {
	'f': lambda moveForward(x, y, z): x, y + s, z,
	'b': lambda moveBackward(x, y, z): x, y - s, z,
	'l': lambda moveLeft(x, y, z): x - s, y, z,
	'r': lambda moveRight(x, y, z): x + s, y, z,
	'u': lambda moveUp(x, y, z): x, y, z + s,
	'd': lambda moveDown(x, y, z): x, y, z - s,
	'fl': lambda moveForwardLeft(x, y, z): x - s / 2, y + s / 2, z,
	'fr': lambda moveForwardRight(x, y, z): x + s / 2, y + s / 2, z,
	'bl': lambda moveBackwardLeft(x, y, z): x - s / 2, y - s / 2, z,
	'br': lambda moveBackwardRight(x, y, z): x + s / 2, y - s / 2, z,
	'fu': lambda moveForwardUp(x, y, z): x, y + s / 2, z + s / 2,
	'fd': lambda moveForwardDown(x, y, z): x, y + s / 2, z - s / 2,
	'bu': lambda moveBackwardUp(x, y, z): x, y - s / 2, z + s / 2,
	'bd': lambda moveBackwardDown(x, y, z): x, y - s / 2, z - s / 2,
	'lu': lambda moveLeftUp(x, y, z): x - s / 2, y, z + s / 2,
	'ld': lambda moveLeftDown(x, y, z): x - s / 2, y, z - s / 2,
	'ru': lambda moveRightUp(x, y, z): x + s / 2, y, z + s / 2,
	'rd': lambda moveRightDown(x, y, z): x + s / 2, y, z - s / 2,
	'ful': lambda moveForwardUpLeft(x, y, z): x - s / 3, y + s / 3, z + s / 3,
	'fur': lambda moveForwardUpRight(x, y, z): x + s / 3, y + s / 3, z + s / 3,
	'fdl': lambda moveForwardDownLeft(x, y, z): x - s / 3, y + s / 3, z - s / 3,
	'fdr': lambda moveForwardDownRight(x, y, z): x + s / 3, y + s / 3, z - s / 3,
	'bul': lambda moveBackwardUpLeft(x, y, z): x - s / 3, y - s / 3, z + s / 3,
	'bur': lambda moveBackwardUpRight(x, y, z): x + s / 3, y - s / 3, z + s / 3,
	'bdl': lambda moveBackwardDownLeft(x, y, z): x - s / 3, y - s / 3, z - s / 3,
	'ddr': lambda moveBackwardDownRight(x, y, z): x + s / 3, y - s / 3, z - s / 3
}

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

# Interpolate between the points to plot the paths between the points
points = 1
X2 = np.interp(np.arange(steps * points), np.arange(steps) * points, X)
Y2 = np.interp(np.arange(steps * points), np.arange(steps) * points, Y)
Z2 = np.interp(np.arange(steps * points), np.arange(steps) * points, Z)
ax = plt.axes(projection='3d')
ax.scatter(X2, Y2, Z2, c=range(steps * points), linewidths=0, s=3)
ax.axis('equal')
plt.title('3D Modified Random Walk with {} steps'.format(steps))
plt.show()
