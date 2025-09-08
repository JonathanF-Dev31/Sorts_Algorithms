import matplotlib.pyplot as plt
import pandas as pd
import os

def create_graphic(results):
    """
    Generate performance charts (bar and line plots) for sorting algorithms,
    with execution time values annotated on each bar and line point.

    Args:
        results (list of tuples): Each tuple contains:
            - Algorithm name (str)
            - Array size (int)
            - Execution time in milliseconds (float)

    Output:
        Saves charts inside the "charts" folder:
            - Bar chart:   "<array_size>_bar.png"
            - Line chart:  "<array_size>_line.png"
    """

    # Ensure the "charts" directory exists
    os.makedirs("charts", exist_ok=True)

    # Convert results to a DataFrame
    df = pd.DataFrame(results, columns=["Algorithm", "Array Size", "Time (ms)"])

    # Iterate through each unique array size
    for arr_size in df["Array Size"].unique():
        subset = df[df["Array Size"] == arr_size]

        # --- BAR CHART ---
        plt.figure(figsize=(12, 6))
        bars = plt.bar(subset["Algorithm"], subset["Time (ms)"], color="skyblue", alpha=0.8)

        # Add labels on top of bars
        for bar, time in zip(bars, subset["Time (ms)"]):
            plt.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height(),
                f"{time:.4f}",
                ha="center",
                va="bottom",
                fontsize=9,
                rotation=0
            )

        plt.xticks(rotation=45)
        plt.ylabel("Execution Time (ms)")
        plt.title(f"Sorting Algorithms Performance (Bar) - size {arr_size}")
        plt.tight_layout()
        plt.savefig(f"charts/{arr_size}_bar.png")
        plt.close()

        # --- LINE CHART ---
        plt.figure(figsize=(12, 6))
        plt.plot(
            subset["Algorithm"],
            subset["Time (ms)"],
            marker="o",
            linestyle="-",
            color="steelblue"
        )

        # Add labels to each point
        for i, time in enumerate(subset["Time (ms)"]):
            plt.text(
                i,
                time,
                f"{time:.4f}",
                ha="center",
                va="bottom",
                fontsize=9,
                rotation=0
            )

        plt.xticks(rotation=45)
        plt.ylabel("Execution Time (ms)")
        plt.title(f"Sorting Algorithms Performance (Line) - size {arr_size}")
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.tight_layout()
        plt.savefig(f"charts/{arr_size}_line.png")
        plt.close()
