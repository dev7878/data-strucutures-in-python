"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Dev Patel
ID:      212325400
Email:   pate5400@mylaurier.ca
__updated__ = "2022-03-21"
-------------------------------------------------------
"""
# Imports

# Constants


from Hash_Set_array import Hash_Set
from Food import Food
from Food_utilities import get_food
# Constants
hset = Hash_Set(2)


food1 = get_food()

print()
food2 = get_food()
food3 = get_food()
print()
hset.insert(food1)
hset.insert(food2)
hset.insert(food3)

hset.debug()
