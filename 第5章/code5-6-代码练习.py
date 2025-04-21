# m行n列*号距阵
# m = 4
# n = 5
# for i in range(m):
#     print('*' * n)

# 打印出n行的等腰三角形
# n = 3
# for i in range(n):
#     print(' ' * (n - i - 1) + '*' * (2 * i + 1))

# 穷举
peach = 1  # 桃子数
while True:
    d1 = peach // 2 - 1 
    d2 = d1 // 2 - 1
    d3 = d2 // 2 - 1
    if d3 == 1:
        print("桃子数：", peach)
        break
    peach += 1

# 1. 计算1+2+3+...+100的和


