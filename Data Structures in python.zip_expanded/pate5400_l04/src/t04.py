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

source.append(11)
source.append(22)
source .append(55)
source .append(44)
source .append(33)
source .append(55)
for i in source:
    print(i)
index = source.index(22)
find = source.find(0)
count = source.count(55)
max = source.max()
min = source.min()
print(f"""Index of 22 :{index}
find number on index 4:{find}
count 55 :{count}
maximum number:{max}
minimum number:{min}""")
