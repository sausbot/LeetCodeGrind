'''
Add two strings that contain integer values
'''


def add_strings(num1: str, num2: str):
    # Can use ord() to get ascii value of str
    # 0 -> 48
    # 1 -> 49
    a_index = len(num1)-1
    b_index = len(num2)-1

    carry = 0
    output = ""
    while a_index >= 0 or b_index >=0:
        value_a = 0
        value_b = 0

        # Get the integer value by subtracting 48
        if a_index >= 0:
            value_a = ord(num1[a_index])-48
            a_index-=1
        if b_index >= 0:
            value_b=ord(num2[b_index])-48
            b_index-=1

        # Add the integer outputs plus the carry
        temp_output = value_a + value_b + carry

        # Compute the next carry value
        if temp_output > 9:
            carry = 1
        else:
            carry = 0

        # Change back to str representation taking last element in str
        output = str(temp_output)[-1] + output
    
    # Take care of last carry case
    if carry:
        output = "1"+output
    print(output)
    return output

# test
add_strings("111","779")