# Heap Sort

## Description
**Heap Sort** is a comparison-based sorting algorithm that uses a **binary heap** data structure.  
It first builds a **max-heap** (where the parent is always greater than or equal to its children).  
Then, it repeatedly swaps the root (largest element) with the last element in the heap and reduces the heap size by one, maintaining the heap property at each step.

---

## How it Works
1. **Build a max-heap** from the input array.  
2. **Swap the root** (maximum value) with the last element.  
3. **Reduce heap size** by 1.  
4. **Heapify** the root again to maintain the heap property.  
5. Repeat until the heap size is 1.  

---

## Example
Unsorted array:  
`[4, 10, 3, 5, 1]`

Steps:
- Build max-heap: `[10, 5, 3, 4, 1]`  
- Swap root with last: `[1, 5, 3, 4, 10]` → heapify → `[5, 4, 3, 1, 10]`  
- Swap root with last (size=4): `[1, 4, 3, 5, 10]` → heapify → `[4, 1, 3, 5, 10]`  
- Swap root with last (size=3): `[3, 1, 4, 5, 10]` → heapify → `[3, 1, 4, 5, 10]`  
- Swap root with last (size=2): `[1, 3, 4, 5, 10]` 

---

## Time Complexity
- **Best Case**: O(n log n)  
- **Average Case**: O(n log n)  
- **Worst Case**: O(n log n)  

## Space Complexity
- **O(1)** → Heap Sort is an **in-place sorting algorithm**.  

---

## When to Use
- Efficient for large datasets.  
- Useful when you need **O(1) extra space**.  
- Slower than Quick Sort in practice, but guarantees O(n log n) performance in the worst case.

---