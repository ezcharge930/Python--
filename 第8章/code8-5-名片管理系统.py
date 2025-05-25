cards = [
        {'name': '小明', 'phone': '12345678901', 'qq': '123456789', 'email': '111'},
        {'name': '小红', 'phone': '12345678902', 'qq': '123456788', 'email': '222'},
        {'name': '小刚', 'phone': '12345678903', 'qq': '123456787', 'email': '333'},
        {'name': '小白', 'phone': '12345678904', 'qq': '123456786', 'email': '444'},
        {'name': '小黑', 'phone': '12345678905', 'qq': '123456785', 'email': '555'}]
# 名片管理系统
def menu():
    print('*'*30)
    print('''欢迎使用【名片管理系统】
    1. 新建名片
    2. 显示名片
    3. 查询名片
    0. 退出系统''')
    print('*'*30)

def new_card(name, phone, qq, email):
    user = {
        'name': name,
        'phone': phone,
        'qq': qq,
        'email': email
    }
    cards.append(user)
    return True

def show_card():
    for card in cards:
        print(card)

def modify_card(target_card):
    print("当前名片信息为：")
    print(target_card)
    print("请输入修改后的信息：")
    name = input("请输入姓名：")
    phone = input("请输入电话：")
    qq = input("请输入QQ:")
    email = input("请输入邮箱：")
    target_card['name'] = name
    target_card['phone'] = phone
    target_card['qq'] = qq
    target_card['email'] = email
    return True

def del_card(target_card):
    cards.remove(target_card)
    return True
    

def query_card(kw):
    for card in cards:
        for k, v in card.items():
            if kw ==v:
                return card
    return False

def quit():
    print("谢谢使用，再见！")


menu()
while True:
    op = input("请输入那你要操作的序号：")
    if op == '1':
        name = input("请输入姓名：")
        phone = input("请输入电话：")
        qq = input("请输入QQ:")
        email = input("请输入邮箱：")
        result = new_card(name, phone, qq, email)
        if result:
            print("名片添加成功！")
        else:
            print("名片添加失败！")
    elif op == '2':
        show_card()
    elif op == '3':
        kw = input("请输入要查询的关键词：")
        result = query_card(kw)
        if result:
            print("查询到的名片信息为：")
            print(result)
            op2 = input('输入4修改名片，输入5删除名片')
            if op2 == '4':
                modify_card(result)
                print("修改成功")
            elif op2 == '5':
                result = del_card(result)
                print("删除成功")
        else:
            print("没有查询到相关信息")
    elif op == '0':
        quit()
        break
    else:
        print("输入错误，请重新输入")
