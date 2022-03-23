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

# Constants

from Food import Food
from Food_utilities import calories_by_origin, average_calories, read_foods
# Constants
file_variable = open("foods.txt", "r", encoding="utf-8")
foods = read_foods(file_variable)
print(Food.origins())
origin = int(input("Enter origin number"))
a = calories_by_origin(foods, origin)
print(a)
