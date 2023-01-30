# def fact(n):
#     result=1
#     for i in range(n,0,-1):
#         result=result*i
#     return result
        
# print(fact(4))
def fact1(n):
    result=1
    while n >1:
        result=result*n
        n=n-1
    return result
print(fact1(5))
     
        