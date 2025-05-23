while True:
    try:
        op = input('请输入一个四则运算算是(例如1+2):')
        if '+' in op:
            a = op.split('+')
            result = int(a[0]) + int(a[1])
            print('结果是:', result)
        elif '-' in op:
            a = op.split('-')
            result = int(a[0]) - int(a[1])
            print('结果是:', result)
        elif '*' in op:
            a = op.split('*')
            result = int(a[0]) * int(a[1])
            print('结果是:', result)
        elif '/' in op:
            a = op.split('/')
            result = int(a[0]) / int(a[1])
            print('结果是:', result)
        elif op == 'C':
            print('退出计算器')
            break
        else:
            raise Exception('请按1+2的格式输入')
    except ZeroDivisionError:
        print('注意除法运算，除数不能为0')
    except Exception as e:
        print(e)

