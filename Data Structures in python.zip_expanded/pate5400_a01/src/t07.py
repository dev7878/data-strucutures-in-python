"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Dev Patel
ID:      212325400
Email:   pate5400@mylaurier.ca
__updated__ = "2022-03-11"
-------------------------------------------------------
"""
# Imports
from functions import matrix_transpose, generate_matrix_char, print_matrix_char
# Constants
rows = int(input("number of rows:"))
cols = int(input("number of columns:"))
a = generate_matrix_char(rows, cols)
print(f"The original matrix is ")
print_matrix_char(a)
print(f"----------------------------")
b = matrix_transpose(a)
print_matrix_char(b)
