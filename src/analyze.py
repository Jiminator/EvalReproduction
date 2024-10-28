import logging
from log_parser import parse_log_file
from plotting import plot_smoothed_loss
from stats_calculator import calculate_stats
from constants import (
    common_columns, common_data_types, common_regex_pattern,
    pp_columns, pp_data_types, pp_regex_pattern
)

def main():
    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    # Process log files
    df = parse_log_file(
        file_path='./data/1k_DP/training_run.log',
        regex_pattern=common_regex_pattern,
        columns=common_columns,
        data_types=common_data_types
    )

    df_DP = parse_log_file(
        file_path='./data/100_DP/training_run.log',
        regex_pattern=common_regex_pattern,
        columns=common_columns,
        data_types=common_data_types
    )

    df_TP = parse_log_file(
        file_path='./data/100_DP_TP/training_run.log',
        regex_pattern=common_regex_pattern,
        columns=common_columns,
        data_types=common_data_types
    )

    df_PP = parse_log_file(
        file_path='./data/100_DP_PP/training_run.log',
        regex_pattern=pp_regex_pattern,
        columns=pp_columns,
        data_types=pp_data_types
    )

    # Calculate statistics
    stats = calculate_stats(df)
    stats_DP = calculate_stats(df_DP)
    stats_TP = calculate_stats(df_TP)
    stats_PP = calculate_stats(df_PP)

    logging.info(f"Full Pre-training Stats: {stats}")
    logging.info(f"DP Stats: {stats_DP}")
    logging.info(f"TP Stats: {stats_TP}")
    logging.info(f"PP Stats: {stats_PP}")

    # Plot smoothed loss
    dfs_to_plot = [
        (df_PP, "PP Only"),
        (df_DP, "DP Only"),
        (df_TP, "TP Only")
    ]

    plot_smoothed_loss(
        dfs=[(df, "DP")],
        title="DeepSpeed GPT-2 Full Pre-Training",
        smoothing_factor=0.6
    )

    plot_smoothed_loss(
        dfs=dfs_to_plot,
        title="Ablation Study of Model Parallelism on Training Loss",
        smoothing_factor=0.6
    )

if __name__ == "__main__":
    main()