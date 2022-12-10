import numpy as np
import matplotlib.pyplot as plt
import locate
import math
import matplotlib as mp
mp.use('TkAgg')

# 进行样本点的布置
A = [(100, 0)]
A.append((98 * math.cos(math.radians(40.10)), 98 * math.sin(math.radians(40.10))))
A.append((112 * math.cos(math.radians(80.21)), 112 * math.sin(math.radians(80.21))))
A.append((105 * math.cos(math.radians(119.75)), 105 * math.sin(math.radians(119.75))))
A.append((98 * math.cos(math.radians(159.86)), 98 * math.sin(math.radians(159.86))))
A.append((112 * math.cos(math.radians(199.96)), 112 * math.sin(math.radians(199.96))))
A.append((105 * math.cos(math.radians(240.07)), 105 * math.sin(math.radians(240.07))))
A.append((98 * math.cos(math.radians(280.17)), 98 * math.sin(math.radians(280.17))))
A.append((112 * math.cos(math.radians(320.28)), 112 * math.sin(math.radians(320.28))))
A_std = []
for i in range(9):
    A_std.append((100 * math.cos(math.radians(40) * i), 100 * math.sin(math.radians(40) * i)))


# 迭代过程函数
def correct(A, alpha, ran):
    count = 0
    count1 = 0
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
            # for i in range(len(A)):
            #     if np.isclose(locate.getAngle(A[i - 1], (0, 0), A[i]), 40):
            #         count += 1
            #     if np.isclose(math.sqrt(A[i][0] ** 2 + A[i][1] ** 2), math.sqrt(A[i - 1][0] ** 2 + A[i - 1][1] ** 2)):
            #         count1 += 1
            # if count == 9 and count1 == 9:
            #     return ;
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
    return (aver,ran)


for alpha_i in range(1,5,1):
    alpha = alpha_i * 0.2
    y_A = []
    x_A = []
    B = A
    ax=plt.subplot(1,1,1)
    for ran_i in range(5):
        ran = ran_i * 10
        y1,x1 = correct(B, alpha, ran)
        y_A.append(y1)
        x_A.append(x1)
    ax.step(x_A, y_A, label="alpha=" + str(alpha))
    plt.subplots_adjust()
plt.show()


