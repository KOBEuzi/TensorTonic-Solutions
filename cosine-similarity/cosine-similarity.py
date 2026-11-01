import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    x = np.asarray(a,dtype=float)
    y = np.asarray(b,dtype=float)
    dot_product = np.dot(x,y)
    x_norm = np.linalg.norm(a)
    y_norm = np.linalg.norm(b)
    if x_norm==0 or y_norm==0:
        return 0.0
    return float(dot_product/(x_norm*y_norm))