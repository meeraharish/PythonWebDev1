#mosh
#remove duplicates in a list

num=[1,2,3,2,4,4,5]
uniques=[]
for i in num:
    if i not in uniques:
        uniques.append(i)
print(uniques)
print('...........................')
#remove consecutive duplicates in a list
num=[1,2,2,2,3,2,2,4,4,5,1]
uniques=[]
for i in num:
    if len(uniques)==0 or i!=uniques[-1]:
        uniques.append(i)
print(uniques)