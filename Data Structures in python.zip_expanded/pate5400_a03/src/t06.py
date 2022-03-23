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
from functions import reroute
# Constants
values_in = ["car1", "car2"]
opstring = "SXSX"
opstring = opstring.upper()
print(f"in values:{values_in}")
print(f"opstring:{opstring}")
values_out = reroute(opstring, values_in)
print(f"values out:{values_out}")
