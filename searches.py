# Assumes array is sorted
def linear_search(array, search_value):
    for index, element in enumerate(array):
        if element == search_value:
            return index
        elif element > search_value:
            break
    return None


def binary_search(array, search_value):

    lower_bound = 0
    upper_bound = len(array)-1

    while lower_bound <= upper_bound:

        midpoint = (upper_bound + lower_bound) // 2
        value_at_midpoint = array[midpoint]

        if search_value == value_at_midpoint:
            return midpoint
        elif search_value < value_at_midpoint:
            upper_bound = midpoint - 1
        elif search_value > value_at_midpoint:
            lower_bound = midpoint + 1

    return None


print(linear_search([3, 17, 22, 75, 80, 202], 22))

print(binary_search([3, 17, 22, 75, 80, 22, 202], 22))
