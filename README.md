# Benchmarking Sorting Algorithms in Python

## Table of Contents
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

## Experiment Results
Check out my early draft for time complexity empirical experiments in this [Google Colab Notebook](https://colab.research.google.com/drive/1aOCxGSlI88Zf_GA2lTMU5oEfXIPLuu1J?authuser=1).

### Run Time
- Iteration for each size: 5
- Max size: 4000
<img width="1492" height="796" alt="Screenshot 2025-07-23 at 2 58 17 PM" src="https://github.com/user-attachments/assets/c0c068b2-c82f-4de4-9788-3912e80d2006" />

### Space Usage
| Algorithm       | 100   | 300   | 500   | 700   | 900   | 1100  | 1300  | 1500  | 1700  | 1900  | 2100  | 2300  | 2500  | 2700  | 2900  | 3100  | 3300  | 3500  | 3700  | 3900  |
| --------------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| bubble\_sort    | 0.001 | 0.003 | 0.004 | 0.006 | 0.007 | 0.009 | 0.010 | 0.012 | 0.013 | 0.015 | 0.016 | 0.018 | 0.019 | 0.021 | 0.022 | 0.024 | 0.025 | 0.027 | 0.028 | 0.030 |
| insertion\_sort | 0.001 | 0.002 | 0.004 | 0.006 | 0.007 | 0.009 | 0.010 | 0.012 | 0.013 | 0.015 | 0.016 | 0.018 | 0.019 | 0.021 | 0.022 | 0.024 | 0.025 | 0.027 | 0.028 | 0.030 |
| selection\_sort | 0.002 | 0.005 | 0.008 | 0.011 | 0.014 | 0.017 | 0.020 | 0.023 | 0.026 | 0.029 | 0.032 | 0.035 | 0.038 | 0.041 | 0.045 | 0.048 | 0.051 | 0.054 | 0.057 | 0.060 |
| merge\_sort     | 0.002 | 0.007 | 0.012 | 0.016 | 0.021 | 0.025 | 0.030 | 0.035 | 0.039 | 0.044 | 0.048 | 0.053 | 0.058 | 0.062 | 0.067 | 0.071 | 0.076 | 0.080 | 0.085 | 0.090 |
| quick\_sort     | 0.002 | 0.007 | 0.023 | 0.038 | 0.053 | 0.068 | 0.084 | 0.099 | 0.114 | 0.129 | 0.145 | 0.160 | 0.175 | 0.190 | 0.206 | 0.221 | 0.236 | 0.251 | 0.267 | 0.282 |
| heap\_sort      | 0.002 | 0.005 | 0.008 | 0.011 | 0.014 | 0.017 | 0.020 | 0.023 | 0.026 | 0.029 | 0.032 | 0.036 | 0.039 | 0.042 | 0.045 | 0.048 | 0.051 | 0.054 | 0.057 | 0.060 |

In all cases, **insertion sort** is the most memory-efficient algorithm

| Size | Most Efficient  | Memory (MB) |
| ---- | --------------- | ----------- |
| 100  | insertion\_sort | 0.0009      |
| 300  | insertion\_sort | 0.0025      |
| 500  | insertion\_sort | 0.0040      |
| 700  | insertion\_sort | 0.0055      |
| 900  | insertion\_sort | 0.0070      |
| 1100 | insertion\_sort | 0.0086      |
| 1300 | insertion\_sort | 0.0101      |
| 1500 | insertion\_sort | 0.0116      |
| 1700 | insertion\_sort | 0.0131      |
| 1900 | insertion\_sort | 0.0147      |
| 2100 | insertion\_sort | 0.0162      |
| 2300 | insertion\_sort | 0.0177      |
| 2500 | insertion\_sort | 0.0192      |
| 2700 | insertion\_sort | 0.0208      |
| 2900 | insertion\_sort | 0.0223      |
| 3100 | insertion\_sort | 0.0238      |
| 3300 | insertion\_sort | 0.0253      |
| 3500 | insertion\_sort | 0.0269      |
| 3700 | insertion\_sort | 0.0284      |
| 3900 | insertion\_sort | 0.0299      |


## Fundamental Sorting Algorithms
### Bubble Sort
### Insertion Sort
### Selection Sort
### Mergesort
### Quicksort
### Heapsort

## Other Sorting Algorithms
### Radix Sort
### Counting Sort
### Bucket Sort
### Topological Sort
