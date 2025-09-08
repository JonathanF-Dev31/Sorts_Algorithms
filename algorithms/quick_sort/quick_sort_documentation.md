# Quick Sort

## Description
**Quick Sort** is a highly efficient, divide-and-conquer, comparison-based sorting algorithm.  
It works by selecting a **pivot element**, partitioning the array around the pivot (so that elements smaller are on the left and larger are on the right), and then recursively applying the same process to the subarrays.

Quick Sort is often faster than other O(n log n) algorithms like Merge Sort, especially for in-memory sorting.

---

## How it Works
1. Choose a **pivot** element (in this implementation, the first element).  
2. Rearrange elements:  
   - Values less than pivot go to the left.  
   - Values greater than pivot go to the right.  
3. Place the pivot in its correct position.  
4. Recursively apply Quick Sort to the left and right partitions.  

---

## Example
Unsorted array:  
`[29, 10, 14, 37, 13]`

Steps:
- Pivot = 29  
- Partition → `[10, 14, 13] [29] [37]`  
- Apply Quick Sort to `[10, 14, 13]`: Pivot = 10 → `[10] [13, 14]`  
- Final result → `[10, 13, 14, 29, 37]`

---

## Time Complexity
- **Best Case**: O(n log n) → when pivot divides array evenly.  
- **Average Case**: O(n log n)  
- **Worst Case**: O(n²) → when pivot is always the smallest or largest element (e.g., already sorted array).  

## Space Complexity
- **O(log n)** → due to recursive stack calls.  

---

## When to Use
- Great for **large datasets** in memory.  
- Performs better than Merge Sort in practice (less memory overhead).  
- Not ideal for **already sorted or nearly sorted data** unless using a randomized pivot strategy.
