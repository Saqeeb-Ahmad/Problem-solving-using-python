# # #Write a program that finds the second highest number in an array of integers.
# def second_highest(numbers):
#     highest=max(numbers)
#     numbers.remove(highest)
#     second_hgh=max(numbers)
#     return second_hgh
    
# numbers=[1,2,3,4,5,6,7,8,20 ,12]
# print(second_highest(numbers))



def second_highest(numbers):
    max1 = -1
    max2 = -1
    for num in numbers:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num
    return max2
# Example usage:
numbers = [10, 20, 30, 40, 30, 60]
print("Second highest number:", second_highest(numbers))


