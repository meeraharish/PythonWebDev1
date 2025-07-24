class Mammal:
    def walk(self):
        print('walk')
class Dog(Mammal):
    def bark(self):
        print('bark')
class Cat(Mammal):
    def meow(self):
        print('meow')


d1=Dog()
d1.bark()
d1.walk()
c1=Cat()
c1.walk()
c1.meow()
