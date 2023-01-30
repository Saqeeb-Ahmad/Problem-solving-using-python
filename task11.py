#w.a.p. to find the number of occurnces with its index values
string=input('enter any string:')
sub_string=input('enter sub string:')
pos=0
counter=0
l=len(string)
while True:
    index=string.find(sub_string, pos, l)
    if index==-1:
        break
    else:
        print('at index ',index)
        counter+=1
        pos=index+len(sub_string)
print('number of occurences',counter)