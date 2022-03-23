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

# Constants

from List_array import List
# Constants

target = List()
t = []
t1 = []
target.append(11)
target.append(22)
target.append(55)
target.insert(3, 44)
target.append(33)
for i in target:
    t.append(i)
print(f"list:{t}")

value = target[1]
target[3] = 1000
for i in target:
    t1.append(i)
print(f"getitem at 1 index : {value}")
print(f"setitem at 3 index 1000:")
print(f"New List:{t1}")
