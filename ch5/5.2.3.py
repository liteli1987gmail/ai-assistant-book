# 计算整数的阶乘（例如，5! = 5 × 4 × 3 × 2 × 1）
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # 输出：120

#计算一个数的斐波那契数列：每个数是前两个数之和（例如，F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)）。
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))  # 输出：5

# 使用一个循环变量和累积乘积的方式来计算阶乘值
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))  # 输出：120