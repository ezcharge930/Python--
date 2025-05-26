import random

def game1(): # 石头剪刀布
    player_score,computer_score = 0,0
    for i in range(3):
        player = input("请输入石头、剪刀或布：")
        computer = random.choice(['石头', '剪刀', '布'])
        print(f"计算机选择了：{computer}")
        if player == computer:
            player_score += 1
            computer_score += 1
        elif (player == '石头' and computer == '剪刀') or \
             (player == '剪刀' and computer == '布') or \
             (player == '布' and computer == '石头'):
             player_score += 1
        else:
            computer_score += 1
        print(f"当前得分 - 玩家: {player_score}, 计算机: {computer_score}")
    if player_score == computer_score:
        print("平局")
    elif player_score > computer_score:
        print("玩家获胜")
    else:
        print("计算机获胜")

def guess_number(start,end): # 猜数字
    number = random.randint(start,end)
    while True:
        player = int(input("猜一个1到100之间的数字："))
        if player == number:
            print("恭喜你，猜对了！")
            break
        elif player > number:
            print("猜大了")
        else:
            print("猜小了")
        