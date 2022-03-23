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
from Stack_array import Stack
from Queue_array import Queue
from Deque_array import Deque
# Constants
"""
source = Stack()
source.push(11)
source.push(22)
source.push(33)
source.push(44)
target1, target2 = source.split_alt()
for i in source:
    print(i)
print("ff")
for i in target1:
    print(i)
for i in target2:
    print(i)
"""
s1 = Queue()
s2 = Queue()
s1.insert(11)
s1.insert(33)
s2.insert(22)
s2.insert(44)
target = Queue()
target.combine(s1, s2)
target.reverse()
for i in target:
    print(i)
"""
deque = Deque()

deque.insert_front(33)
deque.insert_front(22)
deque.insert_front(11)
deque.insert_rear(44)
for i in deque:
    print(i)
"""
