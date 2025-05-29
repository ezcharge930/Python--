import os,csv
path = os.getcwd()  # 获取当前工作目录
filename = path + r'\第10章\data.csv'
with open(filename, mode='r', encoding='utf-8') as f:
    cf = csv.reader(f)
    head = next(cf)  # 读取表头
    scores = []
    for i in cf:
        scores.append(int(i[2]))
    print('平均分：', sum(scores) / len(scores))