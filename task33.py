#to check the number is prime or not
n=5
i=2
while i<=n-1:
    if n%i==0:
        print('it is not prime:',n)
        break
    i=i+1
if i==n:
    print('it is a prime number',n)