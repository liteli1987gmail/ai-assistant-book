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

# 如何在Python中调用函数？举例展示：
"""
函数是一组语句，用于执行特定的任务。在 Python 中，使用 def 关键字定义函数。
语法：
def 函数名(参数):
    代码块
示例：

def hello():
    print('Hello, World!')

hello()  # 输出：Hello, World!
"""

# Python中如何传递参数？举例展示：
"""
函数可以接受参数，参数是调用函数时传递给函数的值。在 Python 中，函数参数可以是必需的、关键字参数、默认参数和可变参数。
示例：

def hello(name):
    print('Hello, ' + name + '!')   

hello('World')  # 输出：Hello, World!

def hello(name='World'):
    print('Hello, ' + name + '!')

hello()  # 输出：Hello, World!

def hello(*names):
    for name in names:
        print('Hello, ' + name + '!')           

hello('World', 'Python')  # 输出：Hello, World! Hello, Python!

def hello(**names):
    for key, value in names.items():
        print(key + ': ' + value)

hello(name='World', language='Python')  # 输出：name: World language: Python
"""

# 什么是Python中的引用？举例展示：
"""
引用是一个对象的别名。在 Python 中，变量是引用，变量名是对象的别名。
示例：

a = 10
b = a
print(b)  # 输出：10
"""

