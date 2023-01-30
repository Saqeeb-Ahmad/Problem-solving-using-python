# take 3 muners from user and print their maximum
n1=int(input('enter first number: '))
n2=int(input('enter second number: '))
n3=int(input('enter thid number: '))
max=n1  if (n1>n2 and n1>n3) else n2 if (n2>n1 and n2 >n3) else n3
print(max)