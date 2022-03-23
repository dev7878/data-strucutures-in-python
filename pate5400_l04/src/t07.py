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
from List_array import List
from utilities import array_to_list, list_to_array, list_test
from Food_utilities import read_foods
from Food import Food

# Constants
c = [1, 2, 3, 4, 5]
x = open("foods.txt", "r", encoding="utf-8")
for i in x:
    c.append(i)
    x = [Food("Butter Chicken", 2, None, None),
         Food("lasagna", 7, None, None)]
list_test(c)
x.close()
