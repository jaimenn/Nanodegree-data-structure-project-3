"""
Solution of;
Project: Problems vs Algorithms
Problem 1: Square Root of an Integer
"""


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if number == 0 or number == 1:
        return number

    first = 0
    last = number
    mid = 0
    mid_list = [mid]  # it is like a cache to look for last mid

    while last > first:

        mid = (first + last) // 2

        if mid_list[-1] == mid:
            break

        square = mid * mid

        if square > number:
            last = mid

        elif square < number:
            first = mid

        mid_list.append(mid)

    return mid


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (876 == sqrt(767452)) else "Fail")
