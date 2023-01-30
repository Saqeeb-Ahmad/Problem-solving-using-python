# def palindrome(s):
#     n=len(s)
#     fist=0
#     last=n-1
#     while fist<last:         #if while cond will false it will go to out of the loop
#         if s[fist]==s[last]: #if,if condition is false it'll go to else
#             fist=fist+1
#             last=last-1
#         else:
#             return False
#         return True
# s='NITIN'
# print(palindrome(s))


def palindrome(s):
    result=''.join(reversed(s))
    if result==s:
        return True
    return False
s='racecar'
print(palindrome(s))
    
    
