'''
Leetcode Medium
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.
https://leetcode.com/problems/sort-characters-by-frequency/
'''


class Solution:
    def frequencySort(self, s: str) -> str:
        # Make a list of unique characters
        char_counts = {}

        # Iterate through string and count letters
        # Assign unique values to dictionary
        for letter in s:
            if letter not in char_counts:
                char_counts[letter] = s.count(letter)
        
        print(char_counts)

        # Sort letters in descending order
        ordered = sorted(char_counts, key=char_counts.get, reverse = True)
        print(ordered)

        # Add the letters to the new string with correct frequencies
        new_str = ""
        for letter in ordered:
            new_str += letter * char_counts[letter]
        
        print(new_str)
        return new_str

# test
test = Solution()
test.frequencySort(s="tree")