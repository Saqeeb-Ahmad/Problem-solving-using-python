#1
#w.a.p to reverse the word of string  
l='Learning python is very easy'.split()
index=len(l)-1
i=0
while i<len(l):
    epmty=''+l[index]
    index=index-1
    i+=1
    print(epmty,end=' ')
# #2

# s='learning python is very easy'.split() #['a', 'b', 'c', 'd', 'e', 'f']
# l=len(s)-1
# new_str=''
# while l>=0:
#     new_str=new_str+' '+s[l]
#     l=l-1
# print(new_str.strip())
# #3
s='learning python is very easy'.split()
lst=[]
l=len(s)-1
while l>=0:
    lst.append(s[l])
    l=l-1
result=' '.join(lst)
print(result)

