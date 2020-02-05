n1 = int(input('Enter a number: '))
n2 = int(input('Enter another number: '))

try:
    res = n1/n2

except Exception as E:
    print(E)
    print("0 not allowed as the divisor")
    '''
    except ZeroDivisionError:
        print("0 not allowed as the divisor")
    '''
else:
    print(res)
finally:
    print('All done!!')
