def myfunc(a,b,c,d,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    for e in args:
        print(e)
    for k,v in kwargs.items():
        print(str(k) + ' ---> ' + str(v))

myfunc(1,2,3,5,6,7,m=10,n=20,p=30)
    
