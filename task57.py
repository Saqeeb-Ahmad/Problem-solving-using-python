#write a program to check anagram or not
s1='race' 
s2='care'
anagram=''
if len(s1)==len(s2):
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]==s2[j]:
                anagram=anagram+s1[i]
if anagram==(s1 or s2):
    print(s1,"and",s2,'are anagrams')
else:
    print(s1,'and',s2,'are not anagrams')

            