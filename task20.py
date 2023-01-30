# s='aabbccddeeffghijjkkllmmnnopqrstuvwwxxxyz'
# empty_set=set()
# for each in s:
#     empty_set.add(each)
# print(empty_set)
# result=' '.join(sorted(empty_set))
# print(result)


s='aabbccddeeffghijjkkllmmnnopqrstuvwwxxxyz'
l=[]
for each in s:
    if each not in l:
        l.append(each)
result=' '.join(l)
print(result)



