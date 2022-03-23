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
from List_linked import List
# Constants
l1 = List()
l2 = List()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l2.append(1)
l2.append(2)
l2.append(33)
l2.append(44)
target = List()
target.intersection_r(l1, l2)
print("-----l1------")
for i in l1:
    print(i)
print("-----l2------")
for i in l2:
    print(i)
print("----intersection----")
for i in target:
    print(i)
