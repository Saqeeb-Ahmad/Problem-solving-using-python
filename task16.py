s='one two three four'.split() #
lst=[]  #['one', 'two', 'three', 'four', 'five']
emty=''
for i in s:
    lst.append(i[::-1])
result=' '.join(lst)
print(result)