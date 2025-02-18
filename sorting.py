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
            print(f"Comparing {array[j]} against {array[j+1]}")
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                total_swaps += 1
                swapped = True  # Swap occurred

        # If no swaps were made, the list is already sorted
        if not swapped:
            break

    print(f"It took {total_swaps} swaps to sort your list using bubble sort.")
    return array


def main():
    """Main Program Flow"""
    unsorted_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(f"{unsorted_list}\nhas now been sorted to...\n")
    sorted_list = bubble_sort(unsorted_list)
    print(sorted_list)


if __name__ == "__main__":
    main()
