from typing import List


def sort(arr: List, reverse=False) -> List:
    """Insertion Sort Algorithm.

    The algorithm works by incrementally building the final sorted list one item at a time.
    It compares the items and insert an item to the right postion in the already sorted subarray.

    The time complexity of insertion sort in the
      - Worst case is quadratic: O(n^2)
      - Best case is linear: O(n)

    Args:
        arr (list): An unsorted list of non-negative integers
        reverse (bool, optional):
            - false: sort the list in an increasing order.
            - true: sort the list in a decreasing order.

    Returns:
        arr (list): A sorted array

    """
    n = len(arr)

    for i in range(1, n):
        # Assign the key variable with the current item
        key = arr[i]

        # This is the position right before i
        j = i - 1

        # Keep comparing the remaining elements with the key
        while j >= 0 and arr[j] > key:
            # Insert arr[j] to the right position of the already sorted subarray
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr
