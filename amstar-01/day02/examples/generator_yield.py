def nextSquare():
    print('INitializing')
    i = 1; 
  
    # An Infinite loop to generate squares  
    while True:
        print('Before Yield')
        yield i*i
        print('After Yield')
        i += 1  # Next execution resumes  
                # from this point      
  
# Driver code to test above generator  
# function

# GEN = nextSquare()

'''
print('Run 1')
for num in GEN:
    if num > 100:
        break
    print(num) 


print('Run 2')
for num in GEN: 
    if num > 1000: 
         break    
    print(num)
'''

print('Run 1')
for num in nextSquare():
    if num > 100:
        break
    print(num) 


print('Run 2')
for num in nextSquare(): 
    if num > 1000: 
         break    
    print(num)
