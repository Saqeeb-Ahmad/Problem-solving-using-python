#1.Write a program that reverses a string.
s='saqeeb'
revers=''
for i in range(len(s)):
    revers=revers+s[len(s)-i-1]
    print(revers)