tuple1 = (1,2,3,True,'hello')

print(tuple1) # (1, 2, 3, True, 'hello')

print(type(tuple1)) # <class 'tuple'>
lsit1 = [1]

tuple2 = (1,)
print(tuple2) # 1

print(type(tuple2)) # <class 'int'>

# 元组的常用方法
a = tuple1.count('hello') # 1
print(a) # 1
print(tuple1)
a = tuple1.index(1)
print(a) # 1