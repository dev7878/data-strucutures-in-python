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
from Priority_Queue_linked import Priority_Queue
# Constants
pq = Priority_Queue()
pq.insert(99)
pq.insert(100)
pq.insert(101)
target1, target2 = pq.split_alt()
print("-----source-----")
for i in pq:
    print(i)
print("----t1------")
for i in target1:
    print(i)
print("----t2------")
for i in target2:
    print(i)
