# Benchmarking Sorting Algorithms in Python

# Table of Contents
- [Bubble Sort](#bubble-sort)
- [Insertion Sort](#insertion-sort)
- [Selection Sort](#selection-sort)
- [Mergesort](#mergesort)
- [Quicksort](#quicksort)
- [Heapsort](#heapsort)
- [Radix Sort](#radix-sort)
- [Counting Sort](#counting-sort)
- [Bucket Sort](#bucket-sort)
- [Topological Sort](#topological-sort)

# Run Time
- Iteration for each size: 5
- Max size: 4000
<img width="1492" height="796" alt="Screenshot 2025-07-23 at 2 58 17 PM" src="https://github.com/user-attachments/assets/c0c068b2-c82f-4de4-9788-3912e80d2006" />

# Space Usage
| Algorithm       | 100   | 300   | 500   | 700   | 900   | 1100  | 1300  | 1500  | 1700  | 1900  | 2100  | 2300  | 2500  | 2700  | 2900  | 3100  | 3300  | 3500  | 3700  | 3900  |
| --------------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| bubble\_sort    | 0.001 | 0.003 | 0.004 | 0.006 | 0.007 | 0.009 | 0.010 | 0.012 | 0.013 | 0.015 | 0.016 | 0.018 | 0.019 | 0.021 | 0.022 | 0.024 | 0.025 | 0.027 | 0.028 | 0.030 |
| insertion\_sort | 0.001 | 0.002 | 0.004 | 0.006 | 0.007 | 0.009 | 0.010 | 0.012 | 0.013 | 0.015 | 0.016 | 0.018 | 0.019 | 0.021 | 0.022 | 0.024 | 0.025 | 0.027 | 0.028 | 0.030 |
| selection\_sort | 0.002 | 0.005 | 0.008 | 0.011 | 0.014 | 0.017 | 0.020 | 0.023 | 0.026 | 0.029 | 0.032 | 0.035 | 0.038 | 0.041 | 0.045 | 0.048 | 0.051 | 0.054 | 0.057 | 0.060 |
| merge\_sort     | 0.002 | 0.007 | 0.012 | 0.016 | 0.021 | 0.025 | 0.030 | 0.035 | 0.039 | 0.044 | 0.048 | 0.053 | 0.058 | 0.062 | 0.067 | 0.071 | 0.076 | 0.080 | 0.085 | 0.090 |
| quick\_sort     | 0.002 | 0.007 | 0.023 | 0.038 | 0.053 | 0.068 | 0.084 | 0.099 | 0.114 | 0.129 | 0.145 | 0.160 | 0.175 | 0.190 | 0.206 | 0.221 | 0.236 | 0.251 | 0.267 | 0.282 |
| heap\_sort      | 0.002 | 0.005 | 0.008 | 0.011 | 0.014 | 0.017 | 0.020 | 0.023 | 0.026 | 0.029 | 0.032 | 0.036 | 0.039 | 0.042 | 0.045 | 0.048 | 0.051 | 0.054 | 0.057 | 0.060 |

In all cases, **insertion sort** is the most memory-efficient algorithm


# Fundamental Sorting Algorithms
## Bubble Sort
### Definition
Bubble sort is a naive and very straightforward sorting algorithm. It works by simply traversing the items in the array one by one and comparing each item with the one on the right. In other words, we compare two adjacent values in the array; if the latter is greater than the former, we swap their positions. If not, we move on to the next item. Below is the step-by-step pseudocode to sort a list in increasing order:

1. Create a loop to go through each item in the array, starting at the first index
2. Create another inner loop to go through each item in the array, starting at the first index
3. Compare the current item with the item right next to it
4. If the next item > the current item, swap their positions. If not, no swap is needed
5. Continue until the inner loop reaches the end of the array. Move on to the next item of the outer loop
6. Finally, return the non-decreasing sorted array.

<img width="3122" height="1281" alt="image" src="https://github.com/user-attachments/assets/ccef2488-5d77-45b1-a48e-8813855924f7" />

<img width="1633" height="2449" alt="image" src="https://github.com/user-attachments/assets/acb34062-97dd-462f-93f6-d9b2d8546c7b" />

### Time & Space Complexity
Due to the nested loop that requires the algorithm to make (n-1) comparisons for each item. That means we have to run n iterations where each iteration consists of (n-1) comparisons, which is equivalent to a quadratic growth rate, no matter whether the list is already sorted, half-sorted, or reversely sorted! That is why bubble sort is very inefficient and rarely used in practice. 

- **Best-case scenario**: $O(n^2)$
- **Worst-case scenario**: $O(n^2)$

### Insertion Sort
Insertion sort is an algorithm used to sort an array by inserting an item one at a time into a sorted subarray. In other words, given a key that is to the right of a sorted subarray, we slide the key according to the comparison between it and other items in the subarray and insert it into the right position.

### Selection Sort
### Mergesort
### Quicksort
### Heapsort

## Other Sorting Algorithms
### Radix Sort
### Counting Sort
### Bucket Sort
### Timsort
### Topological Sort







