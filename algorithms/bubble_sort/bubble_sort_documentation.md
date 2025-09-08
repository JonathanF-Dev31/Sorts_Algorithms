# Bubble Sort

## Description
**Bubble Sort** is one of the simplest sorting algorithms.  
It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until no swaps are needed, which means the list is sorted.

The name "Bubble Sort" comes from the way larger elements "bubble up" to the end of the list with each pass.

---

## How it Works
1. Start at the beginning of the list.
2. Compare the first two elements:
   - If the first is greater than the second, swap them.
3. Move to the next pair and repeat the comparison.
4. After each full pass, the largest element is placed at the end.
5. Repeat this process until no swaps are needed.

---

## Example
Array before sorting:  
`[5, 3, 8, 4, 2]`

Steps:
- Pass 1: `[3, 5, 4, 2, 8]`
- Pass 2: `[3, 4, 2, 5, 8]`
- Pass 3: `[3, 2, 4, 5, 8]`
- Pass 4: `[2, 3, 4, 5, 8]`

---

## Time Complexity
- **Best Case**: O(n) → when the array is already sorted.  
- **Average Case**: O(n²)  
- **Worst Case**: O(n²) → when the array is sorted in reverse order.  

## Space Complexity
- **O(1)** → Bubble Sort is an in-place sorting algorithm (no extra memory required).  

---

## When to Use
- Suitable for small datasets or when simplicity is more important than performance.
- Not efficient for large datasets.
