#mosh
#start stop quit 
action=''
started=True
while True:
    action=input("enter the option : 1. start 2.stop 3. quit")
    if action=='1':
        if started:
            print('car already started')
        else:  
            started=True
            print('car started ..ready to go! ')
        
        
    elif action=='2':
        if started:
            started=False
            print('car stopped')
        else:
            print('car already stopped')
    elif action=='3':
        print('quitting')
        break
    else:
        print('invalid input')
        
