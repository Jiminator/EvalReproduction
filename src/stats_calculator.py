import pandas as pd
import logging
from typing import Dict

def calculate_stats(df: pd.DataFrame) -> Dict[str, float]:
    """
    Calculates and returns statistics from the DataFrame.

    Args:
        df (pd.DataFrame): DataFrame containing the data.

    Returns:
        Dict[str, float]: Dictionary containing calculated statistics.
    """
    stats = {}
    try:
        stats["Average Elapsed Time per iteration (s)"] = round(float(df["elapsed time per iteration (ms)"].mean() / 1000), 4)
        stats["Average Samples Per Second"] = round(float(df["samples per second"].mean()), 4)
        stats["Average Tokens per GPU per Second (TGS)"] = round(float(df["tokens per gpu per second (tgs)"].mean()), 4)
        stats["Average TFLOPs"] = round(float(df["TFLOPs"].mean()), 4)
    except KeyError as e:
        logging.error(f"Column not found in DataFrame: {e}")
    return stats