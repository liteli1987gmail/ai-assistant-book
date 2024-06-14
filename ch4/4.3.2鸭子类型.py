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

# 什么是Python中的鸭子类型？举例展示：
"""
鸭子类型是一种动态类型的风格，是 Python 是动态类型语言的一个重要体现。
鸭子类型是指在动态类型语言中，不要求对象是特定的类型，而是关注对象是否有特定的方法、属性或行为。
示例：
class Duck:
    def quack(self):
        print('Quack, quack')

class Person:
    def quack(self):
        print('I am quacking like a duck')

def in_the_forest(duck):
    duck.quack()

duck = Duck()
person = Person()
in_the_forest(duck)  # 输出：Quack, quack
in_the_forest(person)  # 输出：I am quacking like a duck
"""

class Duck:
    def quack(self):
        print('Quack, quack')

class Person:
    def quack(self):
        print('I am quacking like a duck')

def in_the_forest(duck):
    duck.quack()

duck = Duck()
person = Person()
in_the_forest(duck)  # 输出：Quack, quack
in_the_forest(person)  # 输出：I am quacking like a duck

# 如何判断一个对象是否是可迭代的？举例展示：
"""
使用 isinstance 函数判断一个对象是否是可迭代的。
示例：
from collections.abc import Iterable

print(isinstance([], Iterable))  # 输出：True
print(isinstance({}, Iterable))  # 输出：True
print(isinstance((), Iterable))  # 输出：True
print(isinstance('', Iterable))  # 输出：True
print(isinstance(1, Iterable))  # 输出：False
"""

# 如何编写可以接受多种输入类型的函数？举例展示：
"""
可以使用鸭子类型来编写可以接受多种输入类型的函数。
示例：
def add(a, b):
    return a + b

print(add(10, 20))  # 输出：30
print(add('hello', 'world'))  # 输出：helloworld
"""
