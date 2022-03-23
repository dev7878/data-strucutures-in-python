"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Dev patel
ID:      212325400
Email:   pate5400@mylaurier.ca
__updated__ = "2022-03-11"
-------------------------------------------------------
"""
# Imports
import random
# Constants


def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    x = 0
    output = []
    j = len(values)
    for i in values:
        if i not in output:
            output.append(i)
    values.extend(output)
    del values[0:j]

    return


def dsmvwl(s):
    """
    -------------------------------------------------------
    Disemvowels a string. out contains all the characters in s
    that are not vowels. ('y' is not considered a vowel.) Case is preserved.
    Use: out = dsmvl(s)
    -------------------------------------------------------
    Parameters:
       s - a string (str)
    Returns:
       out - s with the vowels removed (str)
    -------------------------------------------------------
    """
    out = ""
    for i in s:
        if i not in "aeiouAEIOU":
            out += i
    return out


def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """

    u = 0
    l = 0
    d = 0
    w = 0

    for i in fv:
        for j in i:
            if j.isupper():
                u += 1
            elif j.islower():
                l += 1
            elif j.isdigit():
                d += 1
            elif j.isspace():
                w += 1
    r = u + l + d + w
    return u, l, d, w, r


def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    if year % 400 == 0:
        leap_year = True
    elif year % 4 == 0 and year % 100 != 0:
        leap_year = True
    else:
        leap_year = False
    return leap_year


def is_palindrome(s):
    """
    -------------------------------------------------------
    Determines if s is a palindrome. Ignores case, spaces, and
    punctuation in s.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    s = s.lower()
    rev = s[::-1]

    if s == rev:
        palindrome = True
    else:
        palindrome = False
    return palindrome


def max_diff(a):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    a must be unchanged.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of int)
    Returns:
        md - the largest absolute difference between adjacent
            values in a list (int)
    -------------------------------------------------------
    """
    x = 0
    y = 1
    md = 0
    for i in a:
        while x < len(a) and y < len(a):
            diff = a[y] - a[x]
            x += 1
            y += 1
            if diff > md:
                md = diff
            else:
                md = md
    return md


def generate_matrix_char(rows, cols):
    """
    -------------------------------------------------------
    Generates a 2D list of random numbers
    Use: matrix = generate_matrix_char(rows, cols)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the generated matrix (int > 0)
        cols - number of columns in the generated matrix (int > 0)
    Returns:
        matrix - a 2D list of random characters (2D list of int)
    -------------------------------------------------------
    """
    count = 0

    stri = "123456789"

    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(0, cols):
            char = random.choice(stri)
            matrix[count].append(char)
        count += 1

    return matrix


def print_matrix_char(matrix):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list of strings in a formatted table.
    Prints row and column headings.
    Use: print_matrix_char(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of strings (2D list)
    Returns:
        None.
    -------------------------------------------------------
    """
    print(" ", end=" ")
    for x in range(len(matrix[0])):
        print(f"{x:>6d}", end="")
    print()
    for x in range(len(matrix)):
        print(f"{x:>1.0f}", end=" ")
        for y in range(len(matrix[0])):
            print(f"{matrix[x][y]:>6s}", end="")
        print()
    return


def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """
    count = 0
    b = []
    for i in range(len(a[0])):
        b.append([])
        for j in range(len(a)):
            num = a[j][i]
            b[count].append(num)
        count += 1
    return b


def matrix_stats(a):
    """
    -------------------------------------------------------
    Determines the smallest, largest, total, and average of
    the values in the 2D list a. You may assume there is at
    least one value in a.
    a must be unchanged.
    Use: small, large, total, average = matrix_stats(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list of numbers (2D list of float)
    Returns:
        small - the smallest number in a (float)
        large - the largest number in a (float)
        total - the total of all numbers in a (float)
        average - the average of all numbers in a (float)
    -------------------------------------------------------
    """
    small = a[0][0]
    large = a[0][0]
    total = 0
    average = 0
    count = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            num = a[i][j]
            if num < small:
                small = num
            elif num > large:
                large = num
            total += int(num)
            count += 1

    average = total / count
    return small, large, total, average


def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move the leading consonants to
    the end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """
    back = ""
    pl = ""
    i = 0
    if word[0] in "aeiouAEIOU":
        pl = word + "way"
    else:
        for j in word:
            pl = pl + j
        while word[i] not in "aeiouAEIOU":
            back = back + word[i]
            pl = pl.replace(word[i], "")
            i += 1
        if word[0] == word[0].upper():
            pl = pl.capitalize() + back.lower() + "ay"
        else:
            pl = pl + back.lower() + "ay"
    return pl
