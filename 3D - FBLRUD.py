import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import savefig
#Starting point
X=[0]
Y=[0]
Z=[0]
#Size of step
s=1
#Number of steps to process
steps=10
#Movement functions
def moveForward(x,y,z): return x,y+s,z
def moveBackward(x,y,z): return x,y-s,z
def moveLeft(x,y,z): return x-s,y,z
def moveRight(x,y,z): return x+s,y,z
def moveUp(x,y,z): return x,y,z+s
def moveDown(x,y,z): return x,y,z-s
#Dictionnary of movements
moves={'f':moveForward,'b':moveBackward,'l':moveLeft,'r':moveRight,'u':moveUp,'d':moveDown}
#Store the possibles movements in a set
moveSet=set(list(moves.keys()))
#Move randomly 'steps' times
for step in range(1,steps+1):
    movement=random.sample(moveSet,1)[0]
    #get the new point according to the random movement
    newPoint=moves[movement](X[step-1],Y[step-1],Z[step-1])
    X.append(newPoint[0])
    Y.append(newPoint[1])
    Z.append(newPoint[2])
#Plot all the points
fig=plt.figure(figsize=(14,14))
ax=plt.axes(projection='3d')
ax.scatter(X,Y,Z,marker=None)
ax.plot(X,Y,Z,color='black')
#Plot the fist and last points for visualization
xlimits=[X[0],X[-1]]
ylimits=[Y[0],Y[-1]]
zlimits=[Z[0],Z[-1]]
ax.scatter(xlimits,ylimits,zlimits,marker='o',s=100,c='red')
#Finalize and show the graph
plt.title("3D Random Walk with "+str(steps)+" steps")
plt.show()
#savefig('foo.pdf', bbox_inches='tight')