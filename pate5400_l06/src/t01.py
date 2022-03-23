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
print("prepend:5")
lst.prepend(5)
print("append 6")
lst.append(6)
print("insert 99 at 1")
lst.insert(1, 99)
for i in lst:
    print(i)
