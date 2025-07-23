from typing import List


def sort(arr: List, reverse=False) -> List:
    """Bubble Sort Algorithm.

    The algorithm works by comparing the adjacent elements and swap their positions.
    The time complexity of this algorithm in the
        - Best case is quadratic: O(n^2)
        - Worst case is quadratic: O(n^2)

    Args:
        arr (list): An unsorted list of non-negative integers
        reverse (bool, optional):
            - false: sort the list in an increasing order.
            - true: sort the list in a decreasing order.

    Returns:
        arr (list): A sorted array
    """
    if reverse == False:
        for i in range(len(arr)):
            for j in range(len(arr) - 1):
                if arr[j] > arr[j + 1]:
                    arr[j + 1], arr[j] = arr[j], arr[j + 1]
    else:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[j] < arr[j + 1]:
                    arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr
