import re
import pandas as pd
import logging
from typing import List

def parse_log_file(
    file_path: str,
    regex_pattern: str,
    columns: List[str],
    data_types: List[type]
) -> pd.DataFrame:
    """
    Parses a log file using a provided regex pattern and returns a DataFrame.

    Args:
        file_path (str): Path to the log file.
        regex_pattern (str): Regex pattern to parse the log entries.
        columns (List[str]): List of column names for the DataFrame.
        data_types (List[type]): List of data types for each column.

    Returns:
        pd.DataFrame: DataFrame containing the parsed data.
    """
    try:
        with open(file_path, 'r') as file:
            log_data = file.read()
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return pd.DataFrame(columns=columns)
    
    pattern = re.compile(regex_pattern, re.VERBOSE)
    data = []

    for match in pattern.findall(log_data):
        parsed_row = [dtype(value) for dtype, value in zip(data_types, match)]
        data.append(parsed_row)
    
    df = pd.DataFrame(data, columns=columns)
    if "elapsed time per iteration (ms)" in df.columns:
        df["total elapsed time"] = df["elapsed time per iteration (ms)"].cumsum() / 1000
    return df