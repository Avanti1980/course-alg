import time
import numpy as np


def mul(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    n = A.shape[0]
    C = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i, j] += A[i, k] * B[k, j]
    return C


def mul_rec(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    n = A.shape[0]
    if n <= 1:
        return A @ B

    mid = n // 2

    # 四个子矩阵
    A11, A12 = A[:mid, :mid], A[:mid, mid:]
    A21, A22 = A[mid:, :mid], A[mid:, mid:]
    B11, B12 = B[:mid, :mid], B[:mid, mid:]
    B21, B22 = B[mid:, :mid], B[mid:, mid:]

    C = np.empty_like(A)
    C[:mid, :mid] = mul_rec(A11, B11) + mul_rec(A12, B21)
    C[:mid, mid:] = mul_rec(A11, B12) + mul_rec(A12, B22)
    C[mid:, :mid] = mul_rec(A21, B11) + mul_rec(A22, B21)
    C[mid:, mid:] = mul_rec(A21, B12) + mul_rec(A22, B22)

    return C


def mul_rec_strassen(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    n = A.shape[0]
    if n <= 1:
        return A @ B

    mid = n // 2

    # 四个子矩阵
    A11, A12 = A[:mid, :mid], A[:mid, mid:]
    A21, A22 = A[mid:, :mid], A[mid:, mid:]
    B11, B12 = B[:mid, :mid], B[:mid, mid:]
    B21, B22 = B[mid:, :mid], B[mid:, mid:]

    # 7个子问题 递归调用
    T1 = mul_rec_strassen(A11, B11 + B21)
    T2 = mul_rec_strassen(A22, B12 + B22)
    T3 = mul_rec_strassen(A11 - A22, B12 + B21)
    T4 = mul_rec_strassen(A12 - A22, B22 - B21)
    T5 = mul_rec_strassen(A11 - A12, -B21)
    T6 = mul_rec_strassen(A11 - A21, B12 - B11)
    T7 = mul_rec_strassen(A21 - A22, B12)

    # 8次加减计算C
    C = np.empty((n, n))
    C[:mid, :mid] = T1 + T5
    C[:mid, mid:] = T2 + T3 + T4 + T5
    C[mid:, :mid] = T1 - T3 + T6 + T7
    C[mid:, mid:] = T2 + T7

    return C


np.random.seed(0)

trial = 6
time_cost = np.zeros((trial, 3))

for t in range(trial):

    n = int(2**(t + 6))
    A, B = np.random.rand(n, n), np.random.rand(n, n)

    start = time.perf_counter()
    C1 = mul(A, B)
    time_cost[t, 0] = time.perf_counter() - start

    start = time.perf_counter()
    C2 = mul_rec(A, B)
    time_cost[t, 1] = time.perf_counter() - start

    start = time.perf_counter()
    C3 = mul_rec_strassen(A, B)
    time_cost[t, 2] = time.perf_counter() - start

    print(np.allclose(C1, C2))
    print(np.allclose(C1, C3))

np.save('matrix-multiply-time-cost.npy', time_cost)
