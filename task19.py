s='a1b2c3d4'
s1=''
s2=''
for x in s:
    if x.isalpha():
        s1=s1+x
    else:
        s2=s2+x
result=''.join(sorted(s1))+''.join(sorted(s2))
print(result)