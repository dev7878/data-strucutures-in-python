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
lst.append(1)
lst.append(2)
lst.append(2)
lst.append(4)
n = lst.count(2)
c = []
for i in lst:
    c.append(i)
print(f"list:{c}")

print(f"count for 2 : {n}")
max = lst.max()
min = lst.min()
print(f"maximun value:{max}")
print(f"minimun value:{min}")
