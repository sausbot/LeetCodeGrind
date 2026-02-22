"""
Write a function to swap two numbers in place without temporary variables
"""


def number_swap(num_1: int, num_2: int):
    print(f"Initial: {num_1}, {num_2}")
    # If they are the same, simply return the numbers
    if num_1 == num_2:
        return num_1, num_2

    num_1 = num_1 + num_2
    # num_2 = (num_1 + num_2) - num_2 = num_1
    num_2 = num_1 - num_2
    # num_1 = (num_1 + num_2) - num_1 = num_2
    num_1 = num_1 - num_2

    print(f"Final: {num_1}, {num_2}")


number_swap(5, 10)
number_swap(2, 3)
number_swap(7, 15)
