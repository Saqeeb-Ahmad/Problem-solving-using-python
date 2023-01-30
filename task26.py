#Write a program to find how many times substring “Emma” appears in the given string
s='Emma is good developer. Emma is a writer'.split()
sub_str='Emma'
count=0
for each in s:
    if each==sub_str:
        count=count+1
print(f'{sub_str} apprears {count} times')

