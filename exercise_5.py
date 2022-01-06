import numpy as np
from scipy.linalg import block_diag


def block_matrix_maker(matrices: np.ndarray) -> np.ndarray:
    """
    Returns a matrix, where the input matrices are diagonally connected.
    :param matrices: the matrices to connect
    :return: the block matrix containing the connected matrices
    """
    return block_diag(*matrices)  # block_diag expects multiple matrices as an argument, not a list --> unpack
