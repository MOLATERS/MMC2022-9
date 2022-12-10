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


def judge1(A, b, o):
    flag = False
    for j in range(9):
        if j == o or j == 0:
            continue
        ang = getAngle(A[0], b, A[j])
        set = getAngle(A[0], A[o], A[j])
        if set - 10 < ang < set + 10:
            flag = True
        else:
            return False
    return flag


def judge2(A, b, o):
    flag = False
    for j in range(9):
        if j == o or j == 0:
            continue
        ang1 = getAngle(A[0], b, A[j])
        set1 = getAngle(A[0], A[o], A[j])
        for i in range(9):
            if i == j or i == 0 or i == o:
                continue
            ang2 = getAngle(A[0], b, A[i])
            set2 = getAngle(A[0], A[o], A[i])
            ang3 = getAngle(A[i], b, A[j])
            set3 = getAngle(A[i], A[o], A[j])
            if set1 - 10 < ang1 < set1 + 10 or set2 - 10 < ang2 < set2 + 10 or set3 - 10 < ang3 < set3 + 10:
                flag = True
            else:
                return False
    return flag

def show1(A, B, p):
    ret = []
    flag = True
    count = 0
    sum,score=0,0
    for i in range(ran):
        dertax = float(randrange(-x, x + 1) / 100)
        dertay = float(randrange(-x, x + 1) / 100)
        if dertax ** 2 + dertay ** 2 <= (x / 100) ** 2:
            B = (A[p][0] + dertax, A[p][1] + dertay)
            flag = judge1(A, B, p)
            if flag:
                # ax3.scatter(B[0], B[1], c='b', s=0.5, marker='x')
                score += math.exp(-(dertax ** 2 + dertay ** 2) / 2)
                count += 1
                if (count %10==0):
                    ret.append((count, float(score / sum)))
            # else:
            #     ax3.scatter(B[0], B[1], c='r', s=0.5, marker='x')
            sum+=math.exp(-(dertax ** 2 + dertay ** 2) / 2)
        else:
            i -= 1
    print("第", (p + 1), "架飞机的非误差占比:", float(score / sum))
    return ret


def show2(A, B, p):
    ret = []
    flag = True
    count = 0
    score=0
    sum=0
    for i in range(ran):
        dertax = float(randrange(-x, x + 1) / 100)
        dertay = float(randrange(-x, x + 1) / 100)
        if dertax ** 2 + dertay ** 2 <= (x / 100) ** 2:
            B = (A[p][0] + dertax, A[p][1] + dertay)
            flag = judge2(A, B, p)
            if flag:
                # ax4.scatter(B[0], B[1], c='b', s=0.5, marker='x')
                count += 1
                score += math.exp(-(dertax ** 2 + dertay ** 2) / 2)
                if (count%10==0):
                    ret.append((count, float(score/sum)))
            # else:
            #     ax4.scatter(B[0], B[1], c='r', s=0.5, marker='x')
            sum+=math.exp(-(dertax ** 2 + dertay ** 2) / 2)
        else:
            i -= 1
    print("第", (p + 1), "架飞机的非误差占比:", float(score / sum))
    return ret


A = []
for i in range(9):
    A.append((10 * math.cos(math.radians(40) * i), 10 * math.sin(math.radians(40) * i)))

ran = 10000
x = 250
B = (0, 0)
for i in range (1,9,1):
    num=i
    index_1, index_2, x_1, x_2, y_1, y_2 = [], [], [], [], [], []
    index_1 = show1(A, B, num)
    index_2 = show2(A, B, num)

    plt.rcParams['font.sans-serif']=['SimHei']
    plt.title=("FY0"+str(num)+"定位准确率对比")
    plt.xlabel("模拟次数(N)",loc='center')
    plt.ylabel("概率(P)",loc='center',rotation=90)

    for i in range(min(len(index_1),len(index_2))):
        x_1.append(index_1[i][0])
        x_2.append(index_2[i][0])
        y_1.append(index_1[i][1])
        y_2.append(index_2[i][1])

# plt.xlim(-0.5,max(x_2),10)
# plt.ylim(0,1,10/max(x_2))
    ax1=plt.subplot(1,1,1)
    ax2=plt.subplot(1,1,1)
    plt.rcParams['axes.unicode_minus']=False
    ax1.set_title("FY0"+str(num+1)+"定位准确率对比")
    ax1.set_xlim(-0.5,max(x_2),10)
    ax1.set_ylim(0.0,0.7,10/max(x_2))
    ax2.set_xlabel("模拟次数(N)",loc='center')
    ax1.plot(x_1, y_1, c='r',linewidth=1,label='三机概率')
    ax2.set_xlim(-0.5,max(x_2),10)
    ax2.set_ylim(0.0,1.0,10/max(x_2))
    ax2.plot(x_2, y_2, c='b',linewidth=1,label='四机概率')
    plt.savefig("C:/Users/Slater/Desktop/2022年数学建模国赛/"+"FY"+str(num+1)+".png")
    plt.legend()
    plt.subplots_adjust
    plt.show()
