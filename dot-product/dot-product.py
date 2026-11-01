import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    res =0.0; n = len(x)
    for i in range(n):
        res +=x[i]*y[i]
    return res