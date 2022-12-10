import numpy as np
import matplotlib.pyplot as plt
import locate
import math
import matplotlib as mp
mp.use('TkAgg')

# 进行样本点的布置
def initialA():
    A = [(100, 0)]
    A.append((98 * math.cos(math.radians(40.10)), 98 * math.sin(math.radians(40.10))))
    A.append((112 * math.cos(math.radians(80.21)), 112 * math.sin(math.radians(80.21))))
    A.append((105 * math.cos(math.radians(119.75)), 105 * math.sin(math.radians(119.75))))
    A.append((98 * math.cos(math.radians(159.86)), 98 * math.sin(math.radians(159.86))))
    A.append((112 * math.cos(math.radians(199.96)), 112 * math.sin(math.radians(199.96))))
    A.append((105 * math.cos(math.radians(240.07)), 105 * math.sin(math.radians(240.07))))
    A.append((98 * math.cos(math.radians(280.17)), 98 * math.sin(math.radians(280.17))))
    A.append((112 * math.cos(math.radians(320.28)), 112 * math.sin(math.radians(320.28))))
    return A


A_std = []
for i in range(9):
    A_std.append((100 * math.cos(math.radians(40) * i), 100 * math.sin(math.radians(40) * i)))


# 迭代过程函数
def correct(A, alpha, ran):
    for k in range(ran):
        for j in range(len(A)):
            index = j
            index1 = j - 1
            for i in range(1, len(A), 1):
                if i == index or i == index1:
                    continue
                tempA = locate.location(locate.getAngle(A[index], A[i], (0, 0)),
                                        locate.getAngle(A[index1], A[i], (0, 0)), A_std[index], A_std[index1])
                x_A = tempA[0]
                y_A = tempA[1]
                x_a = A[i][0]
                x_std_a = A_std[i][0]
                y_std_a = A_std[i][1]
                y_a = A[i][1]
                A[i] = ((-x_A + x_std_a) * alpha + x_a, y_a + (y_std_a - y_A) * alpha)
    x_1, y_1, x_std, y_std = [], [], [], []
    sum = 0
    for i in range(len(A)):
        x_1.append(A[i][0])
        x_std.append(A_std[i][0])
        y_std.append(A_std[i][1])
        y_1.append(A[i][1])
        s = 0.5 * ((x_1[i] - x_std[i]) ** 2 + (y_1[i] - y_std[i]) ** 2)
        sum = sum + s
    aver = math.sqrt(sum / len(A))
    print("alpha=", alpha, "range=", ran, "时各点标准差平均为", aver)
    return ran,aver

ax1=plt.subplot(111)
ax2=plt.subplot(111)
ax3=plt.subplot(111)
ax4=plt.subplot(111)
ax5=plt.subplot(111)
ax6=plt.subplot(111)
ax7=plt.subplot(111)
ax8=plt.subplot(111)
ax9=plt.subplot(111)
ax10=plt.subplot(111)

ax=[None,ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8,ax9,ax10]

for alpha_i in range(1,10,1):
    a1=[]
    b1=[]
    for ran_i in range(1,5,1):
        A=initialA()
        x1,y1=correct(A, 0.1*alpha_i, ran_i*10)
        a1.append(x1)
        b1.append(y1)
    ax[alpha_i].step(a1, b1, linewidth=1,label="alpha="+str(alpha_i/10))
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号
plt.xlabel("迭代次数（N）",loc='center')
plt.ylabel("适应度（S）",loc='center',rotation=90)    
plt.legend()
plt.subplots_adjust()
plt.show()


