def find_char(s):
    l=len(s)
    
    i=s.find(search_str, 0, l)
    if i==-1:
        return False
    return True
s='saqeeb'
search_str='a'
print(find_char(s))
#find the character in a given string