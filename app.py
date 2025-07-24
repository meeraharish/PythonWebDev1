#mosh
text ="harry potter and the sorcerer's stone"
print(text[-1])
print(text[1:-1])
print(text[-5]) # s
print(text[1:5]) #arry
text='''
hello pam,
how ar you doing ?
i AM OKAY .things are going by .

THnks
Meera 
'''
print(text)

#formatted text

apple='apfel'
banana='baum'
print(f'a for {apple} , b for {banana }')

print(10 ** 3)
print("m"*10)

price=1000000
good_credit=True
if good_credit:
    print("buyer has good credit ")
    price=0.1*price
else:
    print("they dont have good credit ")
    price=0.2*price
print(f'down payment is {price}')


name='meera'
if len(name)<3:
    print('name must be atleast 3 characters')
elif len(name)>50:
    print('name can be maximum of 50 characters')
else:
    print('name looks good! ')


num=[10,20,30]
sum=0
for i in num:
    sum=sum+i
print(sum)


for x in range(4):
    for y in range(3):
        print(str(x)+','+str(y))


num=[5,2,5,2,5,2,2]
for i in num:
    print('*'*i)




#tuple is immutable
#we cannot change a value ,add a value or remove a value from a tuple
t=(1,2,3,3,3,2,2,3,1)
# t[1]=5 we cannot change a value in a tuple
print(t.index(1))
print(t.count(3))
print(t)

#unpacking 
t=(3,4,5,6)
x,y,z,w=t #assigning 3 to x and so on 
print(x,y)

d1={'1':"one",'2':"two",'3':"three",'4':"four",'5':"five",'6':"six",'7':"seven",'8'
    :"eight",'9':"nine",'0':"zero"}
phone_number=input('enter phone number:')
p=list(phone_number)
for i in range(len(p)):
    print(d1.get(p[i],'!'))


d1={'1':'one','2':'two','3':'three','4':'four'}
phone=input('enter phone number: ')
value=''
for ch in phone:
    value+=d1.get(ch,'!')
print(value)


#functions
def greet(fname,lname):
    print('Hello '+fname+" "+lname)

print('Welcome ')
greet('meera','harish')
greet('kavya','ashok') #positional arguments
greet(lname='prasanna',fname='vibha') #keyword arguments

greet('prasanna','vibha')
greet('diya',lname='ajay')
