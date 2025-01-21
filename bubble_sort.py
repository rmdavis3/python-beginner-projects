

def bubble_sort(list):
    total_swaps = 0
    for i, _ in enumerate(list):
        for j in range(0, len(list)-i-1):
            print(f"comparing {list[j]} against {list[j+1]}")
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                total_swaps += 1
    print(f"It took {total_swaps} swaps to sorted your list using buble sort.")
    return list


def main():
    """Main Program Flow"""
    unsorted_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(f"{unsorted_list}\n has now been sorted to...\n")
    sorted_list = bubble_sort(unsorted_list)
    print(sorted_list)


if __name__ == "__main__":
    main()
