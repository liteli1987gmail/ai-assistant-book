# 计算圆面积的函数

import math
from math import pi

def circle_area(radius):
    return math.pi * radius ** 2

"""
对 `circle_area` 函数进行测试
定义一个 `test_circle_area` 函数,
考虑了各种可能的输入情况,
包括正常值、边界值、异常值等,
从不同角度测试了函数的行为是否符合预期。
在测试过程中，需要判断函数调用的报错类型，
每个测试语句需要根据测试结果打印相应的测试是否通过的提示，
提示的格式为："circle_area(0) == 0 raised ValueError"。
"""

def test_circle_area():
    assert circle_area(0) == 0, "Test failed"
    assert circle_area(1) == pi, "Test failed"
    assert circle_area(2) == 4 * pi, "Test failed"
    assert circle_area("2") == 4 * pi, "Test failed"

    try:
        circle_area(-1)
    except ValueError:
        print("Test passed")
    else:
        print("circle_area(-1) == 0 raised ValueError")
    try:
        circle_area(1 + 1j)
    except TypeError:
        print("Test passed")
    else:
        print("circle_area(1 + 1j) == 0 raised TypeError")




if __name__ == "__main__":
    test_circle_area()