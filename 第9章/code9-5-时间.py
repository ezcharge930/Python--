import time
t = time.time()
print(t)  # 输出当前时间戳

t = time.localtime(t)
print(t)  # 输出当前时间的结构化表示
print(t.tm_year)

s = time.strftime('%Y-%m-%d %H:%M:%S',t)
print(s)  # 输出当前时间的字符串表示

from my_package import my_tools
print(my_tools.get_time())  # 使用自定义函数获取当前时间字符串