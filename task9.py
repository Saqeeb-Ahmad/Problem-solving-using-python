#w.a.p. to print index value and its character
string1='python'
for i in range(len(string1)):
    if len(string1)==0:
        print('string is empty:')
    elif  i<len(string1):
        print(i,string1[i])
    else:
        print('index out of range')