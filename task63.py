s= "Great responsibility"
l1=[]
d1=set()
for i in s:
    if i not in l1:
        l1.append(i)
    else:
        d1.add(i)
        

print(sorted(d1))