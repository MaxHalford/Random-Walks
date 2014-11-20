import random
import matplotlib.pyplot as plt
from pylab import savefig
#Starting point
X=[0]
Y=[0]
#Size of step
s=1
#Number of steps to process
steps=1000
#Movement functions
def moveForward(x,y): return x,y+s
def moveBackward(x,y): return x,y-s
def moveLeft(x,y): return x-s,y
def moveRight(x,y): return x+s,y
def moveForwardLeft(x,y): return x-s/2,y+s/2
def moveForwardRight(x,y): return x+s/2,y+s/2
def moveBackwardLeft(x,y): return x-s/2,y-s/2
def moveBackwardRight(x,y): return x+s/2,y-s/2
#Dictionnary of movements
moves={'f':moveForward,'b':moveBackward,'l':moveLeft,'r':moveRight,'fl':moveForwardLeft,'fr':moveForwardRight,'bl':moveBackwardLeft,'br':moveBackwardRight}
#Store the possibles movements in a set
moveSet=set(list(moves.keys()))
#Move randomly 'steps' times
for step in range(1,steps+1):
    movement=random.sample(moveSet,1)[0]
    #get the new point according to the random movement
    newPoint=moves[movement](X[step-1],Y[step-1])
    X.append(newPoint[0])
    Y.append(newPoint[1])
plt.figure(figsize=(14,14))
#Plot all the points
plt.scatter(X,Y,marker=None,linewidths=0.5)
#Join all the points
plt.plot(X,Y,color='black')
#Plot the fist and last points for visualization
xlimits=[X[0],X[-1]]
ylimits=[Y[0],Y[-1]]
plt.scatter(xlimits,ylimits,marker='o',s=100,c='red')
#Finalize and show the graph
plt.title("2D Modified Random Walk with "+str(steps)+" steps")
plt.show()
#savefig('foo.pdf', bbox_inches='tight')