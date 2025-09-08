import math

def counting_sort_for_radix(arr, digit):
    """
    Counting Sort (for Radix Sort)
    ------------------------------
    A stable version of Counting Sort that sorts elements 
    based on a specific digit.

    Parameters:
        arr (list): List of non-negative integers to be sorted.
        digit (int): Current digit position to sort by (0 = least significant digit).

    Returns:
        list: A new list sorted according to the given digit.
    """
    base_10 = 10 ** digit             # Determine the place value (1, 10, 100, ...)
    new_array = [[] for _ in range(10)]  # Buckets for digits 0-9

    # Place each number into the corresponding bucket based on the current digit
    for value in arr:
        digit_value = (value // base_10) % 10
        new_array[digit_value].append(value)
    
    # Flatten buckets back into a single list
    result = []
    for bucket in new_array:
        result.extend(bucket)
    return result


def radix_sort(arr):
    """
    Radix Sort Algorithm
    --------------------
    Sorts a list of non-negative integers using the Radix Sort algorithm.
    It applies Counting Sort to each digit, starting from the least significant
    digit to the most significant digit.

    Parameters:
        arr (list): List of non-negative integers to be sorted.

    Returns:
        list: The sorted list (ascending order).
    """
    max_value = max(arr)  # Find the largest number to know max digits
    max_digits = int(math.log10(max_value)) + 1 if max_value > 0 else 1

    # Apply counting sort for each digit (LSD → MSD)
    for digit in range(max_digits):
        arr[:] = counting_sort_for_radix(arr, digit)

    return arr
