# Common constants used across modules

common_columns = [
    "iteration", "consumed samples", "consumed tokens", "elapsed time per iteration (ms)",
    "learning rate", "global batch size", "lm loss", "loss scale", "actual seqlen",
    "number of skipped iterations", "number of nan iterations", "samples per second",
    "tokens per gpu per second (tgs)", "TFLOPs"
]

common_data_types = [
    int, int, int, float, float, int, float, float, int, int, int, float, float, float
]

common_regex_pattern = r"""
    iteration\s+(\d+)/\s+\d+\s+\|\s+
    consumed\ samples:\s+(\d+)\s+\|\s+
    consumed\ tokens:\s+(\d+)\s+\|\s+
    elapsed\ time\ per\ iteration\ \(ms\):\s+([\d\.]+)\s+\|\s+
    learning\ rate:\s+([\d\.E\+\-]+)\s+\|\s+
    global\ batch\ size:\s+(\d+)\s+\|\s+
    lm\ loss:\s+([\d\.E\+\-]+)\s+\|\s+
    loss\ scale:\s+([\d\.E\+\-]+)\s+\|\s+
    actual\ seqlen:\s+(\d+)\s+\|\s+
    number\ of\ skipped\ iterations:\s+(\d+)\s+\|\s+
    number\ of\ nan\ iterations:\s+(\d+)\s+\|\s+
    samples\ per\ second:\s+([\d\.]+)\s+\|\s+
    tokens\ per\ gpu\ per\ second\ \(tgs\):\s+([\d\.]+)\s+\|\s+
    TFLOPs:\s+([\d\.]+)
"""

pp_columns = [
    "iteration", "total_iterations", "consumed samples", "consumed tokens",
    "elapsed time per iteration (ms)", "learning rate", "global batch size",
    "lm loss", "loss scale", "grad norm", "num zeros", "actual seqlen",
    "number of skipped iterations", "number of nan iterations", "samples per second",
    "tokens per gpu per second (tgs)", "TFLOPs"
]

pp_data_types = [
    int, int, int, int, float, float, int, float, float, float, float, int, int, int, float, float, float
]

pp_regex_pattern = r"""
    iteration\s+(\d+)/\s+(\d+)\s+\|\s+
    consumed\ samples:\s+(\d+)\s+\|\s+
    consumed\ tokens:\s+(\d+)\s+\|\s+
    elapsed\ time\ per\ iteration\ \(ms\):\s+([\d\.]+)\s+\|\s+
    learning\ rate:\s+([\d\.E\+\-]+)\s+\|\s+
    global\ batch\ size:\s+(\d+)\s+\|\s+
    lm\ loss:\s+([\d\.E\+\-]+)\s+\|\s+
    loss\ scale:\s+([\d\.]+)\s+\|\s+
    grad\ norm:\s+([\d\.]+)\s+\|\s+
    num\ zeros:\s+([\d\.]+)\s+\|\s+
    actual\ seqlen:\s+(\d+)\s+\|\s+
    number\ of\ skipped\ iterations:\s+(\d+)\s+\|\s+
    number\ of\ nan\ iterations:\s+(\d+)\s+\|\s+
    samples\ per\ second:\s+([\d\.]+)\s+\|\s+
    tokens\ per\ gpu\ per\ second\ \(tgs\):\s+([\d\.]+)\s+\|\s+
    TFLOPs:\s+([\d\.]+)
"""