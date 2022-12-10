import matplotlib.pyplot as plt
import numpy as np
import math
from random import randrange
import matplotlib as mp
mp.use("TkAgg")


def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0]))
    if 0 <= ang <= 180:
        ang = ang
    elif 180 <= ang <= 360:
        ang = 360 - ang
    elif ang < 0:
        ang = ang + 180
    return ang


def getindex(a, A):
    for i in range(9):
        if (a == A[i]):
            return i


def judge(A, b, o):
    flag = False
    for j in range(9):
        if j == o or j==0:
             continue
        for i in range(9):
            if i==j or i==0 or i==o:
                continue
            ang1 = getAngle(A[0], b, A[j])
            set1 = getAngle(A[0], A[o], A[j])
            ang2 = getAngle(A[0], b, A[i])
            set2 = getAngle(A[0], A[o], A[i])
            ang3 = getAngle(A[i], b, A[j])
            set3 = getAngle(A[i], A[o], A[j])
            if set1 - 10 < ang1 < set1 + 10 or set2 - 10 < ang2 < set2 + 10 or set3-10 < ang3 < set3 +10:
                flag = True
            else:
                return False
    return flag


def show(A,B,p):
    ret=[]
    flag = True
    count=0
    for i in range(ran):
        dertax=float(randrange(-x, x + 1) / 100)
        dertay=float(randrange(-x, x + 1) / 100)
        if dertax**2+dertay**2<=(x/100)**2 :
            B = (A[p][0] +dertax, A[p][1] + dertay)
            flag = judge(A, B, p)
            if flag:
                plt.scatter(B[0], B[1], c='b', s=0.5, marker='x')
                count+=1
                if(count//10):
                    ret.append((i,float(count/i)))
            else:
                plt.scatter(B[0], B[1], c='r', s=0.5, marker='x')
        else:
            i-=1
    print("第",(p+1),"架飞机的非误差占比:",float(count/ran))
    return ret


A = []
for i in range(9):
    A.append((10 * math.cos(math.radians(40) * i), 10 * math.sin(math.radians(40) * i)))            
x_major_locator=plt.MultipleLocator(5)
y_major_locator=plt.MultipleLocator(5)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)
plt.xlim(-12.5,12)
plt.ylim(-12.5,12)
plt.rcParams['axes.unicode_minus']=False
plt.rcParams['font.sans-serif']=['SimHei']
plt.title("使用四个点进行定位的有效点分布")
ran=1000
x = 200
B = (0, 0)
index1,index2,index3,index4=[],[],[],[]
for i in range (0,9,1):
    if(i==1):
        index1=show(A,B,i)
        continue
    if(i==2):
        index2=show(A,B,i)
        continue
    if(i==3):
        index3=show(A,B,i)
        continue
    if(i==4):
        index4=show(A,B,i)
        continue
    show(A,B,i)
for i in range (ran//10):
    plt.scatter(index4[i][0],index4[i][1],c='b',s=0.5)
for i in range(9):
    plt.scatter(A[i][0], A[i][1], c='g', s=1.0)
plt.savefig('2.png')
plt.show()