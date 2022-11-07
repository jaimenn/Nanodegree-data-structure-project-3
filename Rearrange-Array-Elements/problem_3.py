"""
Solution of;
Project: Problems vs Algorithms
Problem 3: Rearrange Array Digits
"""


# mergesort function
def mergesort(items):

    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left, right):

    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    input_list = mergesort(input_list)

    i = len(input_list) - 1

    out_1 = ""
    out_2 = ""

    while i >= 0:

        if i % 2 == 0:
            out_1 += str(input_list[i])

        else:
            out_2 += str(input_list[i])

        i -= 1

    if out_1 > out_2:

        return list(map(int, [out_1, out_2]))

    return list(map(int, [out_2, out_1]))


# test_case[0] is the list that we want to test
# test_case[1] is the result that we expect
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])

test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

test_function([[0, 9], [9, 0]])

test_function([[0, 8, 3], [80, 3]])
