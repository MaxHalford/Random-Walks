import random
import matplotlib.pyplot as plt
from pylab import savefig
import numpy as np
#Starting point
X = [0]
Y = [0]
#Size of step
s = 1
#Number of steps to process
steps = 1000
#Movement functions
def moveForward(x, y) : return x, y + s
def moveBackward(x, y) : return x, y - s
def moveLeft(x, y) : return x - s, y
def moveRight(x, y) : return x + s, y
def moveForwardLeft(x, y) : return x - s / 2, y + s / 2
def moveForwardRight(x, y) : return x + s / 2, y + s / 2
def moveBackwardLeft(x, y) : return x - s / 2, y - s / 2
def moveBackwardRight(x, y) : return x + s / 2, y - s / 2
#Dictionary of movements
moves = {'f' : moveForward, 'b' : moveBackward, 'l' : moveLeft,
         'r' : moveRight, 'fl' : moveForwardLeft, 'fr' : moveForwardRight,
         'bl' : moveBackwardLeft, 'br' : moveBackwardRight}
#Store the possibles movements in a set
moveSet = set(list(moves.keys()))
#Move randomly 'steps' times
for step in range(1, steps):
    movement = random.sample(moveSet, 1)[0]
    #get the new point according to the random movement
    newPoint = moves[movement](X[step - 1], Y[step - 1])
    X.append(newPoint[0])
    Y.append(newPoint[1])
# Interpolate between the points
points = 10
X2 = np.interp(np.arange(steps * points), np.arange(steps) * points, X)
Y2 = np.interp(np.arange(steps * points), np.arange(steps) * points, Y)
plt.scatter(X2, Y2, c = range(steps * points), linewidths = 0, s = 3)
plt.axis('equal')
plt.title("2D Modified Random Walk with "+str(steps)+" steps")
plt.show()
#savefig('foo.pdf', bbox_inches='tight')
