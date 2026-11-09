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
    if m == 1 or n == 1:
        return A + B

    mid_m, mid_n = m // 2, n // 2

    # 四个子矩阵的索引
    block_slices = [
        (slice(None, mid_m), slice(None, mid_n)),
        (slice(None, mid_m), slice(mid_n, None)),
        (slice(mid_m, None), slice(None, mid_n)),
        (slice(mid_m, None), slice(mid_n, None)),
    ]
    C = np.empty((m, n))
    for bs in block_slices:
        C[bs] = add_rec(A[bs], B[bs])

    return C


m, n = 5, 7
A, B = np.random.rand(m, n), np.random.rand(m, n)

C1 = add(A, B)
C2 = add_rec(A, B)

print((C1 - C2).max(), (C1 - C2).min())
