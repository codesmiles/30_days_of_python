# Declare your age as integer variable
age = 26

# Declare your height as a float variable
height = 40

# Declare a variable that store a complex number
complexNum = 1 -1j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
#     Enter base: 20
#     Enter height: 10
#     The area of the triangle is 100

# base = int(input("Input the Base: "))
# height = int(input("Input the height: "))
# print("The area of a Triangle is: ", int((base * height)/2))

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# Enter side a: 5
# Enter side b: 4
# Enter side c: 3
# The perimeter of the triangle is 12

# a = int(input("enter side a: "))
# b = int(input("enter side b: "))
# c = int(input("enter side c: "))
# area = a + b + c
# print("The perimeter of the triangle is: ", area)

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))


# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
import math
# r = input("Input the radius: ")
# pii = math.pi
# print("The area of a circle is: ", int(pii * int(r) * int(r)))

# r = input("input radius: ")
# print("circumference of a circle is: ",2 * math.pi * r)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# Compare the slopes in tasks 8 and 9.
# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
# There is no 'on' in both dragon and python
# Find the length of the text python and convert the value to float and convert it to string
# value = "pyhon"
# length = len(value)
# print("length of value: ", length)
# print ("float format: ", float(length))
# print("convert it to string:", str(length)," \n", "with a type of ", type( str(length)))

# # Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
# number = input("type your number: ")
# if(int(number) % 2 == 0 ):
#     print("this is an even number")
# else:
#     print("This is an odd number")
    
# # Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
# floor_value = 7 // 3
# if floor_value == 2.7:
#     print("equal")
# else:
#     print("not equal")
# # Check if type of '10' is equal to type of 10
# print(type("10") == type(10))

# # Check if int('9.8') is equal to 10
# print(int(9.8) == 10)

# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# Enter hours: 40
# Enter rate per hour: 28
# Your weekly earning is 1120
hrs = input("hours: ")
rate_per_hr = input("rate per hour:")
pay = int(rate_per_hr) * int(hrs)
print(pay)

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# Enter number of years you have lived: 100
# You have lived for 3153600000 seconds.


# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

# numList = [
# 1, 1, 1, 1, 1,
# 2, 1, 2, 4 ,8,
# 3, 1, 3, 9 ,27,
# 4, 1, 4, 16, 64,
# 5, 1, 5, 25, 125,
# ]

# for num in numList:
#     if 