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
	'd': lambda moveDown(x, y, z): x, y, z - s
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
plt.title('3D Random Walk with {} steps'.format(steps))
plt.show()
