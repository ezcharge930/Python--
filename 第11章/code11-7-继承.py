class Player(object):
    numbers = 0
    levels = ['青铜', '白银', '黄金', '铂金', '钻石', '大师', '宗师', '王者']

    def __init__(self, name, age, city, level):
        self.name = name
        self.age = age
        self.city = city
        if level not in Player.levels:
            raise ValueError('等级错误')
        else:
            self.level = level
        Player.numbers += 1

            
    def show(self):
        print('我是这个游戏的第%s个游戏,名字是%s,今年%d岁,来自%s,我的段位是%s' % (Player.numbers, self.name, self.age, self.city, self.level))    
    
    def level_up(self):
        index1 = Player.levels.index(self.level)
        if index1 < len(Player.levels) - 1:
            self.level = Player.levels[index1 + 1]
            
    def get_weapon(self, weapon):
        self.weapon = weapon
        
    def show_weapon(self):
        return self.weapon.show_weapon()
    
    @classmethod
    def get_players(cls):
        print('本游戏的玩家数量已经达到%d' % cls.numbers)
        
    @staticmethod
    def isvalid(**kwargs):
        if kwargs['age'] > 18:
            return True
        else:
            return False
        
class VIP(Player):
    # 构造函数
    def __init__(self, name, age, city, level, coin):
        super().__init__(name, age, city, level)
        self.coin = coin
    def show(self):
        print('我是这个游戏的第%s个游戏,名字是%s,今年%d岁,来自%s,我的段位是%s, 我的余额是%d' % (Player.numbers, self.name, self.age, self.city, self.level, self.coin))    


class weapon(object):
    numbers = 0
    max_damage = 10000
    level = ['青铜', '白银', '黄金', '铂金', '钻石', '大师', '宗师', '王者']
    def __init__(self, name, damage, level):
        self.name = name
        self.damage = damage
        self.level = level
        weapon.numbers += 1
        if damage > weapon.max_damage:
            raise Exception('最大伤害值为10000,请重试')
        if level not in weapon.level:
            raise Exception('武器等级错误,请重试')
        
        def show_weapon(self):
            for k,v in self.weapon.__dict__.items():
                print(k,v)



mia = VIP('Mia', 18, '北京', '白银', 100)

# mia.level_up()
# mia.show()

print(type,mia)

print(isinstance(mia,Player))
print(isinstance(mia,VIP))

mia.show()