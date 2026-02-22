"""
Given an array of integers, return the index of any two numbers that add up to a target.
The order of the indices in the result doesn't matter. If no pair is found, return an empty array
"""


def pair_sum(numbers, target):
    map = {}
    for i in range(len(numbers)):
        value = numbers[i]
        complement = target - value
        if complement not in map:
            map[value] = i
        else:
            return [i, map[complement]]

    return []


def pair_sum_optimized(numbers, target):
    map = {}
    for i, x in enumerate(numbers):
        if target - x in map:
            return [map[target - x], i]
        map[x] = i
    return []
