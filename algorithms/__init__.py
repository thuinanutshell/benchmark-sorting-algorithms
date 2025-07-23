from . import (
    bubblesort,
    insertion_sort,
    selection_sort,
    mergesort,
    quicksort,
    heapsort,
)

ALL_ALGORITHMS = [
    ("bubble_sort", bubblesort.sort),
    ("insertion_sort", insertion_sort.sort),
    ("selection_sort", selection_sort.sort),
    ("merge_sort", mergesort.sort),
    ("quick_sort", quicksort.sort),
    ("heap_sort", heapsort.sort),
]
