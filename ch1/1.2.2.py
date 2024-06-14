
"""
定义函数 top_3_salespeople，
读取当前文件夹内的sales_data.csv文件，
返回按销售额降序排列的前三名员工信息。
"""
def top_3_salespeople():
    import csv
    with open('./sales_data.csv', 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        data = [row for row in reader]
    data = sorted(data, key=lambda x: float(x[1]), reverse=True)
    for i in range(3):
        print(f"{i+1}. {data[i][0]} - ${data[i][1]}")
        


"""

调用这个函数，打印销售额前三名员工的姓名和销售额。
"""
top_3_salespeople()




    


