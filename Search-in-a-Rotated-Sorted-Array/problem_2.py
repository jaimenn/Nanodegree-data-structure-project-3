"""
Solution of;
Project: Problems vs Algorithms
Problem 2: Search in a Rotated Sorted Array
"""


def binary_search(arr, low, high, target):
    """
    return the target eleents index
    if it is not exists return -1
    """

    if low > high:
        return -1

    mid_index = (low + high) // 2

    if arr[mid_index] == target:
        return mid_index

    elif arr[mid_index] > target:
        return binary_search(arr, low, mid_index - 1, target)

    return binary_search(arr, mid_index + 1, high, target)


def find_pivot(arr, low, high):
    """
    return the pivot element's index
    in the given array
    ex: if array is arr=[4,5,6,7,8,1,2,3]
    pivot element is 8 which's index is 4
    """

    if high < low:
        return -1

    if high == low:
        return low

    else:
        mid_index = (low + high) // 2

        if mid_index < high and arr[mid_index] > arr[mid_index + 1]:
            return mid_index

        if mid_index > low and arr[mid_index - 1] > arr[mid_index]:
            return mid_index - 1

        if arr[low] >= arr[mid_index]:
            return find_pivot(arr, low, mid_index - 1)

        return find_pivot(arr, mid_index + 1, high)


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
        input_list(array), number(int):
            Input array to search and the target
    Returns:
        int:
            Index or -1
    """

    if input_list == [] or number is None:
        return -1

    arr = input_list
    low = 0
    high = len(input_list) - 1
    target = number

    pivot_index = find_pivot(arr, low, high)

    # if pivot_index is -1 then arr is not rotated
    if pivot_index == -1:
        return binary_search(arr, low, high, target)

    else:

        # if pivot_index element equals to target
        # return pivot_index
        if arr[pivot_index] == target:
            return pivot_index

        # if target element is grater than 0th element
        # search for left half
        if target >= arr[0]:
            return binary_search(arr, 0, pivot_index - 1, target)

        # if mid element is smaller than 0th element
        # search right half
        return binary_search(arr, pivot_index + 1, high, target)


def linear_search(input_list, number):
    if input_list == [] or number is None:
        return -1
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[9999], 9999])
test_function([[], 9999])
test_function([[], None])
