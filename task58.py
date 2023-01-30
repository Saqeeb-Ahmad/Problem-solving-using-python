#to find no of vowels and consonant in string
vowel_count=0
consonant_count=0
s='This is a really simple sentence'.upper()
for each in s:
    if each in ('A','E','I','O','U'):
        vowel_count+=1
    elif each.isalpha():
        consonant_count+=1
print('total vowels are',vowel_count)
print('total no of consonant are',consonant_count)


# # w.a.p. t check how many this vowels present in string
# s='this is a very simple sentence '
# count=0
# vowels=('a','e','i','o','u')
# for ch in s:
#     if ch in vowels:
#         count+=1
# print(count)
        