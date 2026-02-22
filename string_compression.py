"""
Implement a method to perform basic string compression using the counts of repeated characters.
If the compressed string would not become smaller than the original string then retun the original.
You can assume that the string only has uppercase and lowercase letters (a-z).
"""

# Do we count upper and lowercase seperately for same char?


def unique_characters(s: str):
    chars = {}
    s = s.lower()
    is_unique = True
    for val in s:
        if val in chars:
            chars[val] += 1
        else:
            chars[val] = 1

    return chars


def compress_string(s: str):
    new_str = ""
    counts = unique_characters(s)
    for key, value in counts.items():
        new_str += f"{key}{value}"

    if len(s) < len(new_str):
        print(s)
        return s

    print(new_str)
    return new_str


compress_string("aaabbc")
compress_string("abc")
compress_string("abccccc")
