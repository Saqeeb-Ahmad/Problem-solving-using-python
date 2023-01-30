s1='saqee'
s2='ahmad'
i=0
j=0
output=''
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output=output+s1[i]
    if j<len(s2):
        output=output+s2[j]
    i=i+1
    j=j+1
print(output)