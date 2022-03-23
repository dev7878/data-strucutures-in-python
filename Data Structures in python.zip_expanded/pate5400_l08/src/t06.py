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
from morse import DATA1, fill_code_bst, decode_morse
from BST_linked import BST
# Constants
bst = BST()
fill_code_bst(bst, DATA1)
code = "... --- ..."
text = decode_morse(bst, code)
print(code)
print("decoded")
print(text)
