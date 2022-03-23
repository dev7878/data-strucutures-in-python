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
# Constants
queue = Queue()
queue = Queue()
queue.insert(33)
queue.insert(22)
queue.insert(55)
queue.insert(44)
# queue.insert(11)
q1 = []
for i in queue:
    q1.append(i)
print(f"the queue is {q1}")
q2 = []
value = queue.remove()
for i in queue:
    q2.append(i)
print(f"the new queue is after remove {q2}")

value = queue.peek()
