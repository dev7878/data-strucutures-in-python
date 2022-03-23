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
from functions import generate_matrix_char, print_matrix_char, matrix_stats
# Constants

rows = int(input("number of rows:"))
cols = int(input("number of columns:"))
a = generate_matrix_char(rows, cols)
print(f" matrix is ")
print_matrix_char(a)

small, large, total, average = matrix_stats(a)
print(f"""small:{small}
large:{large}
total:{total}
average:{average}""")
