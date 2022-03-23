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

# Constants

# Constants

llist = List()
source = [11, 22, 33, 44]
print("array to list")
print(f"source(array):{source}")
array_to_list(llist, source)
# list_test(source)
print("list")
for i in llist:
    print(i)

target = []
list_to_array(llist, target)
print("list to array")
print("array")
print(target)

#source = [1, 2, 3, 4, 1, 2, 3]
# list_test(source)
