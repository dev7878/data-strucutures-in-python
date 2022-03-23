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
from utilities import array_to_queue, queue_to_array, queue_test
# Constants

print("Array to Queue")
queue = Queue()
source = ["dev", "patel", 2]
print(f"source:{source}")

array_to_queue(queue, source)
q1 = []
for i in queue:
    q1.append(i)
print(f"queue:{q1}")

print("Queue to Array")
queue = Queue()
source = ["dev", "patel", 2]
array_to_queue(queue, source)
q1 = []
for i in queue:
    q1.append(i)
print("original queue:")
print(q1)
target = []

print("returned array:")
queue_to_array(queue, target)
print(target)


a = [1, 2, 3]
queue_test(a)
