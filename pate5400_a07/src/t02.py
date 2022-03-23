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
from Sorted_List_linked import Sorted_List
# Constants
l1 = Sorted_List()
l2 = Sorted_List()
target = Sorted_List()
tar = Sorted_List()
l1.insert(11)
l1.insert(22)
l1.insert(33)
# l1.insert(33)
l1.insert(44)
l1.insert(45)
l1.remove(22)
l2.insert(11)
l2.insert(100)
l2.insert(99)
value = l1[3]
print(f"get value at index 3 :{value}")
for i in l1:
    print(i)
print("clean the list")
print("-------l1---------")
for i in l1:
    print(i)
value = l1.find(33)
print(f"find 33 : {value}")
ind = l1.index(44)
print(f"index of 44 : {ind}")
print("---------------l2-----------")
for i in l2:
    print(i)
target.intersection(l1, l2)
print("-----intersection-----")
for i in target:
    print(i)
b = l1.is_identical(l2)
print(f" l1,l2 indentical: {b}")
max = l1.max()
min = l1.min()
print(f"""maximum in l1 : {max}
minimum in l1: {min}""")
pe = l2.peek()
print(f"peek l2 : {pe}")
l2.remove_front()
print("-----l2 after remove front-----")
for i in l2:
    print(i)
tar.union(l1, l2)
print("-----union l1,l2----")
for i in tar:
    print(i)
c = 45 in l1
print(f"check 45 in l1: {c}")
