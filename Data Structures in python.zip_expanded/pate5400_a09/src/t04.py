"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Dev Patel
ID:      212325400
Email:   pate5400@mylaurier.ca
__updated__ = "2022-03-21"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
# Constantsm
bst = BST()
t = [11, 7, 15, 6, 9, 12, 18, 8]
for i in t:
    bst.insert(i)

check_1 = 15
check_2 = 78
print(bst.node_counts())
print("check 15 in bst")
print(check_1 in bst)
print("check 78 in bst")
print(check_2 in bst)
key = 15
b = bst.parent(key)
print(f"parent: of 15: {b}")
