# Bucket Sort

## Description
**Bucket Sort** is a sorting algorithm that distributes the elements of an array into multiple buckets. Each bucket is then sorted individually (often using another sorting algorithm such as Insertion Sort or Python’s built-in `sorted()`), and finally, the contents of all buckets are concatenated to form the sorted array.

It is particularly effective when input values are **uniformly distributed** over a known range.

---

## How it Works
1. **Create buckets**: Decide how many buckets to use based on the input size and maximum value.
2. **Distribute elements**: Place each element into its corresponding bucket using a mapping function.
3. **Sort buckets**: Sort the elements inside each bucket individually.
4. **Concatenate results**: Merge all sorted buckets into the final sorted array.

---

## Example
Unsorted array:  
`[0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]`

Steps:
- Create 7 buckets (same as length of array).  
- Distribute elements:  
  - Bucket 0: `[0.23, 0.25]`  
  - Bucket 1: `[0.32]`  
  - Bucket 2: `[0.42, 0.47]`  
  - Bucket 3: `[0.51, 0.52]`  
- Sort each bucket individually.  
- Concatenate buckets → `[0.23, 0.25, 0.32, 0.42, 0.47, 0.51, 0.52]`


---

## Time Complexity
- **Best Case**: O(n + k) → when elements are evenly distributed across `k` buckets and sorting inside buckets is efficient.  
- **Average Case**: O(n + k) → similar reasoning as best case.  
- **Worst Case**: O(n²) → if all elements land in a single bucket.  

## Space Complexity
- **O(n + k)** → requires additional space for the buckets.

---

## When to Use
- Effective for **floating-point numbers** in the range `[0, 1)` or when data is **uniformly distributed**.  
- Not efficient for small datasets or data with high variance in distribution.