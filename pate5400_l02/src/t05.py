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
from Food_utilities import read_foods
from utilities import stack_test
# Constants
file_variable = open("foods.txt", "r", encoding="utf-8")
foods = read_foods(file_variable)
stack_test(foods)
file_variable.close()
