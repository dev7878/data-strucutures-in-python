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
from List_linked import List
# Constants
lst = List()
lst.append(50)
lst.append(100)
lst.insert(0, 200)
for i in lst:
    print(i)
value = lst[2]
print(f"value at 2 : {value}")
print("setting 99 at 1")
lst[1] = 99
for i in lst:
    print(i)
