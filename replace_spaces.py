"""
Write a method to replace all spaces in a string with '%20'
"""


def replace_spaces(s):
    # Remove trailing whitespace
    s = s.strip()

    # Add characters and replace spaces
    new_str = ""
    last_char_is_whitespace = False
    for i in s:
        if i == " ":
            if not last_char_is_whitespace:
                new_str += "%20"
                last_char_is_whitespace = True
        else:
            new_str += i
            last_char_is_whitespace = False

    print(new_str)
    return new_str


replace_spaces("Mr John Smith  ")
replace_spaces("Michelle  Obama      ")
