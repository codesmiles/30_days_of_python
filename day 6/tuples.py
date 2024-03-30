# TUPLES METHODS
# tuple(): to create an empty tuple
# count(): to count the number of a specified item in a tuple
# index(): to find the index of a specified item in a tuple
# operator: to join two or more tuples and to create a new tuple

# create an empty tuple
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()

print("tuple value",empty_tuple, "tuple type",type(empty_tuple))

# creating tuples with values
tpl = ('item1', 'item2','item3')
print(tpl, "of type", type(tpl))

# indexing tuple items
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]
print('item', first_item, second_item)

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[last_index]

# slicing tuples
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # all items
all_items = tpl[0:]         # all items
middle_two_items = tpl[1:3]  # does not include item at index 3

# one can change a tuple to a list
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)

# checking a if an item is in a tuple
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False



# Check if 'Estonia' is a nordic country

# Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print("Iceland" in nordic_countries)
print("Estonia" in nordic_countries)