# #to reverse a number without including 0
# n=1234560
# ans=0
# while n!=0:
#     last_digit=n%10
#     ans=ans*10+last_digit
#     n=n//10
# print(ans)

# # to reverse a number with including 0
n=1234567
digit=0
while n>0:
    digit=n%10
    print(digit,end='')
    n=n//10

    
 