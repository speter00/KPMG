import numpy
import numpy as np


def norm_by_row(matrix: numpy.ndarray) -> numpy.ndarray:
    """
    Calculates the Euclidean norm for each row in the input matrix.

    :param matrix: the input matrix
    :return: a numpy array of the Euclidean norms for each row
    """
    return np.sqrt(np.sum(matrix**2, axis=1))
