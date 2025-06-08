class User(object):
    def __init__(self,name):
        print('__init__被调用')
        self.name = name