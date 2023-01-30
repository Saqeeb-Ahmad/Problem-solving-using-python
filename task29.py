#Given two list of numbers, write a program to create a new list such that 
# the new list 
# should contain odd numbers from the first list and even numbers from the 
# second list.
l1=[10, 20, 25, 30, 35]
l2=[40, 45, 60, 75, 90]
l3=[]
for i in l1:
    if i%2!=0:
        l3.append(i)
for j in l2:
    if j%2==0:
        l3.append(j)
print(l3)