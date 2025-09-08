from algorithms.insertion_sort.insertion_sort import insertion_sort
from algorithms.merge_sort.merge_sort import merge

# Minimum run size (used to divide the array into small chunks)
MIN_RUN = 32

def tim_sort(arr):
    """
    TimSort Algorithm
    -----------------
    A hybrid sorting algorithm derived from Merge Sort and Insertion Sort.
    It is the default sorting algorithm in Python (list.sort()) and Java (Arrays.sort()).

    TimSort works in two phases:
    1. Break the array into small chunks ("runs") of size MIN_RUN and sort
       each run using Insertion Sort (efficient for small arrays).
    2. Iteratively merge runs using a process similar to Merge Sort until the
       whole array is sorted.

    Parameters:
        arr (list): The list of elements to be sorted.

    Returns:
        None: The input array is sorted in place.
    """
    n = len(arr)

    # Step 1: Sort small chunks with Insertion Sort
    for start in range(0, n, MIN_RUN):
        end = min(start + MIN_RUN - 1, n - 1)
        insertion_sort(arr, start, end)

    # Step 2: Merge chunks iteratively like Merge Sort
    size = MIN_RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), n - 1)

            # Merge subarrays if they exist
            if mid < right:
                merge(arr, left, mid, right)

        size *= 2 # Double the size for the next iteration
