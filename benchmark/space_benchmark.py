import tracemalloc
import statistics
from .data_generator import generate_reverse_sorted_array

import sys

sys.setrecursionlimit(5000)


def measure_memory_usage(algorithm_func, data):
    """
    Measure peak memory usage of a sorting algorithm using tracemalloc.

    Args:
        algorithm_func: The sorting function to benchmark
        data: Input data to sort

    Returns:
        tuple: (peak_memory_mb, sorted_result)
    """
    # Start tracing memory allocations
    tracemalloc.start()

    try:
        # Run the sorting algorithm
        result = algorithm_func(data.copy())

        # Get current memory usage
        current, peak = tracemalloc.get_traced_memory()

        # Convert bytes to MB for readability
        peak_memory_mb = peak / 1024 / 1024

        return peak_memory_mb, result

    finally:
        # Always stop tracing
        tracemalloc.stop()


def benchmark_memory_usage(algorithms, sizes, iterations=3):
    """
    Benchmark memory usage for multiple sorting algorithms across different input sizes.

    Args:
        algorithms: List of (name, function) tuples
        sizes: List of input sizes to test
        iterations: Number of iterations per test for averaging

    Returns:
        dict: Nested dictionary with results[algorithm][size] = avg_memory_mb
    """
    results = {}

    print(f"Running memory benchmarks with {iterations} iterations per test...")
    print(f"Input sizes: {sizes}")
    print("-" * 60)

    for algo_name, algo_func in algorithms:
        print(f"Testing {algo_name}...")
        results[algo_name] = {}

        for size in sizes:
            memory_measurements = []

            for iteration in range(iterations):
                # Generate test data (worst case: reverse sorted)
                test_data = generate_reverse_sorted_array(size)

                try:
                    memory_usage, _ = measure_memory_usage(algo_func, test_data)
                    memory_measurements.append(memory_usage)

                except Exception as e:
                    print(f"  Error with {algo_name} at size {size}: {e}")
                    memory_measurements.append(float("inf"))
                    break

            # Calculate average memory usage
            if memory_measurements and all(
                m != float("inf") for m in memory_measurements
            ):
                avg_memory = statistics.mean(memory_measurements)
                results[algo_name][size] = avg_memory
                print(f"  Size {size:4d}: {avg_memory:.4f} MB")
            else:
                results[algo_name][size] = float("inf")
                print(f"  Size {size:4d}: FAILED")

        print()

    return results


def print_memory_results_table(results):
    """
    Print a formatted table of memory benchmark results.

    Args:
        results: Dictionary of benchmark results from benchmark_memory_usage
    """
    if not results:
        print("No results to display.")
        return

    # Get all sizes tested
    sizes = sorted(
        set(size for algo_results in results.values() for size in algo_results.keys())
    )

    # Print header
    print(f"{'Algorithm':<15} " + " ".join(f"{size:>8}" for size in sizes))
    print("-" * (15 + len(sizes) * 9))

    # Print results for each algorithm
    for algo_name in results:
        row = f"{algo_name:<15} "
        for size in sizes:
            memory = results[algo_name].get(size, float("inf"))
            if memory == float("inf"):
                row += f"{'FAIL':>8} "
            else:
                row += f"{memory:>8.3f} "
        print(row)

    print("\nMemory usage shown in MB (megabytes)")
    print("FAIL indicates the algorithm failed or exceeded limits")


def find_most_memory_efficient(results):
    """
    Analyze results to find the most memory-efficient algorithm for each size.

    Args:
        results: Dictionary of benchmark results

    Returns:
        dict: size -> (algorithm_name, memory_usage)
    """
    if not results:
        return {}

    sizes = sorted(
        set(size for algo_results in results.values() for size in algo_results.keys())
    )
    most_efficient = {}

    for size in sizes:
        best_algo = None
        best_memory = float("inf")

        for algo_name in results:
            memory = results[algo_name].get(size, float("inf"))
            if memory < best_memory:
                best_memory = memory
                best_algo = algo_name

        if best_algo:
            most_efficient[size] = (best_algo, best_memory)

    return most_efficient


def print_efficiency_analysis(results):
    """
    Print analysis of which algorithms are most memory efficient.

    Args:
        results: Dictionary of benchmark results
    """
    most_efficient = find_most_memory_efficient(results)

    if not most_efficient:
        print("No efficiency analysis available.")
        return

    print("\n" + "=" * 50)
    print("MEMORY EFFICIENCY ANALYSIS")
    print("=" * 50)

    print(f"{'Size':<8} {'Most Efficient':<15} {'Memory (MB)':<12}")
    print("-" * 35)

    for size in sorted(most_efficient.keys()):
        algo_name, memory = most_efficient[size]
        print(f"{size:<8} {algo_name:<15} {memory:<12.4f}")

    # Count wins per algorithm
    algo_wins = {}
    for _, (algo_name, _) in most_efficient.items():
        algo_wins[algo_name] = algo_wins.get(algo_name, 0) + 1

    print(f"\nOverall winners:")
    for algo, wins in sorted(algo_wins.items(), key=lambda x: x[1], reverse=True):
        print(f"  {algo}: {wins} size(s)")


if __name__ == "__main__":
    from algorithms import ALL_ALGORITHMS
    from .data_generator import generate_test_sizes

    print("Memory Usage Benchmark - Sorting Algorithms")
    print("=" * 50)

    test_sizes = generate_test_sizes(start=100, end=4000, step=200)

    # Run memory benchmarks
    memory_results = benchmark_memory_usage(ALL_ALGORITHMS, test_sizes, iterations=3)

    # Print results
    print_memory_results_table(memory_results)
    print_efficiency_analysis(memory_results)
