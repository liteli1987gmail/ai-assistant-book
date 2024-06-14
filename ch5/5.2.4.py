# 一个使用map()函数的例子

def square(n):
    return n ** 2

numbers = [1, 2, 3, 4, 5]
squares = map(square, numbers)

print(list(squares))  # 输出：[1, 4, 9, 16, 25]

# 一个使用filter()函数的例子
def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_numbers = filter(is_even, numbers)

print(list(even_numbers))  # 输出：[2, 4]

# 一个使用lambda 函数的例子
numbers = [1, 2, 3, 4, 5]
squares = map(lambda x: x ** 2, numbers)

print(list(squares))  # 输出：[1, 4, 9, 16, 25]

# 一个使用高阶函数sort与匿名函数lambda的结合的例子
students = [('John', 'A', 15), ('Jane', 'B', 12), ('Dave', 'B', 10)]
students.sort(key=lambda s: s[2])  # 使用年龄排序

print(students)  # 输出：[('Dave', 'B', 10), ('Jane', 'B', 12), ('John', 'A', 15)]