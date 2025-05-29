import os
path = os.getcwd()  # 获取当前工作目录
filename = path + r'\第10章\diary.txt'

def write_txt():
    date = input('请输入日期（格式：YYYY-MM-DD）：')
    text = input('请输入日记内容：')
    f = open(filename , mode='a', encoding='utf-8')  # 以追加模式打开文件
    f.write('ding\n')  # 写入日期和内容
    f.write(date+'\n')
    f.write(text+'\n')
    f.close()  # 关闭文件
    return True

def read_txt(day=-1):
    f = open(filename, mode='r', encoding='utf-8')  # 以读取模式打开文件
    context = f.read()
    f.close()  # 关闭文件
    if day != '-1':
        lista = context.split('ding\n')
        for i in lista:
            if i[:10] == day:
                print(i)
                return True
        return False
    else:
        context = context.replace('ding\n', '\n')  # 替换掉标记
        print(context)
    return True

def quit():
    print('退出日记本')

    
def menu():
    print('*' * 30)
    print('''
          打开日记本
          1、记录日记
          2、阅读日记
          3、退出''')
    print('*' * 30)
    
menu()

while True:
    op = input('请选择操作：')
    if op == '1':
        if write_txt():
            print('日记记录成功！')
    elif op == '2':
        day = input('请输入要阅读的日期（格式：YYYY-MM-DD），输入-1则阅读全部日记：')
        if read_txt(day):
            print('日记阅读成功！')
        else:
            print('没有找到该日期的日记！')
    elif op == '3':
        quit()
    else:
        print('输入错误，请重新输入！')