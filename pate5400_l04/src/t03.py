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
# Constants

target = List()
print("append")
target.append(11)
target.append(22)
target.append(55)
for i in target:
    print(i)
print("insert")
target.insert(3, 44)
for i in target:
    print(i)
target.append(33)
print("remove(55)")
target.remove(55)
for i in target:
    print(i)

target[1] = 2

# print(value)
