# write a program for sum of even and odd numbers
n=100
even_sum=0
odd_sum=0
for i in range(n):
    if i%2==0:
        even_sum=even_sum+i
    else:
        odd_sum=odd_sum+i
print('even sum',even_sum)
print('odd sum',odd_sum)
        
