# def sum_2():
#     a = 1
#     b = 2 
#     print('a+b=', a+b)

# sum_2()

# def sum_2(a, b): # 形式参数
#     print('a=', a)
#     print('b=', b)
#     print('a+b=', a+b)

# sum_2(6,6) # 实际参数

# def sum_2(a, b): # 形式参数
#     return a + b

# result = sum_2(6, 6) # 实际参数
# print('result=', result)

# a = len('hello')

# def power(x, n):
#     return x ** n

# a = power(4,3)
# print('a=', a)

# def total(*args):
#     print(a)
#     result = 0
#     for i in a:
#         result += i
#     return result

# result = total(1, 2, 3, 4, 5)
# print('result=', result)

def f(**kwargs): # 可变参数，接收字典
    for k,v in kwargs.items():
        print(k, v)
d = {'name': 'zhangsan', 'age': 18}
f(**d) # 关键字参数，接收字典
    