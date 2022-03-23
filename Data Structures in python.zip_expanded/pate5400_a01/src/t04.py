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
from functions import is_leap_year
# Constants
year = int(input("Enter the year"))
leap_year = is_leap_year(year)
print(f"{leap_year}")
