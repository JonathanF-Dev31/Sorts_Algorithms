# Selection Sort

## Description
**Selection Sort** is a simple comparison-based sorting algorithm.  
It works by repeatedly selecting the **minimum element** from the unsorted part of the array and swapping it with the first unsorted element.  

The algorithm divides the array into two parts:
- **Sorted portion** (built from left to right).  
- **Unsorted portion** (shrinks as the algorithm progresses).  

---

## How it Works
1. Start at index `0`.  
2. Find the smallest element in the unsorted portion.  
3. Swap it with the element at the current index.  
4. Move to the next index and repeat until the array is sorted.  

---

## Example
Unsorted array:  
`[64, 25, 12, 22, 11]`

- Step 1 → Smallest = 11 → Swap with 64 → `[11, 25, 12, 22, 64]`  
- Step 2 → Smallest in `[25, 12, 22, 64]` = 12 → Swap with 25 → `[11, 12, 25, 22, 64]`  
- Step 3 → Smallest in `[25, 22, 64]` = 22 → Swap with 25 → `[11, 12, 22, 25, 64]`  
- Step 4 → Smallest in `[25, 64]` = 25 → Already in place → `[11, 12, 22, 25, 64]`

---

## Time Complexity
- **Best Case**: O(n²)  
- **Average Case**: O(n²)  
- **Worst Case**: O(n²)  

## Space Complexity
- **O(1)** → In-place sorting, only swaps are performed.  

---

## When to Use
- When the dataset is **small**.  
- When **memory usage** is extremely limited (since it uses O(1) extra space).  
- In educational contexts to **teach sorting concepts**.  
- When the cost of **swaps is cheaper** than the cost of comparisons.  
- Not recommended for large datasets because of its O(n²) time complexity.  
