# Insertion Sort

## Description
**Insertion Sort** is a simple sorting algorithm that builds the final sorted array one element at a time.  
It is efficient for small datasets and is often used as part of hybrid sorting algorithms (e.g., **Timsort** and **Introsort**) when the data size is small.

---

## How it Works
1. Start with the second element of the array (since the first element is trivially sorted).  
2. Compare the current element (`key`) with the elements before it.  
3. Shift all larger elements one position to the right.  
4. Insert the `key` into its correct position.  
5. Repeat for all elements until the array is sorted.  

---

## Example
Unsorted array:  
`[12, 11, 13, 5, 6]`

Steps:
- Take `11`: insert before `12` → `[11, 12, 13, 5, 6]`  
- Take `13`: already in place → `[11, 12, 13, 5, 6]`  
- Take `5`: move before `11` → `[5, 11, 12, 13, 6]`  
- Take `6`: insert between `5` and `11` → `[5, 6, 11, 12, 13]`

---

## Time Complexity
- **Best Case**: O(n) → when the array is already sorted.  
- **Average Case**: O(n²)  
- **Worst Case**: O(n²) → when the array is sorted in reverse order.  

## Space Complexity
- **O(1)** → Insertion Sort is an in-place sorting algorithm.  

---

## When to Use
- Suitable for **small arrays** or arrays that are **already nearly sorted**.  
- Often used as a subroutine in more advanced sorting algorithms like **Timsort** and **Quick Sort (for small partitions)**.
