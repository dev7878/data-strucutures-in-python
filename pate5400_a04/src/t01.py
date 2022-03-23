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
from Queue_circular import Queue
# Constants
s = []
cq = Queue(3)
empty = cq.is_empty()
print(f"Queue is empty:{empty}")
cq.insert(1)
cq.insert(2)
cq.insert(3)
full = cq.is_full()
print(f"full:{full}")
empty = cq.is_empty()
print(f"Queue is empty:{empty}")
print("the queue is")
for v in cq:
    s.append(v)
print(s)

v = cq.remove()
print(f"remove : {v}")
print("the queue after remove")

for i in cq:
    print(i)
p = cq.peek()
print(f"peek: {p}")
