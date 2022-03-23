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

from Hash_Set_array import Hash_Set

hset = Hash_Set(1)

arr = [100, 1000, 20, 5, 6, 10, 2, 9, 3400, 300, 500, 10000]

for value in arr:
    hset.insert(value)

print("Hash Set: ")
hset.debug()

for value in arr:
    hset.insert(value + 1)
    hset.insert(value + 2)

print()
print("New Hash Set: ")
hset.debug()
