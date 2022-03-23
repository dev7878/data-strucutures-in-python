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
from functions import queue_split_alt
# Constants
source = Queue()
a = [4, 3, 1, 2, 9, 12, 7]
print(f"initial source:{a}")
while len(a) > 0:
    source.insert(a.pop(0))
target1, target2 = queue_split_alt(source)
o = []
for i in source:
    o.append(i)
print(f"final source:{o}")
t1 = []
t2 = []
for i in target1:
    t1.append(i)
print(f"target1:{t1}")
for i in target2:
    t2.append(i)
print(f"target2:{t2}")
