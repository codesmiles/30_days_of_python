# Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py

# Write a python comment saying 'Day 2: 30 Days of python programming'
'''
30 days of python programming
'''

# Declare a first name variable and assign a value to it
first_name = "michael"

# Declare a last name variable and assign a value to it
last_name = "codesmiles"

# Declare a full name variable and assign a value to it
full_name = first_name + " " + last_name

# Declare a country variable and assign a value to it
country = "Nigeria"
# Declare a city variable and assign a value to it
city = "Lagos"
# Declare an age variable and assign a value to it
age = 25

# Declare a year variable and assign a value to it
year = 2024

# Declare a variable is_married and assign a value to it
is_married = False

# Declare a variable is_true and assign a value to it
is_true = True

# Declare a variable is_light_on and assign a value to it
is_light_on = True

# Declare multiple variable on one line
trinity_name, trinity_age = "kizito Trinity", 3


# Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(trinity_name))
print(type(trinity_name))
print(type(trinity_age))

# Using the len() built-in function, find the length of your first name
print(len(first_name) == len(last_name))
# Compare the length of your first name and your last name

# Declare 5 as num_one and 4 as num_two
num_one, num_two = 5, 4
# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
# Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
# Multiply num_two and num_one and assign the value to a variable product
product  = num_one * num_two
# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
reminder = num_one / num_two
# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
radius = 30
area = (22/7) * (radius**2)
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
# Take radius as user input and calculate the area.
radiusInput = input(
    "Input the radius:" 
)
if(int(radiusInput) > 0):
    print((22/7) * (int(radiusInput) ** 2))
else:
    print("Number requested null gotten")
# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
print(help('keywords'))