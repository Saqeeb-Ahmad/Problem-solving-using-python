# # 1***** using while loop ****#
# s='saqeeb'
# l=len(s)-1
# new_str=''
# while l>=0:
#     new_str=new_str+s[l]
#     l=l-1
# print(new_str)

# 2***** using for loop ****#
s='saqeeb'
l=len(s)-1
new_str=''
for i in s:
    new_str=new_str+s[l]
    l=l-1
print(new_str)
#3***** using inbult function reversed ****#
# s='saqeeb'
# r=reversed(s)
# for i in r:
#     print(i,end='')

#4***** using inbult function reversed ****#
# s='saqeeb'
# print(s[::-1])

#5***** using inbult function reversed and join method ****#
# s='abcdef'
# r=reversed(s)
# result=''.join(r)
# print(result)