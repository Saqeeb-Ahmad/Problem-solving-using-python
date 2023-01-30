#factorial usng loop
n=int(input('enter number:'))
result=1
for i in range(n,0,-1):
    result=result*i
print(result)


#usinf recurtion
def rec(n):
    if n==0:
        return 1
    return n*rec(n-1)

print(rec(n))