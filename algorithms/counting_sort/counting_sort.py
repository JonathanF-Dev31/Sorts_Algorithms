def counting_sort(arr):
    """
    Counting Sort Algorithm
    -----------------------
    Sorts a list of integers by counting the number of occurrences 
    of each unique element and then reconstructing the sorted array.

    Parameters:
        arr (list): A list of integers (works best when the range between 
                    min and max values is not significantly larger than 
                    the number of elements).

    Returns:
        list: The sorted list in ascending order.
    """
    # Find the minimum and maximum values in the array
    min_value = min(arr)
    max_value = max(arr)

    # Initialize the counting array with zeros
    # Size is based on the range of values (min to max)
    count_array = [0 for _ in range(min_value, max_value + 1)]

    # Count the occurrences of each element
    for value in arr:
        count_array[value - min_value] += 1
    
    # Reconstruct the sorted array
    sorted_arr = []
    for i, item in enumerate(count_array):
        # Append the value (i + min_value) 'item' times
        sorted_arr.extend([i + min_value] * item)
    
    # Copy sorted values back to the original array
    arr[:] = sorted_arr
    return arr
