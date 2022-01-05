import numpy
import numpy as np


def chess_board_maker(n: int) -> numpy.ndarray:
    """
    Make a chessboard-like matrix.

    :param n: size of the matrix
    :return: the chessboard-like matrix
    """
    matrix_flat = np.ones(n * n)
    matrix_flat[::2] *= -1  # this is the "base" for the matrix, it looks something like this: [1, -1, 1, -1, 1, -1...]

    # if n is even, we have to multiply the matrix with its own transpose,
    # if n is odd, the chessboard is almost ready, but the numbers are "inverted", so multiply by -1
    return np.reshape(np.array(matrix_flat), (n, n)).transpose() * np.reshape(np.array(matrix_flat), (n, n)) \
        if n % 2 == 0 else np.reshape(np.array(matrix_flat), (n, n)) * -1