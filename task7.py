#write a program to replace (comma ,) with (dot .)
s='hi, how are you '
new_s=''
comma=','
dot='.'
for char in s:
    if char ==comma:
        new_s+=dot
    else:
        new_s+=char
print(new_s)
