#mosh 
input_weight=float(input('Weight: '))
input_unit=input('(L)bs or (K)g: ')
if input_unit=='L' or input_unit=='l':
    kg=input_weight*0.45
    print(f'you are {kg} kgs')
elif input_unit=='K' or input_unit=='k':
    pounds=input_weight/0.45
    print(f'you are {pounds} pounds ')
