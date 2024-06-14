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
# Python中的动态引用是如何工作的？举例展示:
"""
# 请使用代码案例说明 Python 中的动态引用。
# Python 中的变量是没有类型的，变量可以引用任何类型的对象。
# 示例：
a = 10
print(a)  # 输出：10
a = 'hello'
print(a)  # 输出：hello
"""
a = 10
print(a)  # 输出：10
a = 'hello'
print(a)  # 输出：hello

# 什么是强类型化语言？Python如何体现强类型化？举例展示:
"""
# 请使用代码案例说明 Python 中的强类型化。
# 强类型化语言是指变量的类型是固定的，不能随意改变。
# Python 是强类型化语言，例如不能将字符串和数字相加。
# 示例：
a = 10
b = 'hello'
c = a + b  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""
a = 10
b = 'hello'
c = a + b  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 如何使用isinstance函数检查对象类型？举例展示:
"""
# 请使用代码案例说明 Python 中如何使用 isinstance 函数检查对象类型。
# isinstance 函数用于检查对象是否是指定的类型。
# 示例：
a = 10
b = 'hello'
print(isinstance(a, int))  # 输出：True
print(isinstance(b, str))  # 输出：True
"""

a = 10
b = 'hello'
print(isinstance(a, int))  # 输出：True
print(isinstance(b, str))  # 输出：True






