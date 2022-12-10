import math
from random import randrange

import matplotlib as mp
import matplotlib.pyplot as plt

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


A = []
for i in range(9):
    A.append((5 * math.cos(math.radians(40) * i), 5 * math.sin(math.radians(40) * i)))


def getindex(a, A):
    for i in range(9):
        if (a == A[i]):
            return i


def judge(A, b, o):
    flag = False
    for i in range(9):
        if i == o:
            continue
        for j in range(9):
            if j == o:
                continue
            ang = getAngle(A[i], b, A[j])
            set = getAngle(A[i], A[o], A[j])
            if set - 10 < ang < set + 10:
                flag = True
            else:
                return False
    return flag


ax1 = plt.subplot(2, 2, (1, 4))
x = 200
B = (0, 0)
flag = True
p=0
for i in range(10000):
        B = (A[p][0] + float(randrange(-x, x + 1) / 100), A[p][1] + float(randrange(-x, x + 1) / 100))
        flag = judge(A, B, p)
        if flag:
            plt.scatter(B[0], B[1], c='b', s=0.5, marker='x')
p+=1
for i in range(10000):
        B = (A[p][0] + float(randrange(-x, x + 1) / 100), A[p][1] + float(randrange(-x, x + 1) / 100))
        flag = judge(A, B, p)
        if flag:
            plt.scatter(B[0], B[1], c='r', s=0.5, marker='x')
p+=1
for i in range(10000):
        B = (A[p][0] + float(randrange(-x, x + 1) / 100), A[p][1] + float(randrange(-x, x + 1) / 100))
        flag = judge(A, B, p)
        if flag:
            plt.scatter(B[0], B[1], c='b', s=0.5, marker='x')
p+=1
for i in range(10000):
        B = (A[p][0] + float(randrange(-x, x + 1) / 100), A[p][1] + float(randrange(-x, x + 1) / 100))
        flag = judge(A, B, p)
        if flag:
            plt.scatter(B[0], B[1], c='r', s=0.5, marker='x')
p+=1
for i in range(10000):
        B = (A[p][0] + float(randrange(-x, x + 1) / 100), A[p][1] + float(randrange(-x, x + 1) / 100))
        flag = judge(A, B, p)
        if flag:
            plt.scatter(B[0], B[1], c='b', s=0.5, marker='x')
p+=1
for i in range(10000):
        B = (A[p][0] + float(randrange(-x, x + 1) / 100), A[p][1] + float(randrange(-x, x + 1) / 100))
        flag = judge(A, B, p)
        if flag:
            plt.scatter(B[0], B[1], c='r', s=0.5, marker='x')
p+=1
for i in range(10000):
        B = (A[p][0] + float(randrange(-x, x + 1) / 100), A[p][1] + float(randrange(-x, x + 1) / 100))
        flag = judge(A, B, p)
        if flag:
            plt.scatter(B[0], B[1], c='b', s=0.5, marker='x')
p+=1
for i in range(10000):
        B = (A[p][0] + float(randrange(-x, x + 1) / 100), A[p][1] + float(randrange(-x, x + 1) / 100))
        flag = judge(A, B, p)
        if flag:
            plt.scatter(B[0], B[1], c='r', s=0.5, marker='x')
p+=1
for i in range(10000):
        B = (A[p][0] + float(randrange(-x, x + 1) / 100), A[p][1] + float(randrange(-x, x + 1) / 100))
        flag = judge(A, B, p)
        if flag:
            plt.scatter(B[0], B[1], c='y', s=0.5, marker='x')
p+=1
for i in range(9):
    plt.scatter(A[i][0], A[i][1], c='g', s=1.0)
plt.savefig('2.png')
plt.show()
