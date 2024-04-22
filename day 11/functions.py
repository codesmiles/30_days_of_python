# def sum_all_nums(*nums):
#     total = 0
#     for num in nums:
#         total += num     # same as total = total + num 
#     return total
# print(sum_all_nums(2, 3, 5)) # 10

# #You can pass functions around as parameters
# def square_number (n):
#     return n * n
# def do_something(f, x):
#     return f(x)
# print(do_something(square_number, 3))


# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list1(["A", "B", "C"]))
# # ["C", "B", "A"]

def reverse_tpl(*tpl):
    arr = list(tpl)
    arr.reverse()
    return arr

print(reverse_tpl(1, 2, 3, 4, 5))

def reverse_list(list):
    return list[::-1]

print(reverse_list([1, 2, 3, 4, 5]))

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
# numbers = [2, 3, 7, 9];
# print(add_item(numbers, 5))      [2, 3, 7, 9, 5]

def add_item(list, item):
    list.append(item)
    return list

print(add_item([1, 2, 3, 4, 5], 6))
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_stuff, "Dayo"))

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9];
# print(remove_item(numbers, 3))  # [2, 7, 9]

def remove_item(list, item):
    if item in list:
        list.remove(item)
        return list
    else:
        return "item not found"

print(remove_item([1, 2, 3, 4, 5], 3))

# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.
def evens_and_odds(num):
    evens = 0
    odds = 0

    for i in range(0, num + 1):
        if i >=0 and i % 2 == 0:
            evens += 1
        elif i >=0 and i % 2 != 0:
            odds += 1
        else:
            pass
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."

print(evens_and_odds(100))
        