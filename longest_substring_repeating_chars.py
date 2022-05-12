'''
Leetcode Medium
Given a string s, find the length of the longest substring without repeating characters.
https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''


class Solution:
    # Longest substring without repeating characters
    # Hashmap, pointer
    def lengthOfLongestSubstring(self,s:str):
        start = 0
        maxlen = 0
        lookup = {}

        for i, c in enumerate(s):
            if c in lookup and start <= lookup[c]:
                start = lookup[c] + 1
            else:
                maxlen = max(maxlen, i-start+1)
            lookup[c] = i

        return maxlen
    
    # Longest substring of repeating characters
    def longestSubstring(self, s:str):
        # "aaaababc" 
        # Keep track of max count, max char, and prev char
        max_count = 0
        max_char = ""
        prev_char = ""

        # Iterate through the string and count the consecutive
        for character in str:
            if character == prev_char:
                count += 1
            if count > max_count:
                max_count = count
                max_char = character
            prev_char = character
        
        return max_count
