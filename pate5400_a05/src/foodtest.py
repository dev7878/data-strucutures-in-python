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
from List_array import List
from Food import Food
# Constants
t1 = List()
t1.append(Food("BBQ Pork", 1, False, 920))
t1.append(Food("BBQ Pork", 1, False, 920))
t1.append(Food("General Tao Chicken", 1, False, 850))
t1.clean()
print("cleaned list1")
for i in t1:
    print(i)

t2 = list()
t2.append(Food("Lemon Chicken", 1, False, 226))
t2.append(Food("Orange Chicken", 1, False, 800))
t2.append(Food("Greek Salad", 5, True, 185))
t2.append(Food("BBQ Pork", 1, False, 920))
print("list2")
for i in t2:
    print(i)

target = List()
"""
target.combine(t1, t2)
print("combined list")
for i in target:
    print(i)
value = target[1]
print(f"value at index 1 in target: {value}")

print("intersection of t1,t2")
target.intersection(t1, t2)
for i in target:
    print(i)
"""
b = t1.is_identical(t2)
print(f"t1,t2 identical :{b}")
t1.prepend(Food("Pavlova", 10, True, 272))
print("after prepend")
value = t1.remove_front()
print("after remove front")
for i in t1:
    print(i)
