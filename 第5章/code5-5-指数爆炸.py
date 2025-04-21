# # 纸的厚度
# n = 0.1
# w = n
# for i in range(50):
#     w *= 2
#     print("第", i + 1, "次折叠，纸的厚度为：", w, "cm")

# # 纸的厚度为0.1cm，折叠50次后，纸的厚度为：1125899906842624.0cm

# 国王麦粒
g = 1   # 当前格麦粒数
total = 0   # 总数
a = 1 # 棋盘格数
while a <= 10: # 计算前10格的麦粒数
    total += g
    print("国王在第", a, "格时，麦粒总数为：", total, "粒")
    g *= 2
    a += 1

# 人生的复利
day = 0 # 天数
total = 1 # 总数
while day < 30: # 计算前30天的复利
    total = total * 1.01
    print(total)
    day += 1
