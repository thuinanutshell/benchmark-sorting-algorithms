from typing import List


def sort(arr: List) -> List:
    """Public interface for MergeSort
    Args:
        arr (list): The array to sort
    Returns:
        list: A new sorted array (doesn't modify original)
    """
    if not arr:  # Handle empty array
        return []

    # Make a copy to avoid modifying the original array
    result = arr.copy()

    # Sort the copy in-place
    mergesort(result, 0, len(result) - 1)

    return result


def mergesort(arr: List, start: int, end: int) -> None:
    """Mergesort Algorithm

    Args:
        arr (list): a list of non-negative integers
        start (int): starting index of the 0-indexed array
        end (int): last index of the array

    Returns:
        None: because this algorithm sorts in-place.
    """
    # Base case
    if start >= end:
        return arr
    else:
        mid = (start + end) // 2

        # Recursively call itself to sort the subarray
        mergesort(arr, start, mid)  # left subarray
        mergesort(arr, mid + 1, end)  # right subarray

        # Merge the sorted subarrays to get the final sorted array
        merge(arr, start, mid, end)


def merge(arr: List, start: int, mid: int, end: int) -> None:
    """Helper function to merge two subarrays.

    1. Compares the first element of the left subarray with the items in the right subarray.

    2. If the 1st item of left subarr is smaller than the 1st item of right subarr,
       then the starting item of the bigger array is the 1st item of left subarr

    3. If that's not the case, then the starting item of the bigger array is the first item of right subarr

    4. Continue until both reach the end of the subarrays

    5. Finally, just add the remaining of both subarrays to the big array

    Args:
        left (list): Left subarray
        right (list): Right subarray
    """
    n1 = mid - start + 1
    n2 = end - mid
    left = [0] * (n1)
    right = [0] * (n2)

    for i in range(n1):
        left[i] = arr[start + i]
    for j in range(n2):
        right[j] = arr[mid + j + 1]

    i, j = 0, 0
    k = start

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1
