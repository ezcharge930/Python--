class Player(object):
    def __init__(self,name,age,city): # 初始化方法
        self.name = name  # 实例属性
        self.age = age
        self.city = city

mia = Player('mia', 18, 'beijing')  # 创建实例
print(mia.name,mia.age,mia.city)  # 访问实例属性

print(mia.__dict__)  # 查看实例的属性字典

class weapon(object):
    def __init__(self,name,damage,level):
        self.name = name
        self.damage = damage
        self.level = level
        
gun = weapon('magic',1000,3)
print(gun.__dict__)