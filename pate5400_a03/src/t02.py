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
source1.push("s1p1")
source1.push("s1p2")
source1.push("s1p3")
source1.push("s1p4")
print("")
for c in source1:
    print(c)
source2 = Stack()
source2.push("s2p1")
source2.push("s2p2")
source2.push("s2p3")
# source2.push(1)
# source2.push(6)
# source2.push(3)
print("the second stack is ")
for j in source2:
    print(j)
print()
target = Stack()
target.combine(source1, source2)
print("the combined stack is ")
for i in target:
    print(i)
