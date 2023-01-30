#To print from A TO B prime number (range)
a=1
b=30
for n in range(a,b+1):
    div=2 
    while div<=n-1:
        if n%div==0:
            break
        div=div+1
    if div==n:
            print(n)
            
            
            
def palidrome(a,b):
    for n in range(a,b+1):
        div=2
        while div<=n-1:
            if n%div==0:
                break
            div=div+1
        if n==div:
            print(n)
a=1
b=30
palidrome(a,b)