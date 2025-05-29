import os
path = os.getcwd()  # 获取当前工作目录
path1 = path + r'\第10章'

with open(path1 + r'\test.txt', mode='r', encoding='utf-8') as f:  # 以追加模式打开文件
    context = f.read()
    print(context)  # 读取文件内容并打印
print('文件读取成功！')