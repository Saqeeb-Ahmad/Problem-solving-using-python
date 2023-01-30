def is_leap(year):
    if year %400==0 or( year %4==0 and year!=0):
        print('it is a leap year')
    else:
        print('it is not a leap year')
year=int(input('enter year'))
is_leap(year)