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
from functions import file_analyze


fv = open("word.txt", "r", encoding="utf-8")

print("file_analyze(fh) →")
stats = file_analyze(fv)
print(f"{stats}")
fv.close()
