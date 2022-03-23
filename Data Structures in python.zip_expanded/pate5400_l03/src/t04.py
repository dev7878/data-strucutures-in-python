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
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue

# Constants
pq = Priority_Queue()
o = []
values = [1, 2, 3]
print(f"value {values}")
for value in values:
    pq.insert(value)

for i in pq:
    o.append(i)
print(f"pq:{o}")
print("peek:")
v = pq.peek()
