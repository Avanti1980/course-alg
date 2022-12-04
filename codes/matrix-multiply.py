import numpy as np


def mul(C):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i, j] += A[i, k] * B[k, j]


def mul_rec_copy(A, B, C, n):
    if n == 1:
        C[0, 0] += A[0, 0] * B[0, 0]
    else:
        mid = int(n/2)

        # 复制子矩阵到 A11 A12 A21 A22 B11 B12 B21 B22
        A11, B11 = A[:mid, :mid], B[:mid, :mid]
        A12, B12 = A[:mid, mid:], B[:mid, mid:]
        A21, B21 = A[mid:, :mid], B[mid:, :mid]
        A22, B22 = A[mid:, mid:], B[mid:, mid:]

        # 依次计算 C11 C12 C21 C22 并复制到 C 的对应位置
        mul_rec_copy(A11, B11, C[:mid, :mid], mid)
        mul_rec_copy(A12, B21, C[:mid, :mid], mid)

        mul_rec_copy(A11, B12, C[:mid, mid:], mid)
        mul_rec_copy(A12, B22, C[:mid, mid:], mid)

        mul_rec_copy(A21, B11, C[mid:, :mid], mid)
        mul_rec_copy(A22, B21, C[mid:, :mid], mid)

        mul_rec_copy(A21, B12, C[mid:, mid:], mid)
        mul_rec_copy(A22, B22, C[mid:, mid:], mid)


def mul_rec_nocopy(C, ar1, ar2, ac1, ac2, br1, br2, bc1, bc2, cr1, cr2, cc1, cc2):
    if ar1 == ar2 - 1:
        C[cr1, cc1] += A[ar1, ac1] * B[br1, bc1]
    else:
        ar, ac = int((ar1 + ar2) / 2), int((ac1 + ac2) / 2)
        br, bc = int((br1 + br2) / 2), int((bc1 + bc2) / 2)
        cr, cc = int((cr1 + cr2) / 2), int((cc1 + cc2) / 2)

        # 不进行子矩阵复制 直接将子矩阵的索引作为参数

        # C11 += A11 B11
        mul_rec_nocopy(C, ar1, ar, ac1, ac, br1, br, bc1, bc, cr1, cr, cc1, cc)

        # C11 += A12 B21
        mul_rec_nocopy(C, ar1, ar, ac, ac2, br, br2, bc1, bc, cr1, cr, cc1, cc)

        # C12 += A11 B12
        mul_rec_nocopy(C, ar1, ar, ac1, ac, br1, br, bc, bc2, cr1, cr, cc, cc2)

        # C12 += A12 B22
        mul_rec_nocopy(C, ar1, ar, ac, ac2, br, br2, bc, bc2, cr1, cr, cc, cc2)

        # C21 += A21 B11
        mul_rec_nocopy(C, ar, ar2, ac1, ac, br1, br, bc1, bc, cr, cr2, cc1, cc)

        # C21 += A22 B21
        mul_rec_nocopy(C, ar, ar2, ac, ac2, br, br2, bc1, bc, cr, cr2, cc1, cc)

        # C22 += A21 B12
        mul_rec_nocopy(C, ar, ar2, ac1, ac, br1, br, bc, bc2, cr, cr2, cc, cc2)

        # C22 += A22 B22
        mul_rec_nocopy(C, ar, ar2, ac, ac2, br, br2, bc, bc2, cr, cr2, cc, cc2)


def mul_rec_strassen(A, B, C, n):
    if n == 1:
        C[0, 0] += A[0, 0] * B[0, 0]
    else:
        mid = int(n/2)

        A11, B11 = A[:mid, :mid], B[:mid, :mid]
        A12, B12 = A[:mid, mid:], B[:mid, mid:]
        A21, B21 = A[mid:, :mid], B[mid:, :mid]
        A22, B22 = A[mid:, mid:], B[mid:, mid:]

        # 10次加减计算中间变量
        R1, R2, R3, R4, R5, R6, R7 = A11, A22, A11-A22, A12-A22, A11-A12, A11-A21, A21-A22
        S1, S2, S3, S4, S5, S6, S7 = B11+B21, B12+B22, B12+B21, B22-B21, -B21, B12-B11, B12

        # 7个子问题 递归调用
        T1 = np.zeros((mid, mid))
        mul_rec_strassen(R1, S1, T1, mid)

        T2 = np.zeros((mid, mid))
        mul_rec_strassen(R2, S2, T2, mid)

        T3 = np.zeros((mid, mid))
        mul_rec_strassen(R3, S3, T3, mid)

        T4 = np.zeros((mid, mid))
        mul_rec_strassen(R4, S4, T4, mid)

        T5 = np.zeros((mid, mid))
        mul_rec_strassen(R5, S5, T5, mid)

        T6 = np.zeros((mid, mid))
        mul_rec_strassen(R6, S6, T6, mid)

        T7 = np.zeros((mid, mid))
        mul_rec_strassen(R7, S7, T7, mid)

        # 8次加减计算C
        C[:mid, :mid] = T1 + T5
        C[:mid, mid:] = T2 + T3 + T4 + T5
        C[mid:, :mid] = T1 - T3 + T6 + T7
        C[mid:, mid:] = T2 + T7


m = n = 8

A = np.random.random((n, n))
B = np.random.random((n, n))
C1 = np.zeros((n, n))
mul(C1)

# 如果n不是2的幂次 将m置为最小的大于n的2的幂次
if (n & (n - 1)) != 0:
    m |= m >> 1
    m |= m >> 2
    m |= m >> 4
    m |= m >> 8
    m |= m >> 16
    m += 1

# 补零
A = np.pad(A, ((0, m-n), (0, m-n)), 'constant')
B = np.pad(B, ((0, m-n), (0, m-n)), 'constant')

C2 = np.zeros((m, m))
mul_rec_copy(A, B, C2, m)
C2 = C2[:n, :n]

C3 = np.zeros((m, m))
mul_rec_nocopy(C3, 0, m, 0, m, 0, m, 0, m, 0, m, 0, m)
C3 = C3[:n, :n]

C4 = np.zeros((m, m))
mul_rec_strassen(A, B, C4, m)
C4 = C4[:n, :n]

# print("C1 = ", C1)
# print("C2 = ", C2)
# print("C3 = ", C3)
# print("C4 = ", C4)

print((C1-C2).max(), (C1-C2).min())
print((C1-C3).max(), (C1-C3).min())
print((C1-C4).max(), (C1-C4).min())
