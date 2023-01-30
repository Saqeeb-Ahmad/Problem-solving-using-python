#sum of evens using recusion
def sum_even(n):
    if n==0:
        return 0
    if n==1:
        return sum_even(n-1)
    return n+sum_even(n-2)

print(sum_even(9))