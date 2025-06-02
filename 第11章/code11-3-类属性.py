class Player(object):
    numbers = 0
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city
        Player.numbers += 1
        
