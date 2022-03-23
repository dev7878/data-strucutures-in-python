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
source = Queue()
a = [4, 3, 1, 2, 9, 12, 7]
while len(a) > 0:
    source.insert(a.pop(0))
o = []
for i in source:
    o.append(i)
print(f"source:{o}")
target1, target2 = source.split_alt()
t1 = []
t2 = []
t = []
for i in source:
    t.append(i)
print(f"final source:{t}")
for i in target1:
    t1.append(i)
print(f"target1:{t1}")
for i in target2:
    t2.append(i)
print(f"target2:{t2}")
