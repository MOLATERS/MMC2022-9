import numpy as np
import matplotlib.pyplot as plt
import locate
import math

def initialA():
    A = [(50, 0)]
    A.append((49 * math.cos(math.radians(60.10)), 49 * math.sin(math.radians(60.10))))
    A.append((56 * math.cos(math.radians(120.21)), 56 * math.sin(math.radians(120.21))))
    A.append((53 * math.cos(math.radians(180.75)),53 * math.sin(math.radians(180.75))))
    A.append((49 * math.cos(math.radians(239.86)),49 * math.sin(math.radians(239.86))))
    A.append((56 * math.cos(math.radians(299.96)),56 * math.sin(math.radians(299.96))))
    return A

def initial_A_std():
    A_std=[]
    for i in range (6):
        A_std.append((5*math.cos(math.radians(60)*i),5*math.sin(math.radians(60)*i)))
    return A_std

A_std=initial_A_std()

def correct(A_,alpha,ran):
    count = 0
    count1 = 0
    for k in range(ran):
        for j in range(len(A_)):
            index = j
            index1 = j - 1
            for i in range(1, len(A_), 1):
                if i == index or i == index1:
                    continue
                tempA = locate.location(locate.getAngle(A_[index], A_[i], (0, 0)),
                                        locate.getAngle(A_[index1], A_[i], (0, 0)), A_std[index], A_std[index1])
                x_A = tempA[0]
                y_A = tempA[1]
                x_a = A_[i][0]
                x_std_a = A_std[i][0]
                y_std_a = A_std[i][1]
                y_a = A_[i][1]
                A_[i] = ((-x_A + x_std_a) * alpha + x_a, y_a + (y_std_a - y_A) * alpha)
            for i in range(len(A_)):
                plt.scatter(A_[i][0], A_[i][1], c='b',s=0.5)
            for i in range(len(A_)):
                if locate.getAngle(A_[i - 1], (0, 0), A_[i])- 40<1e-2:
                    count += 1
                if math.sqrt(A_[i][0] ** 2 + A[i][1] ** 2) - math.sqrt(A_[i - 1][0] ** 2 + A_[i - 1][1] ** 2)<1e-2:
                    count1 += 1
            if count == 9 and count1 == 9:
                return;
A=initialA()
x_1, y_1 = [], []
for i in range(len(A)):
    x_1.append(A[i][0])
    y_1.append(A[i][1])
plt.plot(x_1,y_1,c='g',label="修正前")
correct(A,0.5,60)
x_1, y_1, x_std, y_std = [], [], [], []
sum = 0
for i in range(len(A)):
    x_1.append(A[i][0])
    x_std.append(A_std[i][0])
    y_std.append(A_std[i][1])
    y_1.append(A[i][1])
    s = 0.5 * ((x_1[i] - 10*x_std[i]) ** 2 + (y_1[i] - 10*y_std[i]) ** 2)
    sum = sum + s
aver = math.sqrt(sum / len(A))
print(aver)
theta = np.arange(0, 2*np.pi, 0.01)
x = 0 + 50 * np.cos(theta)
y = 0 + 50 * np.sin(theta)
plt.rcParams['axes.unicode_minus']=False 
plt.rcParams['font.sans-serif']=['SimHei']
plt.plot(x, y,c='r')
x_1.append(x_1[-1])
y_1.append(y_1[-1])
plt.plot(x_1,y_1,label="修正后")
plt.legend()
plt.tight_layout()
plt.show()