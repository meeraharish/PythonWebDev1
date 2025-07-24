#mosh
num=[]

n=int(input('enter no of elements in list'))
print('enter the elements of the list ')
for i in range(n):
    num.append(int(input()))
largest=num[0]
for i in num:
   if largest<i:
       largest=i
print(f'largest = {largest}')

    