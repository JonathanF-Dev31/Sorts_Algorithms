import time

def measure_sort(sort_name, sort_func, arr, *args):
    arr_copy = arr[:]

    start_time = time.perf_counter()
    sort_func(arr_copy, *args)  
    end_time = time.perf_counter()

    elapsed_time = (end_time - start_time) * 1000  # ms

    """print(f"{sort_name} took {elapsed_time:.4f} ms for array size {len(arr_copy)} \n")
    print(arr_copy[0:10], "...\n")"""

    return (sort_name, len(arr_copy), elapsed_time)
