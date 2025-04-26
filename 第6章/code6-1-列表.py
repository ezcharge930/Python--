list1 = [] 

print(list1) # []

print(type(list1)) # <class 'list'>

list2 = [1, 2, 3, True]

print(list2) # [1, 2, 3, True]

list3 = []

print(list3) # []

list3 = list('hello')

print(list3) # ['h', 'e', 'l', 'l', 'o']

print(list3[4])

# 列表的遍历
for i in list3:
    print(i) # h e l l o

for i, j in enumerate(list3):
    print(i, j) # 0 h 1 e 2 l 3 l 4 o

# 列表的常用方法 变量.方法(参数)
list3.append('777') # 在列表末尾添加元素
print(list3) # ['h', 'e', 'l', 'l', 'o', '777']

list3.extend(['a', 'b', 'c']) # 在列表末尾添加多个元素
print(list3) # ['h', 'e', 'l', 'l', 'o', '777', 'a', 'b', 'c']

list3.insert(2, 'hello') # 在列表的指定位置添加元素
print(list3) # ['h', 'e', 'hello', 'l', 'l', 'o', '777', 'a', 'b', 'c']

list3.pop(3) 
print(list3) # ['h', 'e', 'hello', 'l', 'o', '777', 'a', 'b', 'c']

list3.remove('o')
print(list3) # ['h', 'e', 'hello', 'l', '777', 'a', 'b', 'c']

list3.append('hello')
print(list3) # ['h', 'e', 'hello', 'l', '777', 'a', 'b', 'c', 'hello']

list3.remove('hello') # 删除第一个hello
print(list3) # ['h', 'e', 'l', '777', 'a', 'b', 'c', 'hello']

list3.clear()
print(list3) # []

# 计算若干个人的平均年龄
age = [10,20,30,40,23,45]
total = 0 
for i in age:
    total += i
print(total/len(age)) # 28.333333333333332