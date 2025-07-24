#mosh
def emoji_converter(message):
    output=''
    l=message.split(' ')
    emojis={':)':'😊',':(':'😞'}
    
    for ch in l:
        output+= emojis.get(ch,ch)+' '
    return output
    


print('start')
message=input('enter the message')

op=emoji_converter(message)
print(op)
print('done')