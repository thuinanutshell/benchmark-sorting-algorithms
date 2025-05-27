# %%
def insertion_sort(arr, reverse=False):
  """Function for insertion sort algorithm. The algorithm works by
  incrementally building the final sorted list one item at a time. 
  It compares the items and insert an item to the right postion in the already 
  sorted subarray. The time complexity of this algorithm in the 
  worst case is quadratic: O(n^2)

  Args:
      arr (list): An unsorted list of non-negative integers
      reverse (bool, optional): False means sorting the list in an increasing order.
      True means sorting the list in a decreasing order.

  Returns:
      arr (list): A sorted array
  """
  step_count = 0
  n = len(arr)

  for i in range(1, n):
    # Assign the key variable with the item arr[i]
    key = arr[i]
    
    # This is the position right before i
    j = i - 1
    step_count += 1
    
    # Keep comparing the remaining elements with the key
    while j >= 0 and arr[j] > key:
      # Insert arr[j] to the right position of the already sorted subarray
      arr[j + 1] = arr[j]
      step_count += 1
      j -= 1
    
    arr[j + 1] = key
    step_count += 1

  return arr, step_count