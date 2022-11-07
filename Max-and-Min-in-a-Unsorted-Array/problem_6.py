"""
Solution of;
Project: Problems vs Algorithms
Problem 6: Unsorted Integer Array
"""


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
    ints(list): list of integers containing one or more integers
    """

    # intialize max and min variables
    min = ints[0]
    max = ints[0]

    for integer in ints:

        if integer < min:
            min = integer
        elif integer > max:
            max = integer

    return min, max


# Example Test Case of Ten Integers
import random

# test 1
test_list = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(test_list)

print("Pass" if ((0, 9) == get_min_max(test_list)) else "Fail")  # Pass

# test 2
test_list = [0, 0, 0, 0]
print("Pass" if ((0, 0) == get_min_max(test_list)) else "Fail")  # Pass

# test 3
test_list = [11111, 0, 3, 99]
print("Pass" if ((0, 11111) == get_min_max(test_list)) else "Fail")  # Pass

# test 4
test_list = [101, 101, 101, 1, 70]
print("Pass" if ((1, 101) == get_min_max(test_list)) else "Fail")  # Pass
