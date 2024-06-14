"""
首先，我们需要一个函数来输入学生的成绩。
这个函数可以接受一个学生的名字和他们的成绩，
然后将这些信息存储在一个字典中。
学生的名字将作为键，他们的成绩将作为值。
接下来，我们需要一个函数来计算学生的平均成绩。
这个函数应该接受上一步创建的字典作为输入，
然后遍历字典，将所有的成绩加起来，
然后除以成绩的数量，得到平均成绩。
最后，我们需要一个函数来输出结果。
这个函数应该接受平均成绩作为输入，
然后打印出一个消息，告诉我们学生的平均成绩是多少。

"""

def input_grades():
    grades = {}
    while True:
        name = input("Enter student name (or 'q' to quit): ")
        if name == 'q':
            break
        score = float(input("Enter student score: "))
        grades[name] = score
    return grades

def calculate_average(grades):
    total = sum(grades.values())
    average = total / len(grades)
    return average

def output_result(average):
    print("The average grade is:", average)

# Example usage:
grades = input_grades()
average_grade = calculate_average(grades)
output_result(average_grade)

