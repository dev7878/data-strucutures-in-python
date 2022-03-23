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
from Queue_linked import Queue
# Constants
q1 = Queue()
q2 = Queue()
q1.insert(1)
q1.insert(3)
q1.insert(5)
q2.insert(2)
q2.insert(4)
#target = Queue()
#target.combine(q1, q2)
q = Queue()
q.insert(2)
q.insert(2)
q.insert(2)
q.insert(2)
target1, target2 = q.split_alt()
for i in target1:
    print(i)
print("--------")
for i in target2:
    print(i)
b = target1.is_identical(target2)
print(b)
