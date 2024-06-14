"""
定义一个函数，无论参数有多少个数字，
需要参数是整数和浮点数值类型，
都计算这些数字的平均值。
提供2个调用示例，
打印调用的结果

"""
def avg(*args):
    total = 0
    count = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            total += arg
            count += 1
    return total / count

print(avg(1, 2, 3, 4, 5))
print(avg(1.5, 2.5, 3.5, 4.5, 5.5))

