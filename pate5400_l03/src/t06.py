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
from Priority_Queue_array import Priority_Queue
from utilities import array_to_pq, pq_to_array
from Food_utilities import read_foods
from utilities import priority_queue_test
# Constants

# print("Array tp pq")\
"""
new = []
pq = Priority_Queue()
source = [11, 22, 33, 44]
# print(f"source:{source}")
array_to_pq(pq, source)
target = []
for i in pq:
    new.append(i)
print("pq to Array")
print(f"pq:{new}")

pq_to_array(pq, target)
print(f"target:{target}")
"""

file_variable = open("foods.txt", "r", encoding="utf-8")
foods = read_foods(file_variable)
priority_queue_test(foods)
file_variable.close()
