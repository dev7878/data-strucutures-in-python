"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Dev Patel
ID:      212325400
Email:   pate5400@mylaurier.ca
__updated__ = "2022-02-10"
-------------------------------------------------------
"""
# Imports
from Queue_circular import Queue
# Constants
q1 = Queue()
q1.insert(11)

q1.insert(22)
q1.insert(33)
q1.insert(44)

q1.remove()
for i in q1:
    print(i)
v = q1.peek()
print(v)
