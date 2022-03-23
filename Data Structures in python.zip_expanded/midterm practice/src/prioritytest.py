"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Dev Patel
ID:      212325400
Email:   pate5400@mylaurier.ca
__updated__ = "2022-02-14"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue
# Constants
q1 = Priority_Queue()
q2 = Priority_Queue()
q1.insert(55)
q1.insert(33)
q1.insert(11)
q2.insert(44)
q2.insert(22)

print("q1")
for i in q1:
    print(i)
print("q2")
for i in q2:
    print(i)
target = Priority_Queue()
print("combine")
target.combine(q1, q2)
for i in target:
    print(i)
target1, target2 = target.split_alt()
print("t1")
for i in target1:
    print(i)
print("t2")
for i in target2:
    print(i)
