# 定义一个计算圆面积的函数 `circle_area`

import math

def circle_area(radius):
    if type(radius) not in [int, float]:
        raise TypeError("The radius must be a non-negative real number.")
    if radius < 0:
        raise ValueError("The radius cannot be negative.")
    return math.pi * radius ** 2


