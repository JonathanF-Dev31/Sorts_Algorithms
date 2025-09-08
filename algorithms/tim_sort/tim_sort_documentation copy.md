# TimSort

## Description
**TimSort** is a hybrid sorting algorithm derived from **Merge Sort** and **Insertion Sort**.  
It was designed to perform well on many kinds of real-world data.  

Python's built-in `list.sort()` and Java's `Arrays.sort()` both use TimSort as their default sorting algorithm.  

It combines:
- **Insertion Sort** → Efficient on small datasets and nearly sorted arrays.  
- **Merge Sort** → Efficient for merging large sorted sequences.  

---

## How it Works
1. **Divide into runs**:  
   The array is divided into small chunks (called *runs*) of size `MIN_RUN` (commonly 32).  

2. **Sort runs with Insertion Sort**:  
   Each run is sorted individually using Insertion Sort, which is efficient for small arrays.  

3. **Merge runs**:  
   Runs are merged together in a manner similar to Merge Sort until the entire array is sorted.  

---

## Example
Unsorted array:  
`[5, 21, 7, 23, 19, 10, 1, 3, 12, 15]`

- Step 1: Divide into runs of size 32 (or smaller if array is short).  
- Step 2: Sort each run with Insertion Sort.  
- Step 3: Merge runs together until one sorted array remains.  

---

## Time Complexity
- **Best Case**: O(n) → When the array is already sorted.  
- **Average Case**: O(n log n)  
- **Worst Case**: O(n log n)  

## Space Complexity
- **O(n)** → Due to temporary arrays used during merging.  

---

## When to Use
- When using **Python (`list.sort()`) or Java (`Arrays.sort()`)**, as they already implement TimSort.  
- When the dataset is **partially sorted**, since TimSort adapts and runs in nearly linear time.  
- When **stability** is required (important for records with multiple keys).  
- For **general-purpose sorting** in real-world applications, since it handles varied datasets efficiently.  
