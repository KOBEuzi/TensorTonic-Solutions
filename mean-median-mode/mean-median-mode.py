from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    x = np.asarray(x,dtype=float)
    mean_val = float(np.mean(x))
    median_val = float(np.median(x))
    res = Counter(x)
    max_times = max(res.values())
    modes = [k for k,v in res.items() if v==max_times]
    mode = float(min(modes))
    return {"mean":mean_val,"median":median_val,"mode":mode}