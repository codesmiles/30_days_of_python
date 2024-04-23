'''
Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
Sort countries by name, by capital, by population
Sort out the ten most spoken languages by location.
Sort out the ten most populated countries.
'''
# from country_data import list_of_countries as data

# def sort_list_data():
#     print("state |capital |population")
#     def sort_list(country_data):
#         return f"{country_data["name"]} {country_data["capital"]} {country_data["population"]}"
#     return sort_list


# name_capital_population = sort_list_data()
# mapDict = map(name_capital_population, data)
# print(list(mapDict))

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use map to create a new list by changing each country to uppercase in the countries list

def to_uppercase(text):
    return text.upper()

map_to_uppercase = map(to_uppercase,countries)
print(list(map_to_uppercase))

# Use map to create a new list by changing each number to its square in the numbers list
map_to_square = map(lambda num:num ** 2,numbers )
print(list(map_to_square))

# Use map to change each name to uppercase in the names list


# Use filter to filter out countries containing 'land'.
filter_countries = filter(lambda val: val, countries)

