import matplotlib.pyplot as plt
import numpy as np

def plot_benchmark_results(
    results,
    title="Sorting Algorithm Performance Comparison",
    save_path=None,
    show_plot=True,
):
    """
    Generate a line plot comparing algorithm performance.

    Args:
        results (dict): Results from benchmark_algorithms
        title (str): Plot title
        save_path (str): Path to save the plot (optional)
        show_plot (bool): Whether to display the plot
    """
    if not results:
        print("No results to plot")
        return

    plt.figure(figsize=(12, 8))

    # Colors for different algorithms
    colors = [
        "#1f77b4",
        "#ff7f0e",
        "#2ca02c",
        "#d62728",
        "#9467bd",
        "#8c564b",
        "#e377c2",
        "#7f7f7f",
        "#bcbd22",
        "#17becf",
    ]

    for i, (algorithm, data) in enumerate(results.items()):
        sizes = sorted(data.keys())
        times = [data[size] for size in sizes if data[size] is not None]
        valid_sizes = [size for size in sizes if data[size] is not None]

        if not times:
            continue

        plt.plot(
            valid_sizes,
            times,
            marker="o",
            linewidth=2,
            markersize=6,
            color=colors[i % len(colors)],
            label=algorithm.replace("_", " ").title(),
        )

    plt.xlabel("Input Size (n)", fontsize=12)
    plt.ylabel("Execution Time (seconds)", fontsize=12)
    plt.title(title, fontsize=14, fontweight="bold")
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
        print(f"Plot saved to: {save_path}")

    if show_plot:
        plt.show()
