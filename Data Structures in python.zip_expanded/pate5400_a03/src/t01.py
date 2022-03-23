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
from functions import stack_combine
# Constants
source1 = Stack()
source1.push(2)
source1.push(4)
source1.push(6)
source1.push(8)
print("the first stack is ")
for c in source1:
    print(c)
source2 = Stack()
# source2.push(14)
# source2.push(9)
source2.push(1)
source2.push(3)
source2.push(5)
source2.push(7)
print("the second stack is ")
for j in source2:
    print(j)
print()
target = stack_combine(source1, source2)
print("the combined stack is ")
for i in target:
    print(i)
