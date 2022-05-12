"""
Provide an encode and decode method for a given string

Solution from Timothy H Chang https://www.youtube.com/watch?v=qmkVXPJ-9YY
This is why he is a SWE and I am still job hunting :)
"""


class Solution:
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s))+ "#" + s
        print(res)
        return res
    
    def decode(self, str):
        res, i = [], 0

        while i < len(str):
            j = i

            # Loop till you get to the delimeter
            while str[j] != "#":
                j += 1
            print(i,j)
            # The length will be the substring from initial position to delimeter
            length = int(str[i:j])

            # Take substring ahead of delim index (j) to the length         
            res.append(str[j+1:j+1+length])

            # Increment i to new starting point
            i = j + 1 + length

        print(res)
        return res

# test
s = Solution()
encoded = s.encode(["the","very#","next","#"])
s.decode(encoded)