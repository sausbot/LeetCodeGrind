'''
Leetcode Easy
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
Return any array that satisfies this condition.
https://leetcode.com/problems/sort-array-by-parity
'''


def sort_array_parity(nums: list):
    even, odd = 0,1
    n = len(nums)

    while even<n and odd<n:
        while even<n and nums[even]%2==0:
            even+=2
        while odd<n and nums[odd]%2!=0:
            odd+=2
        # Swap numbers if we find an out of place number
        if even<n and odd<n:
            nums[even], nums[odd] = nums[odd], nums[even]
        even+=2
        odd+=2
    print(nums)
    return nums

# test
sort_array_parity([3,2,4,7,8,9])