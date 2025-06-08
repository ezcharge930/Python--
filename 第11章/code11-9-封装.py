class User(object):
    def __init__(self,name,age):
        self._name = name # 受保护的变量
        self.__age = age  # 私有变量
    
    def show_infos(self):
        print('大家好，我是%s,我今年%d'%(self._name,self.__age))
        
    @property # 获取变量
    def age(self):
        return self.__age
    
    @age.setter # 变量的修改器
    def age(self,age):
        if isinstance(age,int):
            self.__age = age
        else:
            raise Exception('年龄只能是整数')

        




# mia = User('mia',24)
# # print(mia.name)
# # print(mia.age)
# # mia.name = 'Tom'
# # mia.age= 25
# # print(mia.name)
# # print(mia.age)
# mia.show_infos()
# print(mia.age)
# mia.age = 25
# print(mia.age)



class Player(object):
    numbers = 0
    levels = ['青铜', '白银', '黄金', '铂金', '钻石', '大师', '宗师', '王者']

    def __init__(self, name, age, city, level):
        self._name = name
        self._age = age
        self._city = city
        if level not in Player.levels:
            raise ValueError('等级错误')
        else:
            self.level = level
        Player.numbers += 1
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,age):
        if not isinstance(age,int):
            raise Exception('年龄必须是整数')
        if age<0 or age > 100:
            raise Exception('年龄必须在0-100之间')
        self._age = age
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if name == self._name:
            raise Exception('修改的名字与之前相同，请重试')
        else:
            self._name = name
        
    

            
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
        



mia = Player('Mia', 18, '北京', '白银')

print(mia.name)
mia.name = 'Tom'
print(mia.name)

print(mia.age)
mia.age =27
print(mia.age)

print(mia.__dict__)




