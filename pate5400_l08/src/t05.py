"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Dev Patel
ID:      212325400
Email:   pate5400@mylaurier.ca
__updated__ = "2022-03-22"
-------------------------------------------------------
"""
# Imports
from morse import encode_morse, fill_letter_bst, DATA1
from BST_linked import BST
# Constants
bst = BST()
fill_letter_bst(bst, DATA1)

text = "My name is David Brown"
code = encode_morse(bst, text)
print(text)
print("encoded  bst ")
print(code)
