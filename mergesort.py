# %%
def mergesort(arr, start, end):
    # Base case
    if start >= end:
        return arr
    else:
        mid = (start + end) // 2
        
        # Recursively call itself to sort the subarray
        mergesort(arr, start, mid)
        mergesort(arr, mid+1, end)
        
        # Merge the sorted subarrays to get the final sorted array
        merge(arr, start, mid, end)
    

def merge(arr, start, mid, end):
    """Helper function to merge two subarrays. The algorithm works by
    comparing the first element of the left subarray with the items in
    the right subarray.  

    Args:
        left (list): Left subarray
        right (list): Right subarray
    """
    n1 = mid - start + 1
    n2 = end - mid
    left = [0] * (n1)
    right = [0] * (n2)
    
    for i in range(n1):
        left[i] = arr[start+i]
    for j in range(n2):
        right[j] = arr[mid+j+1]
    
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
            
            
# %%
arr = [6, 5, 4, 3, 2, 1]
start = 0
end = len(arr) - 1
mergesort(arr, start, end)
print(arr)