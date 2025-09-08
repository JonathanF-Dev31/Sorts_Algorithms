def partition(array, start, end):
    """
    Partition Function
    ------------------
    Places the pivot element at its correct sorted position 
    and ensures that all elements smaller than the pivot are 
    on the left, and all greater elements are on the right.

    Parameters:
        array (list): The list of comparable elements.
        start (int): Starting index of the subarray.
        end (int): Ending index of the subarray.

    Returns:
        int: The index of the pivot after partitioning.
    """
    pivot = array[start]   # Choose the first element as the pivot
    low = start + 1        # Pointer for elements greater than pivot
    high = end             # Pointer for elements less than pivot

    while True:
        # Move 'high' leftward until finding a value < pivot
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Move 'low' rightward until finding a value > pivot
        while low <= high and array[low] <= pivot:
            low = low + 1

        # Swap elements if out of order
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    # Place pivot in its correct position
    array[start], array[high] = array[high], array[start]

    return high


def quick_sort(array, start, end):
    """
    Quick Sort Algorithm
    --------------------
    Sorts an array in ascending order using the Quick Sort algorithm.
    It partitions the array around a pivot and recursively sorts the subarrays.

    Parameters:
        array (list): A list of comparable elements.
        start (int): Starting index of the subarray to sort.
        end (int): Ending index of the subarray to sort.

    Returns:
        None: The array is sorted in place.
    """
    if start >= end:
        return

    # Partition the array and get pivot index
    p = partition(array, start, end)

    # Recursively apply quicksort to the left and right subarrays
    quick_sort(array, start, p - 1)
    quick_sort(array, p + 1, end)
