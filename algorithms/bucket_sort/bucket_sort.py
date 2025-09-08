def create_buckets(arr):
    """
    Create buckets for Bucket Sort.

    Parameters:
        arr (list): A list of comparable numeric elements.

    Returns:
        tuple: 
            - buckets (list of lists): A list of empty buckets to distribute the elements.
            - size (float): The range size used to determine the bucket index.
    """
    max_value = max(arr)        # Get the maximum value in the array
    length = len(arr)           # Total number of elements in the array
    size = max_value / length   # Determine the interval size for each bucket

    # Create a list of empty buckets
    buckets = [[] for _ in range(length)]

    return buckets, size


def add_elements_to_buckets(arr, buckets, size): 
    """
    Distribute the elements into their corresponding buckets.

    Parameters:
        arr (list): The original unsorted list.
        buckets (list): A list of empty buckets.
        size (float): The range size to calculate the bucket index.

    Returns:
        list: Buckets filled with elements distributed according to their value.
    """
    for i in range(len(arr)): 
        # Find the index for the current element
        index = int(arr[i] / size)
        
        # If index is within range, add element to that bucket
        if index != len(arr): 
            buckets[index].append(arr[i]) 
        else: 
            # Handle the edge case where the element equals the max_value
            buckets[len(arr) - 1].append(arr[i]) 
    
    return buckets


def bucket_sort(arr):
    """
    Bucket Sort Algorithm
    ---------------------
    Sorts a list of numbers by distributing them into several buckets,
    sorting each bucket individually, and then concatenating the results.

    Parameters:
        arr (list): A list of comparable numeric elements.

    Returns:
        list: The sorted list in ascending order.
    """
    # Step 1: Create empty buckets
    buckets, size = create_buckets(arr)

    # Step 2: Distribute elements into buckets
    buckets = add_elements_to_buckets(arr, buckets, size)

    # Step 3: Sort each bucket individually and combine results
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))  # Using Python's built-in sort
    
    # Step 4: Copy sorted elements back to original array
    arr[:] = sorted_array
    return arr
