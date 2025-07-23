from typing import List


def sort(arr: List, reverse=False) -> List:
    """Selection Sort Algorithm

    The algorithm sorts a list by comparing one item with the remaining items in the list
    and swap that item with the smallest one. Continue with the second item until the last one.

    The time complexity of selection sort in the:
      - Worst case is: O(n^2)
      - Best case is: O(n^2)

    Args:
        Args:
          arr (list): An unsorted list of non-negative integers
          reverse (bool, optional):
              - false: sort the list in an increasing order.
              - true: sort the list in a decreasing order.

    Returns:
        arr (list): A sorted array
    """
    if not arr:
        return []

    # Make a copy to avoid modifying the original
    result = arr.copy()

    for i in range(len(result)):
        min_idx = i
        for j in range(i + 1, len(result)):
            if not reverse:
                if result[j] < result[min_idx]:
                    min_idx = j
            else:
                if result[j] > result[min_idx]:
                    min_idx = j

        result[i], result[min_idx] = result[min_idx], result[i]

    return result
