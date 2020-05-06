try:
    f = open(r"C:\Users\Purushotham\Desktop\oracle\day_03\code\next\read\test.txt", "r")
    a = 10
    b = a / 2
    s = '123' + 10
except ZeroDivisionError:
    print('You cannot divide by zero')
except FileNotFoundError:
    print('File not found!')
except Exception as E:
    print('Unknown Exception!')
    print(E)
else:
    print(f.read())
    f.close()
    print(a, b)
finally:
    print('Thank you!')
    

    


