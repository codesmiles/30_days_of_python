# # syntax
# st = {'item1', 'item2', 'item3', 'item4'}
# print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True

# # syntax
# st = {'item1', 'item2', 'item3', 'item4'}
# st.update(['item5','item6','item7'])
# print(st) # {'item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7'}

# fruits = {'banana', 'orange', 'mango', 'lemon'}
# vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
# fruits.update(vegetables)
# print(fruits) # {'banana', 'orange', 'mango', 'lemon', 'tomato', 'potato', 'cabbage', 'onion', 'carrot'}

# # syntax
# st = {'item1', 'item2', 'item3', 'item4'}
# st.remove('item2')

fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits.pop())  # removes a random item from the set


# nb: you can convert lists to sets and you can also convert tuples to lists and vice versa


# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# Join A and B
AB = A.union(B)
print(AB)
# Find A intersection B
inter = A.intersection(B)
print(inter)

# Is A subset of B
subset = A.issubset(B)
print(subset)

# Are A and B disjoint sets
disjoint = A.isdisjoint(B)
print(disjoint)

# Join A with B and B with A
AB = A.union(B)
BA = B.union(A)
print(AB)
print(BA)

# What is the symmetric difference between A and B
sym_diff = A.symmetric_difference(B)
print(sym_diff)

# Delete the sets completely
del A
del B
del AB
del BA

# Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages_set = set(age)
if len(ages_set) != len(age):
    print(f"The length of the list is bigger {len(age)} than the set {len(ages_set)}")

# Explain the difference between the following data types: string, list, tuple and set
# string is a simple datatype a list is a coplex datatype that can contain multiple elements of differnt datatype all numerically indexed and each of their data can be manipulated while
# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.