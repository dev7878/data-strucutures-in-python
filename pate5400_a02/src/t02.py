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
from Food_utilities import average_calories, read_foods
# Constants
file_variable = open("foods.txt", "r", encoding="utf-8")
foods = read_foods(file_variable)
avg = average_calories(foods)
print(avg)
