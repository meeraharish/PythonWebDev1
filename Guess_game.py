#mosh
import random

secret_number=random.randint(1,3)
guess_limit=3
guess_count=0
while guess_count<guess_limit:
    num=int(input('enter a number '))
    guess_count+=1
    if num==secret_number:
        print('you won!')
        break

else:
    print('the number is '+ str(secret_number))
    print('you failed !')
