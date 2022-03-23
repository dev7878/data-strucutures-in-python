"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Dev Patel
ID:      212325400
Email:   pate5400@mylaurier.ca
__updated__ = "2022-03-19"
-------------------------------------------------------
"""
# Imports

# Constants

from Food_utilities import get_food
from functions import hash_table


food1 = get_food()

print()
food2 = get_food()

print()
hash_table(4, [food1, food2])
