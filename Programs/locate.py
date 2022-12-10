import numpy as np
import math

def location(ang1, ang2, lau_point1, lau_point2):
    if ang1 < 180:
        lambda_1 = math.sqrt(1 / math.sin(math.radians(ang1)) ** 2 - 1)*(-1)
    elif 360> ang1 >180:
        lambda_1 = math.sqrt(1 / math.sin(math.radians(ang1)) ** 2 - 1)
    if ang2 < 180:
        lambda_2 = math.sqrt(1 / math.sin(math.radians(ang2)) ** 2 - 1)*(-1)
    elif 360> ang2 >180:
        lambda_2 = math.sqrt(1 / math.sin(math.radians(ang2)) ** 2 - 1)
    k_1 = lau_point2[0] - lau_point1[0] + lambda_1 * lau_point1[1] - lambda_2 * lau_point2[1]
    k_2 = lau_point1[1] - lau_point2[1] + lambda_1 * lau_point1[0] - lambda_2 * lau_point2[0]
    k = k_1 / k_2
    x_locate = (lau_point1[0] + lau_point1[1] * k - lambda_1 * lau_point1[1] + k * lambda_1 * lau_point1[0]) / (
            k**2 + 1)
    y_locate = k * x_locate
    return [x_locate, y_locate]


def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0]))
    if ang < 0:
        ang = ang + 360
    return ang

def swap(a, b):
    temp = a
    a = b
    b = temp
    return a,b
