# Sorting Algorithms in Python

## Introduction

### Why are sorting algorithms important?
Sorting algorithms are fundamental in computer science because they organize data into a specific order, usually ascending or descending. Efficient sorting:  
- Speeds up searching operations (e.g., Binary Search).  
- Facilitates data analysis and processing.  
- Is a critical component in databases, search engines, and large-scale systems.  

### Trade-offs of sorting algorithms
Different sorting algorithms have unique trade-offs in terms of:  
- **Time complexity** (speed of execution).  
- **Space complexity** (extra memory required).  
- **Stability** (whether equal elements preserve their relative order).  
- **Adaptability** (efficiency with nearly sorted or special datasets).  

Choosing the right algorithm depends on the problem requirements, dataset size, and constraints.  

### Common sorting algorithms
Some widely used sorting algorithms include:  
- **Comparison-based**: Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort, Heap Sort, TimSort.  
- **Non-comparison-based**: Counting Sort, Bucket Sort, Radix Sort.  

---

## Index of Algorithms

Each folder contains:  
- Python implementation of the algorithm.  
- Documentation explaining how it works, complexity, and when to use it.  

- [Bubble Sort](./algorithms/bubble_sort)  
- [Bucket Sort](./algorithms/bucket_sort)  
- [Counting Sort](./algorithms/counting_sort)  
- [Heap Sort](./algorithms/heap_sort)  
- [Insertion Sort](./algorithms/insertion_sort)  
- [Merge Sort](./algorithms/merge_sort)  
- [Quick Sort](./algorithms/quick_sort)  
- [Radix Sort](./algorithms/radix_sort)  
- [Selection Sort](./algorithms/selection_sort)  
- [TimSort](./algorithms/tim_sort)  

---

## Comparative Table of Sorting Algorithms

| Algorithm       | Best Case     | Average Case   | Worst Case    | Space Complexity | Stable |
|-----------------|--------------|---------------|---------------|------------------|--------|
| **Bubble Sort** | O(n)         | O(n²)         | O(n²)         | O(1)             | ✅     |
| **Selection Sort** | O(n²)     | O(n²)         | O(n²)         | O(1)             | ❌     |
| **Insertion Sort** | O(n)      | O(n²)         | O(n²)         | O(1)             | ✅     |
| **Merge Sort**  | O(n log n)   | O(n log n)    | O(n log n)    | O(n)             | ✅     |
| **Quick Sort**  | O(n log n)   | O(n log n)    | O(n²)         | O(log n)         | ❌     |
| **Heap Sort**   | O(n log n)   | O(n log n)    | O(n log n)    | O(1)             | ❌     |
| **Counting Sort** | O(n + k)   | O(n + k)      | O(n + k)      | O(n + k)         | ✅     |
| **Bucket Sort** | O(n + k)     | O(n + k)      | O(n²)         | O(n + k)         | ✅     |
| **Radix Sort**  | O(n·k)       | O(n·k)        | O(n·k)        | O(n + k)         | ✅     |
| **TimSort**     | O(n)         | O(n log n)    | O(n log n)    | O(n)             | ✅     |

**Legend**:  
- `n` = number of elements  
- `k` = range of input values or number of digits (for non-comparison sorts)  

## Charts of Sorting Performance

All performance charts generated from the experiments are stored in the [charts](./charts) folder.  

These charts show:  
- **Bar plots**: Comparison of execution times for each algorithm on a given array size.  
- **Line plots**: Execution time trends across algorithms for each array size.  

They help visualize how each algorithm scales and performs under different input sizes.  

**Note:** If you want to create new graphics, you just need to uncomment line 80 in the app.py file.

---

## How to Run
```bash
# Run main app
python app.py
