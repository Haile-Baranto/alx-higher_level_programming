import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy and returns the result.

    Args:
        m_a (list): The first matrix represented as a list of lists.
        m_b (list): The second matrix represented as a list of lists.

    Returns:
        list: The resulting matrix after multiplying m_a and m_b.
        
    Example:
        m_a = [[1, 2, 3], [4, 5, 6]]
        m_b = [[7, 8], [9, 10], [11, 12]]
    """

    # Convert input matrices to NumPy arrays
   
    a = np.array(m_a)
    b = np.array(m_b)

    # Perform matrix multiplication using NumPy
    result = np.matmul(a, b)

    # Convert the result back to a nested list
    return result.tolist()