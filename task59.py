s='AABBDDFDJGD'
d={}
for i in s:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
for k,v in d.items():
    print(k,f'occures {v} times')
    
#find the coccurrences of each character in a given string

