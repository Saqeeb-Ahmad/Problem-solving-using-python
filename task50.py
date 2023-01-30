#to check wheather the number is palindrome or not
def palindrome(n):
    digit=0
    rev_n=0
    temp=n
    while temp>0:
        digit=temp%10
        rev_n=rev_n*10+digit
        temp=temp//10
    if n==rev_n:
        return True
    else:
        return False
n=11000011
print(palindrome(n))

