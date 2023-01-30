def fact(num):
    result=1
    while num>1:
        result=result*num
        num=num-1
    return result
      
for i in range(1,11):
    print(f'the factorial of {i} is ',fact(i))


#without funtion 


num=1
result=1
if num== 0:
    print(1)
else:
    while num>1:
        result=result*num
        num=num-1
print(result)