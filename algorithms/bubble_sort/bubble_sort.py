def bubble_sort(arr):
    """
    Bubble Sort Algorithm
    ---------------------
    This function sorts a list of numbers in ascending order 
    using the Bubble Sort algorithm.

    Parameters:
        arr (list): A list of comparable elements (e.g., integers or floats).

    Returns:
        list: The sorted list in ascending order.
    """

    # A flag to track whether the array is already sorted
    sort = False
    
    # Continue looping until no swaps are needed (array is sorted)
    while sort == False:
        sort = True  # Assume the array is sorted
        
        # Iterate through the array comparing adjacent elements
        for i in range(0, len(arr) - 1):
            # If the current element is greater than the next, swap them
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sort = False  # A swap occurred, so the array was not sorted
    
    return arr
