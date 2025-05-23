try:
    n = int(input('请输入一个数字:'))
    n = 5/n
    print(n)
except ZeroDivisionError as e:
    print('除数不能为0')
    print('原始报错信息',e)
except:
    print('请输入一个数字')
else:
    print('else模块') # 运行没有被except语句捕获时会执行else模块
finally:
    print('finally模块') # 无论如何都会执行finally模块