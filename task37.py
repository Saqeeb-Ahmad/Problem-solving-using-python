# num=int(input('enter number to check it is armstrong number or not:'))
# lenght=len(str(num))
# sum=0
# temp=num
# while  temp!=0:
#     digit=temp%10
#     sum=sum+digit**lenght
#     temp=temp//10
# if sum==num:
#     print(sum,'it is Armstrong Nmuber')
# else:
#     print('it is not Armstrong Nmuber')
    
def armstrong(num):
    lenght=len(str(num))
    temp=num
    digit=0
    sum=0
    while temp>0:
        digit=temp%10
        sum=sum+digit**lenght
        temp=temp//10
    if num==sum:
        return True
    return False
num=371
print(armstrong(num))


 