"""
# 请使用代码案例说明 Python 中的标识符命名规则，以'''开始输出。
# 标识符可以是小写字母（a 到 z）或大写字母（A 到 Z）或数字（0 到 9）或下划线（_）的组合。
# 标识符不能以数字开头。
# 标识符是区分大小写的。
# 示例：

variable = 10
Variable = 20
print(variable)  # 输出：10
print(Variable)  # 输出：20

"""

# 如何调用Python中的函数？举例展示:
"""
    Python 中函数的调用方式是通过函数名后面跟着括号和参数列表来调用的。
    示例：
    def add(a, b):
        return a + b

    result = add(10, 20)
    print(result)  # 输出：30
"""

def add(a, b):
    return a + b
result = add(10, 20)
print(result)

# 什么是Python对象的方法？如何调用对象的方法？举例展示:
"""
    Python 对象的方法是与对象相关联的函数，对象的方法是通过对象名后面跟着点和方法名来调用的。
    示例：
    class Person:
        def __init__(self, name):
            self.name = name

        def say_hello(self):
            print('Hello, ' + self.name)

    p = Person('Alice')
    p.say_hello()  # 输出：Hello, Alice
"""

class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print('Hello, ' + self.name)

p = Person('Alice')
p.say_hello()  # 输出：Hello, Alice


# 函数参数可以是位置参数和关键词参数，它们如何使用？举例展示:
"""
    函数参数可以是位置参数和关键词参数，位置参数是按照参数的位置传递的，关键词参数是按照参数的名称传递的。
    示例：
    def add(a, b):
        return a + b

    result = add(a=10, b=20)
    print(result)  # 输出：30
"""

def add(a, b):
    return a + b
result = add(a=10, b=20)
print(result)

# 什么是Python中的默认参数？如何使用默认参数？举例展示:
"""
    默认参数是在定义函数时给参数指定一个默认值，调用函数时如果没有传递参数，则使用默认值。
    示例：
    def add(a, b=10):
        return a + b

    result = add(20)
    print(result)  # 输出：30
"""

def add(a, b=10):
    return a + b
result = add(20)
print(result)

# 什么是Python中的可变参数？如何使用可变参数？举例展示:
"""
    可变参数是指函数的参数个数是可变的，可以接受任意数量的参数。
    示例：
    def add(*args):
        result = 0
        for arg in args:
            result += arg
        return result

    result = add(10, 20, 30)
    print(result)  # 输出：60
"""

def add(*args):
    result = 0
    for arg in args:
        result += arg
    return result
result = add(10, 20, 30)
print(result)




