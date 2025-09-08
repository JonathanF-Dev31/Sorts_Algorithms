def merge_sort(arr, left, right):
    """
    Merge Sort Algorithm
    --------------------
    Recursively divides the array into halves, sorts each half, 
    and then merges the sorted halves.

    Parameters:
        arr (list): A list of comparable elements.
        left (int): The starting index of the subarray to be sorted.
        right (int): The ending index of the subarray to be sorted.

    Returns:
        None: The array is sorted in place.
    """
    if left < right:
        # Find the middle index
        mid = (left + right) // 2

        # Recursively sort the first half
        merge_sort(arr, left, mid)

        # Recursively sort the second half
        merge_sort(arr, mid + 1, right)

        # Merge the two sorted halves
        merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    """
    Merge Helper Function
    ---------------------
    Merges two sorted subarrays into one sorted array.

    Parameters:
        arr (list): The original array containing two sorted subarrays.
        left (int): Starting index of the first subarray.
        mid (int): Ending index of the first subarray.
        right (int): Ending index of the second subarray.

    Returns:
        None: The array is modified in place.
    """
    # Create temporary subarrays
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    # Initialize pointers
    i = j = 0     # Pointers for left and right subarrays
    k = left      # Pointer for the main array

    # Merge elements back into the main array
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    # Copy any remaining elements from the left subarray
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    # Copy any remaining elements from the right subarray
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1
