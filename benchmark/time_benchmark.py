import time
import copy
from .data_generator import generate_reverse_sorted_array, generate_test_sizes


def time_algorithm(algorithm_func, data, iterations=3):
    """
    Time a single algorithm on given data.

    Args:
        algorithm_func: The sorting algorithm function
        data: Input data to sort
        iterations: Number of iterations for averaging

    Returns:
        float: Average execution time in seconds
    """
    times = []

    for _ in range(iterations):
        # Create a fresh copy for each iteration
        test_data = copy.deepcopy(data)

        start_time = time.perf_counter()
        algorithm_func(test_data)
        end_time = time.perf_counter()

        times.append(end_time - start_time)

    return sum(times) / len(times)


def benchmark_algorithms(algorithms, sizes=None, iterations=3):
    """
    Benchmark multiple algorithms across different input sizes.

    Args:
        algorithms (dict): Dictionary of {name: function} for algorithms
        sizes (list): List of input sizes to test
        iterations (int): Number of iterations per test

    Returns:
        dict: Results in format {algorithm_name: {size: time}}
    """
    if sizes is None:
        sizes = generate_test_sizes(100, 1000, 100)

    if isinstance(algorithms, list):
        algorithms = dict(algorithms)

    results = {name: {} for name in algorithms.keys()}

    print("Starting benchmark...")
    total_tests = len(algorithms) * len(sizes)
    current_test = 0

    for size in sizes:
        print(f"\nTesting size: {size}")
        data = generate_reverse_sorted_array(size)

        for name, algorithm_func in algorithms.items():
            current_test += 1
            print(f"  [{current_test}/{total_tests}] {name}...", end=" ")

            try:
                avg_time = time_algorithm(algorithm_func, data, iterations)
                results[name][size] = avg_time
                print(f"{avg_time:.6f}s")
            except Exception as e:
                print(f"ERROR: {e}")
                results[name][size] = None

    return results


def print_results_table(results):
    """
    Print benchmark results in a formatted table.

    Args:
        results (dict): Results from benchmark_algorithms
    """
    if not results:
        return

    sizes = sorted(list(results[list(results.keys())[0]].keys()))
    algorithms = list(results.keys())

    # Print header
    print(f"\n{'Size':<10}", end="")
    for alg in algorithms:
        print(f"{alg:<12}", end="")
    print()

    print("-" * (10 + 12 * len(algorithms)))

    # Print data rows
    for size in sizes:
        print(f"{size:<10}", end="")
        for alg in algorithms:
            time_val = results[alg][size]
            if time_val is not None:
                print(f"{time_val:.6f}s  ", end="")
            else:
                print("ERROR     ", end="")
        print()
