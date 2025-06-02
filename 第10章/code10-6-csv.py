import os,csv,random
from my_package import my_tools

lista = []
def random_info(n=100):
    subjects = ['python','java','c++','javascript','php']
    for i in range(n):
        name = my_tools.random_string(random.randint(3,6))
        subject = random.choice(subjects)
        score = random.randint(50,100)
        lista.append([name,subject,score])

def average():
    with open('data.csv', mode='r', encoding='utf-8') as f:
        cf = csv.reader(f)
        head = next(cf)  # 读取表头
        scores = []
        for i in cf:
            scores.append(int(i[2]))
        return sum(scores) / len(scores)

def make_datas():
    with open('data.csv', mode = 'a',encoding = 'utf-8', newline='') as f:
        cf = csv.writer(f)
        random_info()  # 调用函数生成数据
        cf.writerows(lista)  # 添加多行数据

make_datas()
result = average()
print('大家的平均分是：',result)