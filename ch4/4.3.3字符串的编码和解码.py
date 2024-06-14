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

# 什么是字节和Unicode？举例展示:
"""
# 请使用代码案例说明 Python 中的字节和 Unicode。
# 字节是 Python 中的数据类型，表示一个字节的数据。
# Unicode 是 Python 中的数据类型，表示一个 Unicode 字符。
# 示例：

# 字节
b = b'hello'

# Unicode
u = 'hello'
"""

# 如何将字符串编码为UTF-8？举例展示:
"""
# 请使用代码案例说明如何将字符串编码为 UTF-8。
# 使用 encode 方法将字符串编码为 UTF-8。
# 示例：

s = 'hello'

b = s.encode('utf-8')
print(b)  # 输出：b'hello'
"""

# 如何将字节解码为字符串？举例展示:
"""
# 请使用代码案例说明如何将字节解码为字符串。
# 使用 decode 方法将字节解码为字符串。
# 示例：

b = b'hello'

s = b.decode('utf-8')
print(s)  # 输出：hello
"""

# 读取本地包含中文的话，为什么要显式制指定编码格式？举例展示:
"""
# 请使用代码案例说明读取本地包含中文的话，为什么要显式指定编码格式。
# 读取本地文件时，需要显式指定编码格式，避免乱码。
# 示例：

with open('test.txt', 'r', encoding='utf-8') as f:
    s = f.read()
    print(s)
"""





