class User(object):
    def __init__(self,name,age):
        self._name = name # 受保护的变量
        self.__age = age  # 私有变量
    
    def show_infos(self):
        print('大家好，我是%s,我今年%d'%(self._name,self.__age))


mia = User('mia',24)
# print(mia.name)
# print(mia.age)
# mia.name = 'Tom'
# mia.age= 25
# print(mia.name)
# print(mia.age)
mia.show_infos()




