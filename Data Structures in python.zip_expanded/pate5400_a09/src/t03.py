"""
-------------------------------------------------------
[Functions]
-------------------------------------------------------
Author:  Dev Patel
ID:      212325400
Email:   pate5400@mylaurier.ca
__updated__ = "2022-03-21"
-------------------------------------------------------
"""
from Hash_Set_BST import Hash_Set
from functions import insert_words, comparison_total

fv = open("otoos610.txt", "r", encoding="utf-8")
hs = Hash_Set(20)
insert_words(fv, hs)
total, max_word = comparison_total(hs)

print("Using Linked BST Hash_Set")
print()
print("Total Comparisons: {:,}".format(total))
print("Word with maximum comparisons '{}': {:,}".format(
    max_word.word, max_word.comparisons))
