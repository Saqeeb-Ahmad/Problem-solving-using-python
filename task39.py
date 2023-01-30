#prime factorization
n=786 
div=2
while div<=n:
    if n%div==0:
        n=n//div
        print(div,end=',')
        continue
    div=div+1



