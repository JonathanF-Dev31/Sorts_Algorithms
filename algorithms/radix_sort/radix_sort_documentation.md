# Radix Sort

## Description
**Radix Sort** is a non-comparison-based sorting algorithm that sorts integers by processing their digits one by one.  
It uses a stable subroutine (usually **Counting Sort**) to sort numbers based on each digit, starting from the **least significant digit (LSD)** to the **most significant digit (MSD)**.

Unlike comparison-based algorithms like Quick Sort or Merge Sort, Radix Sort's performance does not depend on comparisons between elements.

---

## How it Works
1. Find the number with the maximum digits in the list.  
2. Starting from the **least significant digit** (units place), sort the list using **Counting Sort**.  
3. Move to the next digit (tens, hundreds, …) and repeat.  
4. After processing all digits, the list will be fully sorted.  

---

## Example
Unsorted array:  
`[170, 45, 75, 90, 802, 24, 2, 66]`

- **Step 1 (units digit)** → `[170, 90, 802, 2, 24, 45, 75, 66]`  
- **Step 2 (tens digit)** → `[802, 2, 24, 45, 66, 170, 75, 90]`  
- **Step 3 (hundreds digit)** → `[2, 24, 45, 66, 75, 90, 170, 802]`

---

## Time Complexity
- **Best Case**: O(n · k)  
- **Average Case**: O(n · k)  
- **Worst Case**: O(n · k)  
Where:  
- `n` = number of elements  
- `k` = number of digits in the largest number  

## Space Complexity
- **O(n + k)** → Due to auxiliary buckets in Counting Sort.  

---

## When to Use
- Works best for **integers** or **strings with fixed length**.  
- Very efficient when `k` (number of digits) is much smaller than `n`.  
- Not ideal for floating-point numbers or when comparisons are cheaper than digit manipulations.
