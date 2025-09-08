# Merge Sort

## Description
**Merge Sort** is a **divide-and-conquer** sorting algorithm.  
It divides the array into halves, recursively sorts each half, and then merges the two sorted halves into one sorted array.  

Merge Sort is stable and guarantees **O(n log n)** performance regardless of input order.

---

## How it Works
1. **Divide**: Split the array into two halves until each subarray has only one element.  
2. **Conquer**: Recursively sort each half.  
3. **Combine**: Merge the two sorted halves back together.  

---

## Example
Unsorted array:  
`[38, 27, 43, 3, 9, 82, 10]`

Steps:
- Divide into `[38, 27, 43, 3]` and `[9, 82, 10]`.  
- Further divide `[38, 27, 43, 3]` → `[38, 27]` and `[43, 3]`.  
- Keep dividing until single elements remain.  
- Merge step by step:  
  - `[27, 38]`, `[3, 43]` → `[3, 27, 38, 43]`  
  - `[9, 10, 82]`  
  - Final merge: `[3, 9, 10, 27, 38, 43, 82]`

---

## Time Complexity
- **Best Case**: O(n log n)  
- **Average Case**: O(n log n)  
- **Worst Case**: O(n log n)  

## Space Complexity
- **O(n)** → Requires auxiliary arrays during merging.  

---

## When to Use
- Suitable when **stability** is required (preserves order of equal elements).  
- Works well for **large datasets**.  
- Preferred when random access is slow (like linked lists) since merge can be efficient there.