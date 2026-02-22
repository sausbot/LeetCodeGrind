from operator import le


def palindrome(input):
    # remove special characters and spacing
    s = "".join(e for e in input if e.isalnum())
    print(s)

    # convert everything to lowercase
    s = s.lower()

    # Get the length of the string, calc midpint
    # remember 0 indexing
    length = len(s)
    print(length)

    # if odd stop before midpoint character
    if length % 2 != 0:
        midpoint = (length - 1) / 2
    else:
        midpoint = length / 2
    print(midpoint)

    # compare first and last chars
    # abcba, compare a to a, b to b, saved c, this is a palindrome
    for i in range(int(midpoint)):
        if s[i] != s[length - i - 1]:
            print("This is not a palindrome")
            return False

    print("This is a palindrome")
    return True


# palindrome("AAab--cbaAA")

import re


def isPalindrome(s: str) -> bool:
    s = re.sub("[^a-z0-9]", "", s.lower())
    return s == "".join(reversed(s))


ans = isPalindrome("abpa")
print(ans)
