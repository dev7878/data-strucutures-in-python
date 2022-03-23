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
from utilities import stack_to_array, array_to_stack
# Constants

source = [11, 22, 33, 44]
stack = Stack()
array_to_stack(stack, source)
print("elements of intial stack")
for i in stack:
    print(i)
target = []
print("initial array:", target)
stack_to_array(stack, target)
print("final array:", target)
