# write a program to validate name and password using while loop
while True:
    name=(input('enter name'))
    pwd=(input('enter pwd'))
    if pwd=='python@example' and name=='first_name':
        print('password is correct')
        break
    else:
        print('incorrect password')  