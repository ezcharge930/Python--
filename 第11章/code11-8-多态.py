class Animal(object):
    def speak(self):
        print('动物的叫声')
    
class Cat(Animal):
    def speak(self):
        print('喵喵')
        
class Dog(Animal):
    def speak(self):
        print('汪汪')
    
def speak(object):
    object.speak()

animal = Animal()

animal.speak()

speak(animal)
        
        
kitty = Cat()

puppy = Dog()

speak(kitty)

speak(puppy)