"""
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""


def unique_characters_1(s: str):
    # string to dict while counting occurance of elements
    # d = {k+1: v for k, v in enumerate(chars, 1)}
    # check for higher counts than 1
    chars = {}
    for val in s:
        if val in chars:
            chars[val] += 1
        else:
            chars[val] = 1

    print(chars)

    is_unique = True
    for _, value in chars.items():
        if value > 1:
            is_unique = False

    print(is_unique)
    return is_unique


def unique_characters_2(s: str):
    chars = []
    is_unique = True
    for val in s:
        if val in chars:
            is_unique = False
        chars.append(val)

    print(is_unique)
    return is_unique


def unique_characters_3(s: str):
    # compare each character to the other characters in the string
    # does not use additional data structures but increases time
    # complexity because of nested for loops O(N^2)
    is_unique = True
    for i, val in enumerate(s):
        for j in s[i + 1 : :]:
            if j == val:
                is_unique = False
    return is_unique


unique_characters_3("abc")
unique_characters_3("abbc")
unique_characters_3("bbbb")
