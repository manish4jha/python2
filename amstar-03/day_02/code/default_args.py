# Default arguments
# Keyword arguments

def printmsg(name, quote='Howdy!'):
    print('Hi!', name)
    print('-'*40)
    print(quote.upper())


print('\ncall #1')
printmsg('Ravi', 'How are you?')
print('\ncall #2')
printmsg('Anil')
print('\ncall #3')
printmsg('How are you?', 'Anil')
print('\ncall #4')
printmsg(quote='How are you?', name='Anil')
