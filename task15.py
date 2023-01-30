# s='learning python is very easy'.split() #['learning', 'python', 'is', 'very', 'easy']
# lst=[]
# for i in s:
#     lst.append(i[::-1])
# print(lst)

s='ONE TWO THREE FOUR'.split() #['learning', 'python', 'is', 'very', 'easy']
lst=[]   #['gninrael', 'nohtyp', 'si', 'yrev', 'ysae']
for i in s:
    lst.append(i[::-1])
result=' '.join(lst)
print(result)

# #using list comprehantion
# s = 'ONE TWO THREE FOUR'
# lst = [i[::-1] for i in s.split()]
# result = ' '.join(lst)
# print(result)







