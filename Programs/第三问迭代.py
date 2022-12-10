import csv
import numpy as np
import matplotlib.pyplot as plt
import locate
import math


# 进行样本点的布置
def initialA():
    A = [(100, 0), (98 * math.cos(math.radians(40.10)), 98 * math.sin(math.radians(40.10))),
         (112 * math.cos(math.radians(80.21)), 112 * math.sin(math.radians(80.21))),
         (105 * math.cos(math.radians(119.75)), 105 * math.sin(math.radians(119.75))),
         (98 * math.cos(math.radians(159.86)), 98 * math.sin(math.radians(159.86))),
         (112 * math.cos(math.radians(199.96)), 112 * math.sin(math.radians(199.96))),
         (105 * math.cos(math.radians(240.07)), 105 * math.sin(math.radians(240.07))),
         (98 * math.cos(math.radians(280.17)), 98 * math.sin(math.radians(280.17))),
         (112 * math.cos(math.radians(320.28)), 112 * math.sin(math.radians(320.28)))]
    return A


def initialA_std():
    A_std = []
    for i in range(9):
        A_std.append((100 * math.cos(math.radians(40) * i), 100 * math.sin(math.radians(40) * i)))
    return A_std


def correct(A_, alpha, ran):
    count = 0
    count1 = 0
    for k in range(ran):  # 设定迭代轮数
        writer.writerow(A_)
        for j in range(len(A_)):  # 一轮迭代
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
            for i in range(len(A)):
                plt.scatter(A[i][0], A[i][1], c='b', s=0.5)
            for i in range(len(A)):
                if locate.getAngle(A[i - 1], (0, 0), A[i]) - 40 < 1e-2:
                    count += 1
                if math.sqrt(A[i][0] ** 2 + A[i][1] ** 2) - math.sqrt(A[i - 1][0] ** 2 + A[i - 1][1] ** 2) < 1e-2:
                    count1 += 1
            if count == 9 and count1 == 9:
                return;


A = initialA()
x_1, y_1 = [], []
for i in range(len(A)):
    x_1.append(A[i][0])
    y_1.append(A[i][1])
plt.plot(x_1, y_1, c='g', label="修正前")
A_std = initialA_std()
header = ["FY01", "FY02", "FY03", "FY04", "FY05", "FY06", "FY07", "FY08", "FY09"]
with open('point.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    correct(A, 0.5, 40)
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
print(aver)
theta = np.arange(0, 2 * np.pi, 0.01)
x = 0 + 100 * np.cos(theta)
y = 0 + 100 * np.sin(theta)
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.plot(x, y, c='r')
plt.plot(x_1, y_1, label="修正后")
plt.legend()
plt.tight_layout()
plt.show()
