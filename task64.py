s='saqeeb ahamd nafeesullah'
vowels=('a','e','i','o','u')
d={}
for i in s:
    if i in vowels:
        d[i]=d.get(i,0)+1
for k,v in d.items():
    print(k,v)
        
#count the frequency of vowels