while True:
    a=int(input('enter the number'))
    t=0
    s=0
    b=a 
    c=a
    while a!=0:
        t+=1
        a=int(a/10)
    n=t
    while b!=0:
        r=b%10
        s+=r*pow(10,t-1)
        t-=1
        b=int(b/10)
    if c==s and n==3:
        print('this number is both 3 digits and equal to its reverse')
    elif c==s and n!=3:
        print('this number is just equal to its reverse')
    elif c!=s and n==3:
        print('this number is just 3 digits')
    else :
        print('this number is neither 3 digits nor equal to its reverse ')
        


    
        
        
        
