# Counting Sort

## Description
**Counting Sort** is a non-comparison-based sorting algorithm.  
It works by counting the number of occurrences of each distinct element in the input array, storing these counts in an auxiliary array, and then using this information to place the elements in the correct position in the output array.

It is very efficient for sorting integers or objects that can be mapped to small integer keys.

---

## How it Works
1. Find the **minimum** and **maximum** value in the array.  
2. Create a **counting array** to store the frequency of each element.  
3. Iterate over the input array and increment the count for each element.  
4. Reconstruct the sorted array by iterating over the counting array and placing elements based on their frequency.  

---

## Example
Unsorted array:  
`[4, 2, 2, 8, 3, 3, 1]`

Steps:
- Find min = 1, max = 8  
- Create `count_array` of size `(max - min + 1) = 8` → `[0,0,0,0,0,0,0,0]`  
- Count occurrences: `[1,2,2,1,0,0,1,0]`  
- Reconstruct sorted array: `[1,2,2,3,3,4,8]`


---

## Time Complexity
- **Best Case**: O(n + k)  
- **Average Case**: O(n + k)  
- **Worst Case**: O(n + k)  

Where:  
- `n` = number of elements  
- `k` = range of input values (`max - min + 1`)

## Space Complexity
- **O(n + k)** → requires additional space for the counting array and output array.  

---

## When to Use
- Best for sorting **integers with a small range** compared to the number of elements.  
- Not suitable for datasets with a very large range (e.g., numbers between 1 and 1 billion) due to memory usage.  
- Often used as a subroutine in other algorithms like **Radix Sort**.
