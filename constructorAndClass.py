class Point:
    def __init__(self,x=0,y=0): #constructor in python 
        #self references the object that called it
        self.x=x
        self.y=y
    def draw(self):
        print('draw')
    def paint(self):
        print('paint')


p1=Point(10,20) # here 10 and 20 passed to init method 
p1.draw()
print(p1.y)
p2=Point()
p2.paint()


#Exercise
# talk() and name 

class Person:
    def __init__(self,name='abc'):
        self.name=name
    def talk(self):
        print(self.name+' talking')
    


p1=Person('meera')
print(p1.name)

p1.talk()
p2=Person()
p2.talk()

