#For example, If the given int is 7536, the output shall be “6 3 5 7“, with
# a space 
# separating the digits.
# num=4321
# while num>0:
#     digit=num%10
#     num=num//10
#     print(digit,end=' ')
    
    
    
#############################################
#7536
n=4321
digit=0
reverse=''
while n>0:
    digit=n%10
    reverse=reverse+str(digit)
    #print(digit,end=' ')
    n=n//10
print(reverse)
# print(type(reverse))

    
    
