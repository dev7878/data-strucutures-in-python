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
from functions import pq_split_key
# Constants
source = Priority_Queue()
a = [4, 1, 7, 3, 9, 2, 4, 5, 1, 7, 0, 9]
while len(a) > 0:
    source.insert(a.pop(0))
o = []
for i in source:
    o.append(i)
print(f"source:{o}")
key = 4
print(f"key:{key}")
target1, target2 = pq_split_key(source, key)
t1 = []
t2 = []
for i in target1:
    t1.append(i)
print(f"target1:{t1}")
for i in target2:
    t2.append(i)
print(f"target2:{t2}")
