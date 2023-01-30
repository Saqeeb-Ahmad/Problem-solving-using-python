# this program will retrun max value and min value
l1=[30,20,3,4,5,10,60]
min_value=l1[0]
max_value=l1[0]
for x in l1:
    if x>max_value: # 
        max_value=x
    if x<min_value:
        min_value=x #20,3
print(min_value)
print(max_value)
###########################################################################
l1=[60,20,3,4,5,10]                            #[20,60,3,4,5,10], [20,3,60,4,5,10]

# bubble sort algorithen******
temp=0
for x in range(len(l1)-1,0,-1):
    for i in range(x): #0,1,2
        if l1[i]>l1[i+1]:
            temp=l1[i]
            l1[i]=l1[i+1]
            l1[i+1]=temp
        print(l1)
print('min value',l1[0])
print('max value',l1[-1])








