import matplotlib.pyplot as plt
import locate
import random
import matplotlib as mp
import math
import numpy as np

mp.use("TkAgg")


def initialA():
    A = [(0, 0), (5, 0),(10,0)]

    for i in range(1, 3, 1):
        x = 5 * i * math.cos(math.radians(60))
        y = 5 * i * math.sin(math.radians(60))
        A.append((x, y))
    A.append((A[3][0]+5,A[3][1]))
    return A

def correct(a,A,derta):
    x=a[0]
    y=a[1]
    for i in range (5000):
        plt.scatter(a[0],a[1],c='b',s=1)
        # if a[0]<1e-3 and a[1]<1e-3 :
        #      break;
        # else:
        a1= locate.getAngle(A[4],a,A[5])
        b1= locate.getAngle(A[3],a,A[2])
        if 0< a1 < 180 and 180 < b1 < 360:
                 x=a[0]
                 y=a[1]
                 x-=random.randrange(1,10)/10*derta
                 y+=random.randrange(1,10)/10*derta
        if  180<a1< 360 and 0<b1<180:
                 x=a[0]
                 y=a[1]
                 x+=random.randrange(1,10)/10*derta
                 y-=random.randrange(1,10)/10*derta
        elif  180< a1< 360 or 180<b1<360:
                 x=a[0]
                 y=a[1]
                 x+=random.randrange(1,10)/10*derta
                 y+=random.randrange(1,10)/10*derta
        elif  0< a1 < 180 and 0<b1<180:
                 x=a[0]
                 y=a[1]
                 x-=random.randrange(1,10)/10*derta
                 y-=random.randrange(1,10)/10*derta
        a=(x,y)
    plt.scatter(x,y,c='g',s=10)
    s=math.sqrt(a[0]**2+a[1]**2)
    print("最后的适应度为：",s)
             


A=initialA()
for i in range(len(A)):
    plt.scatter(A[i][0],A[i][1])
a=(11,0)
plt.scatter(a[0],a[1],c='r',s=1)
correct(a,A,0.1)
plt.xlim(-1,15)
plt.ylim(-1,10)
plt.show()
