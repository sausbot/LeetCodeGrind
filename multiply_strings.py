'''
Leetcode Medium
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
https://leetcode.com/problems/multiply-strings/
'''


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Use ord() to get asciii value of the string
        # 0 -> 48
        # 1 -> 49
        # We can then multiply the two numbers
        return str(self.string_to_int(num1)*self.string_to_int(num2))
    
    def string_to_int(self,n):
        result = 0
        for i in range(len(n)):
            result = result*10+(ord(n[i])-48)
        return result


class Solution:
    def multiply(self, num1: str, num2: str):
        # From each string get each digit and its degree
        # The product is the sum of the product of each digit
        # with the correct degree
        # 
        # Assuming we cannot convert directly to int or
        # multiply the inputs directly

        ans = 0

        # Reverse the strings to get correct degree of digits 
        for i1, n1 in enumerate(num1[::-1]):
            for i2, n2 in enumerate(num2[::-1]):
                ans += (ord(n1) - 48) * (10**i1) * (ord(n2) - 48) * (10**i2)
        print(ans)
        return str(ans)

# test
s = Solution()
s.multiply("55","75")