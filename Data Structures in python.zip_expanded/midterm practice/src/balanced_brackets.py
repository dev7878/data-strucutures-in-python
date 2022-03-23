"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Dev Patel
ID:      212325400
Email:   pate5400@mylaurier.ca
__updated__ = "2022-02-14"
-------------------------------------------------------
"""
# Imports

# Constants
from Stack_array import Stack


def balanced_brackets(s):
    """
    -------------------------------------------------------
    Determines whether a string contains balanced brackets or not.
    Must use a Stack to do so.
    Use: b = balanced_brackets(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
    is_balanced - true or bool (type)
    ------------------------------------------------------
    """
    st = Stack()
    bal = True
    id = 0
    while id < len(s)and bal:
        sym = s[id]
        if sym in "{([":
            st.push(sym)
        elif sym == ")":
            v = st.pop()
            if v != "(":
                bal = False
        elif sym == "}":
            v = st.pop()
            if v != "{":
                bal = False
        elif sym == "[":
            v = st.pop()
            if v != "]":
                bal = False
        id += 1
        if not st.is_empty():
            bal = False

    return bal


s = "[{}]"
b = balanced_brackets(s)
print(b)
