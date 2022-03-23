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
from Priority_Queue_array import Priority_Queue
# Constants
pq = Priority_Queue()
pq.insert(1)
pq.insert(2)
pq.insert(3)
o = []
for i in pq:
    o.append(i)
print(f"original pq :{o}")
value = pq.remove()
print(f"remove:{value}")
e = []
for i in pq:
    e.append(i)
print(f"new pq :{e}")
