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

# 什么是Python对象的属性和方法？举例展示:
"""
    Python 对象的属性是对象的特征，Python 对象的方法是对象的行为。
    Python 对象的属性和方法是通过点号（.）来访问的。
    示例：
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def say_hello(self):
            print(f'Hello, my name is {self.name}')

    person = Person('Alice', 20)
    print(person.name)  # 输出：Alice
    person.say_hello()  # 输出：Hello, my name is Alice
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Hello, my name is {self.name}')

person = Person('Alice', 20)
print(person.name)  # 输出：Alice
person.say_hello()  # 输出：Hello, my name is Alice

# 如何使用getattr函数访问对象的属性和方法？举例展示:
"""
    使用 getattr 函数可以访问对象的属性和方法。
    示例：
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def say_hello(self):
            print(f'Hello, my name is {self.name}')

    person = Person('Alice', 20)
    print(getattr(person, 'name'))  # 输出：Alice
    getattr(person, 'say_hello')()  # 输出：Hello, my name is Alice
"""

