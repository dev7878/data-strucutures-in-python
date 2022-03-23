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
from Deque_linked import Deque
# Constants
dq = Deque()
dq.insert_front(2)
dq.insert_front(1)
dq.insert_rear(3)
print("---------------------------")
for i in dq:
    print(i)
dq.remove_front()
dq.remove_rear()
print("------after remove---------")
for i in dq:
    print(i)
