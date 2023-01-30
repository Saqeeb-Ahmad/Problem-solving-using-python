def fibonacci(n):
    a=0
    b=1
    temp1=a
    temp2=b
    print(temp1)
    print(temp2)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
fibonacci(9)

##using recursion 
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
a=7
for i in range(a+1):
    print(fibonacci(i))
    