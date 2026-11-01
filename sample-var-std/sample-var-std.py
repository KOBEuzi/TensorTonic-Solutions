import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x = np.asarray(x,dtype=float)
    n = len(x)
    var = float(np.sum((x-np.mean(x))**2)/(n-1))
    std = float(np.sqrt(var))
    return {"variance":var,"standard_deviation":std}
    
    