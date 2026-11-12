import numpy as np


def add(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    m, n = A.shape
    C = np.empty((m, n))
    for i in range(m):
        for j in range(n):
            C[i, j] = A[i, j] + B[i, j]
    return C


def add_rec(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    m, n = A.shape
    if m <= 1 or n <= 1:
        return A + B

    mid_m, mid_n = m // 2, n // 2

    # 四个子矩阵
    A11, A12 = A[:mid_m, :mid_n], A[:mid_m, mid_n:]
    A21, A22 = A[mid_m:, :mid_n], A[mid_m:, mid_n:]
    B11, B12 = B[:mid_m, :mid_n], B[:mid_m, mid_n:]
    B21, B22 = B[mid_m:, :mid_n], B[mid_m:, mid_n:]

    C = np.empty((m, n))
    C[:mid_m, :mid_n] = add_rec(A11, B11)
    C[:mid_m, mid_n:] = add_rec(A12, B12)
    C[mid_m:, :mid_n] = add_rec(A21, B21)
    C[mid_m:, mid_n:] = add_rec(A22, B22)

    return C


m, n = 1024, 1024
A, B = np.random.rand(m, n), np.random.rand(m, n)

C1 = add(A, B)
C2 = add_rec(A, B)

print(np.allclose(C1, C2))
