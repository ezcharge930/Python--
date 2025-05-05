score  = [80,70,60,80,70,60,40]
s = set(score) # 集合去重
print(s) # {40, 60, 70, 80}
d = {}

# 统计各个分数都有几个学生
for i in s:
    t = score.count(i) # 统计分数为i的学生人数
    d[i] = t # 将分数和人数存入字典
for k,v in d.items():
    print("得分为%d的学生有%d个人" %(k,v))