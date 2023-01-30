#take N value form the user the print the sum from 1 to N
#using for loop
# n=int(input('enter n vlaue:'))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)

#using while loop
n=int(input('enter n value to sum them'))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
    
print(f'the sum of first {n} number is {sum}')