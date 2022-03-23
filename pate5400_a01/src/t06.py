"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Dev Patel
ID:      212325400
Email:   pate5400@mylaurier.ca
__updated__ = "2022-03-11"
-------------------------------------------------------
"""
# Imports
from functions import max_diff
# Constants
a = []
i = int(input("Enter number to add to list "))
a.append(i)
while i != -999:
    i = int(input("Enter -999  to stop "))
    a.append(i)
a.pop()
print(f"{a}")
md = max_diff(a)
print(f"{md}")
