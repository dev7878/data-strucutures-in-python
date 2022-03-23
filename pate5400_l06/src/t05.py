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
from List_linked import List
# Constants
lst = List()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
c = []
for i in lst:
    c.append(i)
print(f"original:{c}")
# lst.remove(3)
value = lst.remove_front()
t = []
for i in lst:
    t.append(i)
print(f" removed {value}  :{t}")
value1 = lst.peek()
print(f"peek:{value1}")
