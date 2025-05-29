# 打开文件
import os 
path = os.getcwd()  # 获取当前工作目录
filename = path + r'\第10章\test3.txt'

f = open(filename, mode = 'a', encoding='utf-8')  # 以追加模式打开文件

f.write('hello\n')
a = ['hello', 'world']
f.writelines(a)  # 将列表中的内容写入文件

f.close()  # 关闭文件