"""
定义一个计数器函数，
使用全局变量counter初始化为0，
定义一个更新计数器的函数update_counter，
函数里面使用global 关键字，更新全局变量counter。
调用update_counter，
打印现在的计数数字。

"""

counter = 0

def update_counter():
    global counter
    counter += 1

update_counter()
print(counter)  # 输出：1


