def bubble_sort(arr):
    # Set a flag to indicate whether any swaps were made
    swapped = True

    # Keep looping until no swaps are made
    while swapped:
        # Set the flag to False
        swapped = False

        # Loop through the array and compare each pair of adjacent elements
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                # Swap the elements
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                # Set the flag to True to indicate that a swap was made
                swapped = True

    # Return the sorted array
    return arr


# Example usage
my_list = [5, 2, 7, 1, 3]
print(bubble_sort(my_list))  # [1, 2, 3, 5, 7]
