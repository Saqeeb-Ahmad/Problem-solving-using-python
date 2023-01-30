#remove elemetns using remove method
l=[10,20,30,10,1,10,10,223,223,]
x=int(input('enter x value:'))

for i in range(len(l)):
    if x in l:
        l.remove(x)
print(l)

#################
# l=[10,20,30,10,1,10,10,223,223,]
# x=int(input('enter x value:'))

# while x in l:
#     l.remove(x)
# print(l)


# to remocve duplicates from the list
# l=[10,20,30,10,1,10,10,223,223,]
# l2=[]
# for i in l:
#     if i not in l2:
#         l2.append(i)

# print(l2)