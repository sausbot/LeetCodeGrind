"""
Given two strings, write a method to decide if one is a permutation of the other
"""


def is_permutation(s1: str, s2: str):
    # case sensitive input, whitespace sensitive
    s1 = s1.lower().strip(" ")
    s2 = s2.lower().strip(" ")
    # a permutation implies (1) that all the characters found in one string are present in the other and (2) have the same length
    # we can convert both strings to dicts and check that the value counts for each of their letters are the same
    is_perm = False
    if len(s1) != len(s2):
        print("uneven length")
        return is_perm

    s1_dict = {}
    s2_dict = {}

    for i in range(len(s1)):
        s1_val = s1[i]
        s2_val = s2[i]
        s1_dict[s1_val] = s1.count(s1_val)
        s2_dict[s2_val] = s2.count(s2_val)

    for key, value in s2_dict.items():
        if not s1_dict.get(key, False):
            print(f"{key} not present in {s1_dict}")
            return is_perm

        if key in s1_dict and s1_dict[key] != value:
            print(f"{key}:{value} not equal to value in {s1_dict}")
            return is_perm

    is_perm = True
    print(is_perm)
    return is_perm


def is_permutation(s1: str, s2: str):
    # case sensitive input, whitespace sensitive
    s1 = s1.lower().strip(" ")
    s2 = s2.lower().strip(" ")

    # sorting the strings would make them even if they are a permutation
    s1_sorted = "".join(sorted(s1))
    s2_sorted = "".join(sorted(s2))

    print(s1_sorted == s2_sorted)
    return s1_sorted == s2_sorted


is_permutation("aab", "baa")  # True
is_permutation("fgh", "fg")  # False (uneven length)
is_permutation("abc", "bac")  # True
is_permutation("fad", "fba")  # False (val no present)
is_permutation("ccba", "cba")  # False (uneven length)
is_permutation("A bc", "ab c")  # True
