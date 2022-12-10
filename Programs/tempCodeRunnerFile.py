import math
import matplotlib.pyplot as plt
import locate
import random
import numpy as np
import re

A_std=[]
for i in range (6):
    A_std.append((50*math.cos(math.radians(60)*i),50*math.sin(math.radians(60)*i)))
    
def initialA():
    A=[(0,0),(50,0)]
    for i in range (2,5,1):
        x=50*i+random.randrange(-3,3)
        y=0
        A.append((x,y))

    for i in range (1,5,1):
        x=50*i*math.cos(math.radians(60))+random.randrange(-3,3)
        y=50*i*math.sin(math.radians(60))+random.randrange(-3,3)
        A.append((x,y))

    for i in range (1,4,1):
        x_1=A[5][0]
        y_1=A[5][1]
        x=x_1+50*i+random.randrange(-3,3)
        y=y_1+random.randrange(-3,3)
        A.append((x,y))

    for i in range (1,3,1):
        x_1=A[6][0]
        y_1=A[6][1]
        x=x_1+50*i+random.randrange(-3,3)
        y=y_1+random.randrange(-3,3)
        A.append((x,y))

    for i in range (1,2,1):
        x_1=A[7][0]
        y_1=A[7][1]
        x=x_1+50*i+random.randrange(-3,3)
        y=y_1+random.randrange(-3,3)
        A.append((x,y))
    
    return A

def showpoint(A):
    x_1, y_1 = [], []
    for i in range(len(A)):
        x_1.append(A[i][0])
        y_1.append(A[i][1])
    plt.scatter(x_1,y_1)

def correct(A_,ran,center,circle,start): 
    A_std=initial_A_std()
    for k in range(ran):
        if len(circle)<=2:
            break 
        for j in range(len(circle)):
            index = j+start
            index1 = j+start-1
            if index>=len(circle):
                index=index-len(circle)
            if index1>=len(circle):
                index1=index-len(circle)
            if index<-1:
                index+=len(circle)
            if index<-1:
                index1+=len(circle)
            for i in range(1, len(circle), 1):
                if i == index or i == index1:
                    continue
                tempA = locate.location(locate.getAngle(circle[index][0], circle[i][0], center),
                                        locate.getAngle(circle[index1][0], circle[i][0], center), A_std[index], A_std[index1])
                x_A = tempA[0]
                y_A = tempA[1]
                x_a = circle[i][0][0]
                x_std_a = A_std[i][0]
                y_std_a = A_std[i][1]
                y_a = circle[i][0][1]
                # A_[i] = ((-x_A + x_std_a) * alpha + x_a, y_a + (y_std_a - y_A) * alpha)
                circle[i]=(-x_A+x_std_a+x_a,y_a+y_std_a-y_A)
    for i in range (len(circle)):
        A_[[circle[i][2]]]=circle[i][1]
    x_1, y_1 = [], []
    for i in range(len(A)):
        x_1.append(A_[i][0])
        y_1.append(A_[i][1])
    plt.scatter(x_1,y_1)
    return circle

def initial_A_std():
    A_std=[]
    for i in range (6):
        A_std.append((5*math.cos(math.radians(60)*i),5*math.sin(math.radians(60)*i)))
    return A_std

def distant(p1,p2):
    s=math.sqrt(float((p1[0]-p2[0])**2+(p1[1]-p2[1])**2))
    return s

def findPoint(A,center):
    circle=[]
    for i in range(len(A)):
        if i==center:
            continue
        if(0<distant(A[i],A[center])<55):
            circle.append((A[i],i))
    return circle


A=initialA()
# showpoint(A)
circle = findPoint(A,5)
# showpoint(A_std)
correct(A,20,A[5],circle,0)
plt.show()