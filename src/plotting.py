import os
import pandas as pd
import matplotlib.pyplot as plt
import logging
from typing import List, Tuple

def plot_smoothed_loss(
    dfs: List[Tuple[pd.DataFrame, str]],
    title: str = "Training Loss",
    smoothing_factor: float = 0.9,
    save_path: str = "outputs",
    display: bool = False
):
    """
    Plots smoothed loss curves for multiple DataFrames and saves the plot to a specified directory.

    Args:
        dfs (List[Tuple[pd.DataFrame, str]]): List of tuples containing DataFrames and their labels.
        title (str): Title of the plot.
        smoothing_factor (float): Smoothing factor for the exponential moving average.
        save_path (str): Directory path to save the plot.
    """
    plt.figure(figsize=(10, 6))
    for df, label in dfs:
        if "lm loss" not in df.columns or "total elapsed time" not in df.columns:
            logging.warning(f"'lm loss' or 'total elapsed time' not in DataFrame columns for {label}")
            continue
        smoothed_loss = df["lm loss"].ewm(alpha=(1 - smoothing_factor)).mean()
        plt.plot(df["total elapsed time"], smoothed_loss, label=label, linestyle="--", linewidth=1.5)
    
    plt.title(title)
    plt.xlabel("Elapsed Time (s)")
    plt.ylabel("LM Loss")
    plt.grid(True)
    plt.legend()
    
    if display:
        plt.show()
    else: 
        # Ensure the output directory exists
        os.makedirs(save_path, exist_ok=True)
        # Save plot
        plot_filename = os.path.join(save_path, f"{title.replace(' ', '_')}.png")
        plt.savefig(plot_filename)
        plt.close()
    