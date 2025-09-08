def insertion_sort(arr, left, right):
    """
    Insertion Sort Algorithm
    ------------------------
    Sorts a portion of an array (from index 'left' to 'right') in ascending order.

    Parameters:
        arr (list): A list of comparable elements.
        left (int): The starting index of the subarray to be sorted.
        right (int): The ending index of the subarray to be sorted.

    Returns:
        None: The array is sorted in place.
    """
    # Iterate through the subarray starting from index `left + 1`
    for i in range(left + 1, right + 1):
        key = arr[i]      # The current element to be placed in correct position
        j = i - 1         # Index to compare backwards

        # Shift elements that are greater than `key` one position to the right
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Place the key element in its correct sorted position
        arr[j + 1] = key
