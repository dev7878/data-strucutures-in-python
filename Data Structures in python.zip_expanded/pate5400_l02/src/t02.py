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
from Stack_array import Stack
from utilities import array_to_stack
# Constants
source = ["a", "b", 23, "@"]
print("initial array: ", source)
s = Stack()
t = array_to_stack(s, source)
print("final array: ", source)
print("elements of stack")
for v in s:
    print(v)
