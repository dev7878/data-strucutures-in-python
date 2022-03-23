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
from Sorted_List_array import Sorted_List
# Constants
s1 = Sorted_List()
s2 = Sorted_List()
s1.insert(1)
s1.insert(-2)
s1.insert(8)
s1.insert(1)
s1.insert(1)
s1.clean()
print("s1")
for i in s1:
    print(i)
n = s1.count(1)
print(f"1 repeated: {n} times")

s2.insert(1)
s2.insert(2)
s2.insert(2)
s2.insert(3)
s2.insert(4)
s2.insert(5)
print("s2")
for i in s2:
    print(i)

target = Sorted_List()
target.intersection(s1, s2)
print("intersection s1,s2")
for i in target:
    print(i)

b = s1.is_identical(s2)
print(f"identiacal s1,s2:{b}")
vmax = s1.max()
vmin = s1.min()
print(f"maximum in s1:{vmax}")
print(f"minimum in s1:{vmin}")
vpeek = s1.peek()
print(f"peeked s1 :{vpeek}")
s1.remove(-2)
print("s1 after remove -2")
for i in s1:
    print(i)
s2.remove_many(0)
print("s2 after remove all 3 0")
for i in s2:
    print(i)

#target1, target2 = s2.split()
#target1, target2 = s2.split_alt()
target1, target2 = s2.split_key(3)
print("target1")
for i in target1:
    print(i)
print("target2")
for i in target2:
    print(i)
target.union(target1, target2)
print("union")
for i in target:
    print(i)
