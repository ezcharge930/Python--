import os

# 打开文件
path = os.getcwd()  # 获取当前工作目录
filename = path + r'\第10章\test.txt'
print(filename)

# D:\Python\Python学习\第10章\test.txt

f = open(filename, mode = 'r', encoding = 'utf-8')

# 读取文件
context = f.read()
print(context)

# 关闭文件
f.close()




