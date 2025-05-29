import os 
# 打开文件
path = os.getcwd()  # 获取当前工作目录
filename = path + r'\第10章\test2.txt'
f = open(filename, mode= 'w', encoding='utf-8')
f.write('hello\n')
f.write('world\n')
context = ['hello','world']
for i in context:
    f.write(i + '\n')

f = open(filename, mode = 'r', encoding='utf-8')
context = f.read()
print(context)
f.close()