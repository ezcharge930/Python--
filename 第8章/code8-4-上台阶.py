# 10阶楼梯，每次上1次或者上2个台阶，问一共又多少种走法
# def f(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     return f(n-1) + f(n-2)
# # print(f(10))
# for i in range(10):
#     print('楼梯有', i, '阶，走法有', f(i), '种')

a = [0,1,2]
for i in range(3,11):
    a.append(a[i-1] + a[i-2])
    print('楼梯有', i, '阶，走法有', a[i], '种')