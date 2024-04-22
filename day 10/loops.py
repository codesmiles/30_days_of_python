# # Iterate 0 to 10 using for loop, do the same using while loop.
# for i in range(10):
#     print(i)
    
# # Iterate 10 to 0 using for loop, do the same using while loop.
# i = 10
# while i > 0:
#     print(i)
#     i = i - 1
    
# numbers = [0, 1, 2, 3, 4, 5]
# for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
#     print(number)
    
# numbers = (0,1,2,3,4,5)
# for number in numbers:
#     print(number)
#     if number == 3:
#         break

# numbers = (0,1,2,3,4,5)
# for number in numbers:
#     print(number)
#     if number == 3:
#         continue
#     print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
# print('outside the loop')

# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
num = 0
for i in range(0,101):
    num = num + i

print('sum of all numbers: ', num)

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.
num2 = 0
for i in range(0,101,2):
    num2 += i

print('sum of all evens: ', num2)

num3 = 0
for i in range(1,101,2):
    num3 += i

print('sum of all odds: ', num3)