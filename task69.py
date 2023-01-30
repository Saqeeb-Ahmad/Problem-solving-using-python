#wrtie a program to insert even number at even posion and odd number at odd posion
l=[1,2,3,4,5,6,7,8,9,10]
l1=[]
even_postion=0
odd_postion=1
for i in l:
    if i%2==0:
        l1.insert(even_postion,i)
        even_postion+=2
    else:
        l1.insert(odd_postion,i)
        odd_postion+=2
print(l1)