"""
There are three types of edits that can be performed on strings: insert a char, remove a char or replace a char,
write a function to check if they are one edit (or zero edits) away
"""


def one_away(s1, s2):
    len_1 = len(s1)
    len_2 = len(s2)

    # If diff of lengths more than 1
    # strings are not one edit away
    if abs(len_1 - len_2) > 1:
        return False

    count_edits = 0
