import random
class Dice:
    def roll(self):
        x=random.randint(1,6)
        y=random.randint(1,6)
        t=(x,y)
        print(t)

d1=Dice()
d1.roll()


s='apple a day keeps a doctor away '
l=s.split(' ')
print(l)

l=[1,2,3,4]
str1=''.join(str(i) for i in l)
print(str1)
n=int(str1)
m=n+1

str2=str(m)
print(str2)
l1=list(str2)
print(l1)