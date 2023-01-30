##Write a program to iterate the first 10 numbers and in each iteration, print the sum of 
# the current and previous number.
n=0
for i in range(10):
    print(f'Current Number {i} Previous Number  {n}  Sum:',i+n)
    n=i