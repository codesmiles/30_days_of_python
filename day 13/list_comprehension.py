# Generating numbers
numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# performing operations in the list
numbers = [i * i for i in range(11)] 
print(numbers)                    

# Generating even numbers
even_numbers = [i for i in range(21) if i != 0 and i % 2 == 0]  # to generate even numbers list in range 0 to 21
print(even_numbers)   

# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print(list(filter(lambda x: x > 0, numbers)))  

def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five) 

# Flatten the following list of lists of lists to a one dimensional list :
# list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
# output
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
output = [number for dlist in list_of_lists for list in dlist for number in list]
print(output)

# Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
data = [number for number in numbers if number > 0]
print(data)

# Using list comprehension create the following list of tuples:

# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]

numberlist =[(i, i ** i) for i in range(11)]
print(numberlist)