def bubble_sort(array):
    """
    Sorts a list using the Bubble Sort algorithm.

    Parameters:
    array (list): The list of numbers to be sorted.

    Returns:
    list: The sorted list.
    """
    total_swaps = 0
    n = len(array)

    for i in range(n):
        swapped = False  # Optimization: Track if a swap occurs

        for j in range(n - i - 1):
            # print(f"Comparing {array[j]} against {array[j+1]}")
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                total_swaps += 1
                swapped = True  # Swap occurred
                print(array)

        # If no swaps were made, the list is already sorted
        if not swapped:
            break

    print(f"It took {total_swaps} swaps to sort your list using bubble sort.")
    return array


def selection_sort(array):
    """
    Sorts a list using the Selection Sort algorithm.
    """
    swap_count = 0  # Initialize swap counter
    for i in range(len(array)-1):
        lowest_value_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[lowest_value_index]:
                lowest_value_index = j
        if lowest_value_index != i:
            array[i], array[lowest_value_index] = array[lowest_value_index], array[i]
            swap_count += 1  # Increment swap count when a swap happens
            print(array)

    print(f"Selection Sort took {swap_count} swaps.")
    return array


def insertion_sort(array):
    """
    Sorts a list using the Insertion Sort algorithm.
    """
    shift_count = 0  # Count actual shifts
    for i in range(1, len(array)):
        temp_value = array[i]
        position = i - 1

        # Shift elements to the right only if necessary
        while position >= 0 and array[position] > temp_value:
            array[position + 1] = array[position]  # Shift right
            position -= 1  # Move left
            shift_count += 1  # Count the shift

        # Insert temp_value in the correct position
        array[position + 1] = temp_value
        print(array)

    print(f"Insertion Sort took {shift_count} shifts.")
    return array


def main():
    """Main Program Flow"""

    unsorted_array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    # Test Bubble Sort
    print("Testing Bubble Sort:")
    print(f"Original Array: {unsorted_array}")
    # Create a copy to preserve the original array
    bubble_sorted_array = unsorted_array.copy()
    bubble_sort(bubble_sorted_array)
    print(f"Bubble Sorted Array: {bubble_sorted_array}\n")

    print()

    # Test Selection Sort
    print("Testing Selection Sort:")
    print(f"Original Array: {unsorted_array}")
    # Create a copy to preserve the original array
    selection_sorted_array = unsorted_array.copy()
    selection_sort(selection_sorted_array)
    print(f"Selection Sorted Array: {selection_sorted_array}")

    print()

    # Test Selection Sort
    print("Testing Selection Sort:")
    print(f"Original Array: {unsorted_array}")
    # Create a copy to preserve the original array
    insertion_sorted_array = unsorted_array.copy()
    insertion_sort(insertion_sorted_array)


if __name__ == "__main__":
    main()
