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
lst = List()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lst.append(5)

even, odd = lst.split_alt_r()
print("-----lst--------")
for i in lst:
    print(i)
print("---even--------")
for i in even:
    print(i)
print("----odd--------")
for i in odd:
    print(i)
