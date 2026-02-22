"""
Design an algorithm to find all pairs of integers within an array which sum to a specified values
"""


def pair_with_sum(lst: list, value: int):

    pairs = []

    elem = 1
    for i in lst:
        for j in lst[elem:]:
            if i + j == value:
                pairs.append((i, j))
        elem += 1

    print(pairs)


pair_with_sum([0, 2, 3, 4, 7, 9, 12], 7)
