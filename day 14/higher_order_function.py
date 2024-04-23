def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation

result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15


'''
|--------------------------------------------------------------------------
|  add comment
|--------------------------------------------------------------------------
'''
def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3

'''
|--------------------------------------------------------------------------
|  add comment
|--------------------------------------------------------------------------
'''
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15

'''
|--------------------------------------------------------------------------
|  add comment
|--------------------------------------------------------------------------
'''
# # Normal function
# def greeting():
#     return 'Welcome to Python'
# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper
# g = uppercase_decorator(greeting)
# print(g())          # WELCOME TO PYTHON

## Let us implement the example above with a decorator

'''
|--------------------------------------------------------------------------
|  add comment
|--------------------------------------------------------------------------
'''
'''
This decorator function is a higher order function
that takes a function as a parameter
'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def hello():
    return 'hello Python'
print(hello())   # WELCOME TO PYTHON

def hi(): 
    return "what's up?"
print(hi())


'''
|--------------------------------------------------------------------------
|  add comment
|--------------------------------------------------------------------------
'''
'''These decorator functions are higher order functions
that take functions as parameters'''

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON


'''
|--------------------------------------------------------------------------
|  add comment
|--------------------------------------------------------------------------
'''
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')

'''
|--------------------------------------------------------------------------
|  inbuilt map function
|--------------------------------------------------------------------------
'''
numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Lets apply it with a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]

numbers_int = [1,2,3,4,5,6,7,7,8,9]
numbers_int = map(str, numbers_int)
print(list(numbers_int))    # ['1', '2', '3', '4', '5', '6', '7', '7', '8', '9']


'''
|--------------------------------------------------------------------------
|  inbuilt filter function
|--------------------------------------------------------------------------
'''
# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]


'''
|--------------------------------------------------------------------------
|  inbuilt reduce function
|--------------------------------------------------------------------------
'''
from functools import reduce
numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15

# Explain the difference between map, filter, and reduce.
'''
map takes in a function(lambda or def) and a list and performs the actions listed on that function on a list and returns a new list
filter takes in a function(lambda or def) and a list and returns a new list with only the elements that return True
reduce need to be imported from functools and it takes in a function(lambda or def) and a list and runs the action listed on that function on a list with the aim of reducing
'''

# Explain the difference between higher order function, closure and decorator
'''
higher order function is a function that takes a function as a parameter
closure is a function that returns a function
decorator is a function that takes a function as a parameter and returns a function
'''

# Define a call function before map, filter or reduce, see examples.

val_list = [1, 2, 3, 4, 5, 6, 7]
def call(func):
    return func()
mapCall = map(call, val_list)
# Use for loop to print each country in the countries list.
# Use for to print each name in the names list.
# Use for to print each number in the numbers list.

