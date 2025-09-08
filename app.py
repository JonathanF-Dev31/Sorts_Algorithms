from multiprocessing import Pool
from data.arrays import Arrays
from algorithms.quick_sort.quick_sort import quick_sort
from algorithms.merge_sort.merge_sort import merge_sort
from algorithms.heap_sort.heap_sort import heap_sort
from algorithms.insertion_sort.insertion_sort import insertion_sort
from algorithms.counting_sort.counting_sort import counting_sort
from algorithms.bucket_sort.bucket_sort import bucket_sort
from algorithms.radix_sort.radix_sort import radix_sort
from algorithms.selection_sort.selection_sort import selection_sort
from algorithms.bubble_sort.bubble_sort import bubble_sort
from algorithms.tim_sort.tim_sort import tim_sort
from create_graphic import create_graphic
from measure_sort import measure_sort

if __name__ == "__main__":
    # Initialize predefined arrays (different sizes) from the Arrays class
    arrays = Arrays()

    # Define tasks for each sorting algorithm with corresponding array(s).
    # Each task is represented as a tuple:
    # (Algorithm Name, Sorting Function, Array, Optional Parameters)
    tasks = [
        # QuickSort tasks
        ("QuickSort", quick_sort, arrays.array_one, 0, len(arrays.array_one) - 1),
        ("QuickSort", quick_sort, arrays.array_two, 0, len(arrays.array_two) - 1),
        ("QuickSort", quick_sort, arrays.array_three, 0, len(arrays.array_three) - 1),

        # MergeSort tasks
        ("MergeSort", merge_sort, arrays.array_one, 0, len(arrays.array_one) - 1),
        ("MergeSort", merge_sort, arrays.array_two, 0, len(arrays.array_two) - 1),
        ("MergeSort", merge_sort, arrays.array_three, 0, len(arrays.array_three) - 1),

        # HeapSort tasks
        ("HeapSort", heap_sort, arrays.array_one),
        ("HeapSort", heap_sort, arrays.array_two),
        ("HeapSort", heap_sort, arrays.array_three),

        # InsertionSort tasks
        ("InsertionSort", insertion_sort, arrays.array_one, 0, len(arrays.array_one) - 1),
        ("InsertionSort", insertion_sort, arrays.array_two, 0, len(arrays.array_two) - 1),
        ("InsertionSort", insertion_sort, arrays.array_three, 0, len(arrays.array_three) - 1),

        # CountingSort tasks
        ("CountingSort", counting_sort, arrays.array_one),
        ("CountingSort", counting_sort, arrays.array_two),
        ("CountingSort", counting_sort, arrays.array_three),

        # BucketSort tasks
        ("BucketSort", bucket_sort, arrays.array_one),
        ("BucketSort", bucket_sort, arrays.array_two),
        ("BucketSort", bucket_sort, arrays.array_three),

        # RadixSort tasks
        ("RadixSort", radix_sort, arrays.array_one),
        ("RadixSort", radix_sort, arrays.array_two),
        ("RadixSort", radix_sort, arrays.array_three),

        # SelectionSort tasks
        ("SelectionSort", selection_sort, arrays.array_one),
        ("SelectionSort", selection_sort, arrays.array_two),
        ("SelectionSort", selection_sort, arrays.array_three),

        # BubbleSort tasks
        ("BubbleSort", bubble_sort, arrays.array_one),
        ("BubbleSort", bubble_sort, arrays.array_two),
        ("BubbleSort", bubble_sort, arrays.array_three),

        # TimSort tasks
        ("TimSort", tim_sort, arrays.array_one),
        ("TimSort", tim_sort, arrays.array_two),
        ("TimSort", tim_sort, arrays.array_three),
    ]

    # Execute all tasks in parallel using Python's multiprocessing Pool
    with Pool() as pool:
        results = pool.starmap(measure_sort, tasks)

    # Generate a graph with the execution results of all sorting algorithms
    # create_graphic(results)
