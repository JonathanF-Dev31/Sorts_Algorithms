def heapify(arr, n, i):
    """
    Heapify Subtree
    ---------------
    Ensures the max-heap property for a subtree rooted at index `i`.

    Parameters:
        arr (list): The array representing the heap.
        n (int): Size of the heap (number of elements considered).
        i (int): Index of the current root node to heapify.

    Returns:
        None: The array is modified in place.
    """
    largest = i          # Assume the root is the largest
    l = 2 * i + 1        # Left child index
    r = 2 * i + 2        # Right child index

    # If the left child exists and is greater than the root
    if l < n and arr[i] < arr[l]:
        largest = l

    # If the right child exists and is greater than the current largest
    if r < n and arr[largest] < arr[r]:
        largest = r

    # If the largest is not the root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    """
    Heap Sort Algorithm
    -------------------
    Sorts an array in ascending order using the Heap Sort algorithm.
    It first builds a max-heap and then repeatedly extracts the largest element.

    Parameters:
        arr (list): A list of comparable elements.

    Returns:
        list: The sorted list in ascending order.
    """
    n = len(arr)

    # Step 1: Build a max-heap from the input array
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Swap the root (max element) with the last element
        arr[i], arr[0] = arr[0], arr[i]

        # Heapify the reduced heap
        heapify(arr, i, 0)