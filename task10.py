#programm for +ve and - ve index
string=input('enter any string: ')
l=-len(string)
print(l)
for i in range(len(string)):
    print(i,string[i],l)
    l=l+1