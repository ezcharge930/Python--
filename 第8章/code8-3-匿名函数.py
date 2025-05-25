a = [1,2,3,4,5]

# def f(x):
#     return x ** 2

# result = map(f, a)
result = map(lambda x: x**2,a)

print(list(result)) # [1, 4, 9, 16, 25]

# reduce 累积
from functools import reduce
result = reduce(lambda x,y:x+y,a)
print(result) # 15

# filter 过滤
result = filter(lambda x:x%2,a)
print(list(result)) # [2, 4]

a = [1,2,3,40,5,6,0,6,0,5]
result = filter(lambda x: x!=0,a)
print(list(result)) # [1, 2, 3, 40, 5, 6, 6, 5]

result = reduce(lambda x,y:x*10**len(str(y))+y,a)
print(result) 