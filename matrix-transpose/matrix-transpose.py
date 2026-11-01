import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    matrix = np.asarray(A,dtype=float)
    row,col = matrix.shape
    res = np.zeros((col,row),dtype=matrix.dtype)
    for i in range(col):
        for j in range(row):
            res[i][j] = matrix[j][i]
    return res