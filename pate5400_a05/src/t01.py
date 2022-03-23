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
# Constants
source = List()

source.append(1)
source.append(2)
source.append(5)
source.append(6)
source.append(1)


# source.prepend(0)
#value = source.remove_front()

# source.append()
print("source1")
for i in source:
    print(i)
source.clean()
print("clean")
for i in source:
    print(i)
#value = source[2]
#print(f"value at 2 index in source:{value}")

s2 = List()
s2.append(1)
s2.append(2)
s2.append(5)
s2.append(6)
s2.append(6)
s2.remove_many(6)
print("source2")
for i in s2:
    print(i)
source.clean()
target = List()
target.combine(source, s2)
target.intersection(source, s2)
print("target")
for i in target:
    print(i)

b = source.is_identical(s2)
print(f"source identical with s2:{b}")

#target1, target2 = source.split()

target1, target2 = source.split_alt()
print("target1")
for i in target1:
    print(i)
print("target2")
for i in target2:
    print(i)
ite = List()
ite.union(target1, target2)
print("union")
for i in ite:
    print(i)
