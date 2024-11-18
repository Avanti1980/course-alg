import numpy as np


def add(A, B, C, m, n):
    for i in range(m):
        for j in range(n):
            C[i, j] = A[i, j] + B[i, j]


def add_rec(A, B, C, shape):
    m, n = shape
    if m == 1 or n == 1:
        C[:] = A[:] + B[:]
    else:
        mid_m, mid_n = int(m / 2), int(n / 2)

        # 四个子矩阵的索引
        block_11 = slice(None, mid_m), slice(None, mid_n)
        block_12 = slice(None, mid_m), slice(mid_n, None)
        block_21 = slice(mid_m, None), slice(None, mid_n)
        block_22 = slice(mid_m, None), slice(mid_n, None)

        add_rec(A[block_11], B[block_11], C[block_11], A[block_11].shape)
        add_rec(A[block_12], B[block_12], C[block_12], A[block_12].shape)
        add_rec(A[block_21], B[block_21], C[block_21], A[block_21].shape)
        add_rec(A[block_22], B[block_22], C[block_22], A[block_22].shape)


m, n = 5, 7
A, B = np.random.rand(m, n), np.random.rand(m, n)
C1, C2 = np.empty((m, n)), np.empty((m, n))
add(A, B, C1, m, n)
add_rec(A, B, C2, [m, n])

# print("C1 =\n", C1)
# print("C2 =\n", C2)
# print("C1 - C2 =\n", C1 - C2)
print((C1 - C2).max(), (C1 - C2).min())
