import random
# 随机小数
a = random.random()
print(a)

# 生成一个随机字母组成的列表
# a = []
# n = 5
# for i in range(20):
#     s = ''
#     for j in range(n):
#         t = random.randint(65, 90)
#         s += chr(t)
#     a.append(s)
    
from my_package import my_tools,my_games
print(my_tools.random_string(5))

list1 = [1, 2, 3, 4, 5]
random.shuffle(list1)
print(list1)

my_games.guess_number()