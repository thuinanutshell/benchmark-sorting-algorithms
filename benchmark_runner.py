import sys

sys.setrecursionlimit(5000)

from algorithms import ALL_ALGORITHMS
from benchmark.time_benchmark import benchmark_algorithms, print_results_table
from benchmark.data_generator import generate_test_sizes
from benchmark.plot_generator import plot_benchmark_results


def main():
    """Main function to run the sorting algorithm benchmarks."""

    print("🔍 Sorting Algorithm Benchmark - Worst Case Analysis")
    print("=" * 55)
    print("Testing with reverse-sorted arrays (worst case scenario)")
    print()

    # Configure test parameters
    print("Configuration:")

    sizes = generate_test_sizes(start=100, end=4000, step=100)

    # Run benchmarks
    results = benchmark_algorithms(ALL_ALGORITHMS, sizes=sizes, iterations=5)

    # Print results table
    print("\n" + "=" * 60)
    print("BENCHMARK RESULTS")
    print("=" * 60)
    print_results_table(results)

    plot_benchmark_results(
        results,
        title="Sorting Algorithms: Worst-Case Performance Comparison\n(Reverse-sorted input arrays)",
        save_path="sorting_benchmark_results.png",
    )


if __name__ == "__main__":
    main()
