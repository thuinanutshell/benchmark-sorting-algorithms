# %%
def bubble_sort(arr, reverse=False):
    """Function for bubble sort algorithm. The algorithm works by
    comparing the adjacent elements and swap their positions. The time
    complexity of this algorithm in the worst case is quadratic: O(n^2)

    Args:
        arr (list): An unsorted list of non-negative integers
        reverse (bool, optional): False means sorting the list in an increasing order.
        True means sorting the list in a decreasing order.

    Returns:
        arr (list): A sorted array
    """
    if reverse == False:
        for i in range(len(arr)):
            for j in range(len(arr)-1):
                if arr[j] > arr[j+1]:
                    arr[j+1], arr[j] = arr[j], arr[j+1]
    else:
       for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[j] < arr[j+1]:
                    arr[j+1], arr[j] = arr[j], arr[j+1] 
    return arr