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
lst.append("dev")
lst.append("rushil")
lst.insert(0, "darsh")
for i in lst:
    print(i)
value = lst.find("darsh")
print("----------------")
print(f"find: {value}")
lst[1] = "munni"
print("added [munni] at 1")
for i in lst:
    print(i)
b = "darsh" in lst
print(f"check darsh in lst : {b}")
