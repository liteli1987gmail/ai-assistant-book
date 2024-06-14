def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
factorial('5')

"""
当我们向 factorial 函数传递一个非整数值时，
它会抛出一个 TypeError。这是因为函数期望输入是一个整数，
但是它接收到了一个字符串。

我们可以在函数的开始处添加一个类型检查，
如果输入不是整数，就抛出一个友好的错误消息。
这样，用户就可以立即知道他们的输入是错误的，
而不是等到程序抛出一个难以理解的 TypeError。

请帮我在 factorial 函数中添加输入类型和值的检查，
确保函数只接受非负整数输入。
"""
def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

factorial(5)


