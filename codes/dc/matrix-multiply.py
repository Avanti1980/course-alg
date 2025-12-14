import numpy as np


def mul(A, B, C, n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i, j] += A[i, k] * B[k, j]


def mul_rec(A, B, C, n):
    if n == 1:
        C[0, 0] += A[0, 0] * B[0, 0]
    else:
        mid = int(n / 2)

        # 四个子矩阵的索引
        block_11 = slice(None, mid), slice(None, mid)
        block_12 = slice(None, mid), slice(mid, None)
        block_21 = slice(mid, None), slice(None, mid)
        block_22 = slice(mid, None), slice(mid, None)

        mul_rec(A[block_11], B[block_11], C[block_11], mid)  # C11 += A11 B11
        mul_rec(A[block_12], B[block_21], C[block_11], mid)  # C11 += A12 B21
        mul_rec(A[block_11], B[block_12], C[block_12], mid)  # C12 += A11 B12
        mul_rec(A[block_12], B[block_22], C[block_12], mid)  # C12 += A12 B22
        mul_rec(A[block_21], B[block_11], C[block_21], mid)  # C21 += A21 B11
        mul_rec(A[block_22], B[block_21], C[block_21], mid)  # C21 += A22 B21
        mul_rec(A[block_21], B[block_12], C[block_22], mid)  # C22 += A21 B12
        mul_rec(A[block_22], B[block_22], C[block_22], mid)  # C22 += A22 B22


def mul_rec_strassen(A, B, C, n):
    if n == 1:
        C[0, 0] = A[0, 0] * B[0, 0]
    else:
        mid = int(n / 2)

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
        T1 = np.empty((mid, mid))
        mul_rec_strassen(R1, S1, T1, mid)

        T2 = np.empty((mid, mid))
        mul_rec_strassen(R2, S2, T2, mid)

        T3 = np.empty((mid, mid))
        mul_rec_strassen(R3, S3, T3, mid)

        T4 = np.empty((mid, mid))
        mul_rec_strassen(R4, S4, T4, mid)

        T5 = np.empty((mid, mid))
        mul_rec_strassen(R5, S5, T5, mid)

        T6 = np.empty((mid, mid))
        mul_rec_strassen(R6, S6, T6, mid)

        T7 = np.empty((mid, mid))
        mul_rec_strassen(R7, S7, T7, mid)

        # 8次加减计算C
        C[block_11] = T1 + T5
        C[block_12] = T2 + T3 + T4 + T5
        C[block_21] = T1 - T3 + T6 + T7
        C[block_22] = T2 + T7


m = n = 6

A = np.random.rand(n, n)
B = np.random.rand(n, n)
C1 = np.zeros((n, n))
mul(A, B, C1, n)

# 如果n不是2的幂次 将m置为最小的大于n的2的幂次
if (n & (n - 1)) != 0:
    m |= m >> 1
    m |= m >> 2
    m |= m >> 4
    m |= m >> 8
    m |= m >> 16
    m += 1

# 补零
A = np.pad(A, ((0, m - n), (0, m - n)), 'constant')
B = np.pad(B, ((0, m - n), (0, m - n)), 'constant')

C2 = np.zeros((m, m))
mul_rec(A, B, C2, m)
C2 = C2[:n, :n]

C3 = np.zeros((m, m))
mul_rec_strassen(A, B, C3, m)
C3 = C3[:n, :n]

print("C1 = \n", C1)
print("C2 = \n", C2)
print("C3 = \n", C3)

print((C1 - C2).max(), (C1 - C2).min())
print((C1 - C3).max(), (C1 - C3).min())
