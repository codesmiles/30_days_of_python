# Third Example about unpacking list
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

# checking items in a list
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

# Adding items to a list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)

# inserting items to the specified index of a list

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)

# removing items from a list
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - this method removes the first occurrence of the item in the list
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango', 'banana']

# remove items using pop unlike remove this one uses index values instead and if no index is specified it will be removed from end of list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)  

# using del
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3!
print(fruits)       # ['orange', 'lime']
del fruits
# print(fruits)  # deletes the fruit  

# clear the list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)   

# copy the list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)  

# joining two lists together
# plus (+)
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

# using the extend (extend())
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)
print(list1)

# counting items in a list
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))

# index of an item majorly the first occurence of the item in the list
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24)) 

# reversing items in a list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)


# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age

ages.sort()
print(" min:",ages[0],"\n","max:",ages[-1])
# Add the min age and the max age again to the list
min_age = ages[0]
max_age = ages[-1]
new_ages = ages + [min_age,max_age]
print(new_ages)
# Find the median age (one middle item or two middle items divided by two)
median_age = new_ages[len(new_ages) // 2]
print("Median Age: ",median_age)
# Find the average age (sum of all items divided by their number )
average_age = sum(new_ages) / len(new_ages)
print("Average Age: ",average_age)
# Find the range of the ages (max minus min)
max_age = new_ages[-1]
min_age = new_ages[0]
range_age = max_age - min_age
print("Range of Ages: ",range_age)
# Compare the value of (min - average) and (max - average), use abs() method
min_age = new_ages[0]
max_range_age = abs(max_age - average_age)
min_range_age = abs(min_age - average_age)
print("Range of Ages: ",max_range_age, min_range_age)
# Find the middle country(ies) in the countries list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
middle_country = countries[len(countries) // 2]
print("Middle Country: ",middle_country)
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
if len(countries) % 2 == 0:
    first_half = countries[:len(countries) // 2]
    second_half = countries[len(countries) // 2:]
    print(first_half)
    print(second_half)
else:
    first_half = countries[:len(countries) // 2 + 1]
    second_half = countries[len(countries) // 2 + 1:]
    print(first_half)
    print(second_half)
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)