def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
    Args:
       input_list(list): List to be sorted
    """
    next_0_pos = 0
    next_2_pos = len(input_list) - 1
    index = 0
    while index <= next_2_pos:
        current_value = input_list[index]
        if current_value == 0:
            input_list[index] = input_list[next_0_pos]
            input_list[next_0_pos] = current_value
            next_0_pos += 1
            index += 1
        elif current_value == 2:
            input_list[index] = input_list[next_2_pos]
            input_list[next_2_pos] = current_value
            next_2_pos -= 1
        else:
            index += 1
    return input_list


print(sort_012([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]))
# should return [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]

print(sort_012([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]))
# should return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]

print(sort_012([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]))
# should return [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]

print(sort_012([]))
# should return []

print(sort_012([2]))
# should return [2]

print(sort_012([1]))
# should return [1]