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
# 在Python中，变量赋值和引用是如何工作的？举例展示:
"""
变量赋值是通过赋值运算符（=）来实现的。在 Python 中，变量是没有类型的，变量可以引用任何类型的对象。
示例：
a = 10
b = 20
c = a + b
print(c)  # 输出：30
"""

# 当将对象作为参数传递给函数时，Python是如何处理的？举例展示:
"""
当将对象作为参数传递给函数时，Python 会将对象的引用传递给函数，而不是对象的副本。
示例：
def add(a, b):
    return a + b

x = 10
y = 20
result = add(x, y)
print(result)  # 输出：30
"""

# 如何在函数内修改可变对象的内容？举例展示:
"""
在函数内修改可变对象的内容，可以通过引用传递的方式来实现。
示例：
def change_list(lst):
    lst.append(4)
    lst.append(5)

my_list = [1, 2, 3]
change_list(my_list)
print(my_list)  # 输出：[1, 2, 3, 4, 5]
"""

# 如何在函数内修改不可变对象的内容？举例展示:
"""
在函数内修改不可变对象的内容，可以通过返回新的对象来实现。
示例：
def change_string(s):
    s = s + " World"
    return s

my_string = "Hello"
new_string = change_string(my_string)
print(my_string)  # 输出：Hello
print(new_string)  # 输出：Hello World
"""
