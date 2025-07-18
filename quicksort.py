# %%
def partition(arr, start, end):
    """Partition function using last element as pivot.
    
    Args:
        arr (list): The array to partition
        start (int): Starting index of subarray
        end (int): Ending index of subarray (pivot location)
    
    Returns:
        int: Final position of pivot after partitioning
    """
    pivot_value = arr[end]  # Choose last element as pivot
    i = start - 1           # Index of smaller element
    
    # Traverse through start to end-1
    for j in range(start, end):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot_value:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place pivot in correct position
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


def quicksort(arr, start, end):
    """QuickSort algorithm implementation.
    
    Args:
        arr (list): The array to sort
        start (int): Starting index
        end (int): Ending index
    """
    if start < end:
        # Partition the array and get pivot index
        pivot_index = partition(arr, start, end)
        
        # Recursively sort elements before and after partition
        quicksort(arr, start, pivot_index - 1)
        quicksort(arr, pivot_index + 1, end)
# %%
arr = [6, 5, 4, 3, 2, 1]
quicksort(arr, 0, len(arr)-1)
print(arr)