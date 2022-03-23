"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Dev Patel
ID:      212325400
Email:   pate5400@mylaurier.ca
__updated__ = "2022-03-11"
-------------------------------------------------------
"""
# Imports
from Food import Food
from Food_utilities import read_foods, get_vegetarian, by_origin, food_search
# Constants
file_variable = open("foods.txt", "r", encoding="utf-8")
foods = read_foods(file_variable)
print(Food.origins())
origin = int(input("Enter value / -1 for any origin"))
max_cals = int(input("Enter maximum cals / 0 for no limit "))
is_veg = input("Enter y/n for veg")
if is_veg == "y":
    is_veg = True
elif is_veg == "n":
    is_veg = False
results = food_search(foods, origin, max_cals, is_veg)
for i in results:
    print(i)
