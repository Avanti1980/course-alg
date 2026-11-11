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
    if n == 1:
        return A * B

    mid = n // 2

    # 四个子矩阵的索引
    block_11 = slice(None, mid), slice(None, mid)
    block_12 = slice(None, mid), slice(mid, None)
    block_21 = slice(mid, None), slice(None, mid)
    block_22 = slice(mid, None), slice(mid, None)

    C = np.zeros((n, n))
    C[block_11] = mul_rec(A[block_11], B[block_11]) + \
        mul_rec(A[block_12], B[block_21])
    C[block_12] = mul_rec(A[block_11], B[block_12]) + \
        mul_rec(A[block_12], B[block_22])
    C[block_21] = mul_rec(A[block_21], B[block_11]) + \
        mul_rec(A[block_22], B[block_21])
    C[block_22] = mul_rec(A[block_21], B[block_12]) + \
        mul_rec(A[block_22], B[block_22])

    return C


def mul_rec_strassen(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    n = A.shape[0]
    if n == 1:
        return A * B

    mid = n // 2

    # 四个子矩阵的索引
    block_11 = slice(None, mid), slice(None, mid)
    block_12 = slice(None, mid), slice(mid, None)
    block_21 = slice(mid, None), slice(None, mid)
    block_22 = slice(mid, None), slice(mid, None)

    # 10次加减计算中间变量
    R1 = A[block_11]
    R2 = A[block_22]
    R3 = A[block_11] - A[block_22]
    R4 = A[block_12] - A[block_22]
    R5 = A[block_11] - A[block_12]
    R6 = A[block_11] - A[block_21]
    R7 = A[block_21] - A[block_22]

    S1 = B[block_11] + B[block_21]
    S2 = B[block_12] + B[block_22]
    S3 = B[block_12] + B[block_21]
    S4 = B[block_22] - B[block_21]
    S5 = -B[block_21]
    S6 = B[block_12] - B[block_11]
    S7 = B[block_12]

    # 7个子问题 递归调用
    T1 = mul_rec_strassen(R1, S1)
    T2 = mul_rec_strassen(R2, S2)
    T3 = mul_rec_strassen(R3, S3)
    T4 = mul_rec_strassen(R4, S4)
    T5 = mul_rec_strassen(R5, S5)
    T6 = mul_rec_strassen(R6, S6)
    T7 = mul_rec_strassen(R7, S7)

    C = np.empty((n, n))

    # 8次加减计算C
    C[block_11] = T1 + T5
    C[block_12] = T2 + T3 + T4 + T5
    C[block_21] = T1 - T3 + T6 + T7
    C[block_22] = T2 + T7

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

    print((C1 - C2).max(), (C1 - C2).min())
    print((C1 - C3).max(), (C1 - C3).min())

np.save('matrix-multiply-time-cost.npy', time_cost)
