"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Dev Patel
ID:      212325400
Email:   pate5400@mylaurier.ca
__updated__ = "2022-03-12"
-------------------------------------------------------
"""
# Imports
from Food_utilities import write_foods, read_foods
# Constants
file_variable = open("foods.txt", "r", encoding="utf-8")
file_variable1 = open("new_foods", "a", encoding="utf-8")
foods = read_foods(file_variable)
write_foods(file_variable1, foods)
