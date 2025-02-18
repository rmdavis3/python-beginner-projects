def linear_search_sorted_array(sorted_array, search_value):
    """
    Performs a linear search on a sorted array to find a given value.

    Since the array is sorted, the function exits early if it encounters a value 
    greater than the search target, improving efficiency.

    Parameters:
    sorted_array (list): A sorted list of elements to search through.
    search_value (any): The value to search for in the array.

    Returns:
    str: A message indicating whether the value was found and its index, 
         or that it was not found.
    """
    for index, value in enumerate(sorted_array):
        if value == search_value:
            return f"I found your value {search_value} in the array at index {index}."
        elif value > search_value:
            break  # Early exit for sorted arrays

    return f"I did not find your value {search_value} in the array."


def binary_search_sorted_array(sorted_array, search_value):
    """
    Performs a binary search on a sorted array to find a given value.

    Parameters:
    sorted_array (list): A sorted list of elements to search through.
    search_value (any): The value to search for in the array.

    Returns:
    str: A message indicating whether the value was found and its index, 
         or that it was not found.
    """
    lower_bound = 0
    upper_bound = len(sorted_array) - 1

    while lower_bound <= upper_bound:
        midpoint = (upper_bound + lower_bound) // 2
        if search_value == sorted_array[midpoint]:
            return f"I found your value {search_value} in the array at index {midpoint}."
        elif search_value < sorted_array[midpoint]:
            upper_bound = midpoint - 1
        else:
            lower_bound = midpoint + 1

    return f"I did not find your value {search_value} in the array."


print(linear_search_sorted_array([3, 17, 22, 75, 80, 202], 22))  # Found case
print(linear_search_sorted_array(
    [3, 17, 22, 75, 80, 202], 24))  # Not found case


print()


print(binary_search_sorted_array([3, 17, 22, 75, 80, 202], 22))  # Found case
print(binary_search_sorted_array(
    [3, 17, 22, 75, 80, 202], 24))  # Not found case
