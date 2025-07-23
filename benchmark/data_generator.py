def generate_reverse_sorted_array(size):
    """
    Generate a reverse-sorted array for worst-case scenario testing.

    Args:
        size (int): Size of the array to generate

    Returns:
        list: Reverse-sorted array from size-1 down to 0
    """
    return list(range(size - 1, -1, -1))


def generate_test_sizes(start=100, end=1000, step=100):
    """
    Generate a range of input sizes for benchmarking.

    Args:
        start (int): Starting size
        end (int): Ending size
        step (int): Step size

    Returns:
        list: List of sizes to test
    """
    return list(range(start, end + 1, step))
