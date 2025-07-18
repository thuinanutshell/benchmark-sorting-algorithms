# %%
def selection_sort(arr, reverse=False):
  """Function for selection sort. The algorithm works to sort a list by
  comparing one item with the remaining items in the list and swap that item
  with the smallest one. Continue with the second item until the last one.

  Args:
      arr (list): An unsorted list of non-negative integers
      reverse (bool, optional): False means sorting the list in an increasing order.
      True means sorting the list in a decreasing order.

  Returns:
      arr (list): A sorted array
  """
  step_count = 0
  for i in range(len(arr)):
    min_idx = i
    step_count += 1

    for j in range(i+1, len(arr)-1):
      step_count += 1
      
      if arr[i] > arr[j]:
        step_count += 1
        min_idx = j

    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    step_count += 1
  return arr, step_count