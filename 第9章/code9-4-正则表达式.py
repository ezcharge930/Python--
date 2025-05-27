

# ids = input("请输入身份证号码：")
# # 位数18位
# if len(ids) == 18:
#     if ids[:-1].isdigit() and (ids[-1].isdigit() or ids[-1] == 'X'):
#         print("身份证号码格式正确")
#     else:
#         print("身份证号码格式错误")
# else:
#     print("身份证号码位数不正确")

# 检测字符串是否为纯数字的字符串
import re
result = re.match(r'\d+','123321234')
print(result)

# \w:数字字母下划线
result = re.match(r'\w+','a9*')
print(result)

# \s:空白字符 \S:非空白字符
result = re.match(r'\s+','   ')
print(result)

# .:任意字符
result = re.match(r'^code\d-\d-.+$','code9-3-re')
print(result)

# []区间,可选列表
# result = re.match(r'^[abcd]+$','abc')
result = re.match(r'^abc{2}','abcc')
print(result)

# | 或者
result = re.match(r'^a|b|c$','d')
print(result)

# 身份证号
result = re.match(r'^\d{6}((20[012][012345])|(19\d\d))d{7}[\dX]$','12345678901234567X')
print(result)

result = re.match(r'20[012][12345]','2001')
print(result)

from my_package import my_tools
print(my_tools.is_phone_number('12345678901'))
print(my_tools.is_id_number('12345678901234567X'))