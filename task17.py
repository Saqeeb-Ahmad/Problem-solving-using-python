s='abcdefgh'
even_list=[]
odd_list=[]
for i in range(len(s)):
    if i%2==0:
        even_list.append(s[i])
    else:
        odd_list.append(s[i])
result1=' '.join(even_list)
result2=' '.join(odd_list)
print('the character present at even index id:',result1)
print('the character present at odd index is :',result2)
       


