def selection_sort(arr):
    """
    Selection Sort Algorithm
    ------------------------
    Sorts a list of elements in ascending order by repeatedly
    finding the minimum element from the unsorted portion
    and placing it at the beginning.

    Parameters:
        arr (list): The list of elements to be sorted.

    Returns:
        list: The sorted list in ascending order.
    """
    for i in range(0, len(arr) - 1):
        # Assume the current index holds the smallest value
        current_min_index = i
        
        # Find the index of the smallest element in the remaining unsorted part
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[current_min_index]:
                current_min_index = j

        # Swap the found minimum with the element at index i
        arr[i], arr[current_min_index] = arr[current_min_index], arr[i]
    
    return arr
