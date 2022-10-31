import numpy as np
from math import ceil


def mul(A, B, C, n):
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
        A11, B11 = A[0:mid, 0:mid], B[0:mid, 0:mid]
        A12, B12 = A[0:mid, mid:n], B[0:mid, mid:n]
        A21, B21 = A[mid:n, 0:mid], B[mid:n, 0:mid]
        A22, B22 = A[mid:n, mid:n], B[mid:n, mid:n]

        # 依次计算 C11 C12 C21 C22 并复制到 C 的对应位置
        mul_rec_copy(A11, B11, C[0:mid, 0:mid], mid)
        mul_rec_copy(A12, B21, C[0:mid, 0:mid], mid)

        mul_rec_copy(A11, B12, C[0:mid, mid:n], mid)
        mul_rec_copy(A12, B22, C[0:mid, mid:n], mid)

        mul_rec_copy(A21, B11, C[mid:n, 0:mid], mid)
        mul_rec_copy(A22, B21, C[mid:n, 0:mid], mid)

        mul_rec_copy(A21, B12, C[mid:n, mid:n], mid)
        mul_rec_copy(A22, B22, C[mid:n, mid:n], mid)


def mul_rec_nocopy(A, B, C, ar1, ar2, ac1, ac2, br1, br2, bc1, bc2, cr1, cr2, cc1, cc2):
    if ar1 == ar2 - 1:
        C[cr1, cc1] += A[ar1, ac1] * B[br1, bc1]
    else:
        ar, ac = int((ar1 + ar2) / 2), int((ac1 + ac2) / 2)
        br, bc = int((br1 + br2) / 2), int((bc1 + bc2) / 2)
        cr, cc = int((cr1 + cr2) / 2), int((cc1 + cc2) / 2)

        # 不进行子矩阵复制 直接将子矩阵的索引作为参数

        # C11 += A11 B11
        mul_rec_nocopy(A, B, C, ar1, ar, ac1, ac, br1, br, bc1, bc, cr1, cr, cc1, cc)

        # C11 += A12 B21
        mul_rec_nocopy(A, B, C, ar1, ar, ac, ac2, br, br2, bc1, bc, cr1, cr, cc1, cc)

        # C12 += A11 B12
        mul_rec_nocopy(A, B, C, ar1, ar, ac1, ac, br1, br, bc, bc2, cr1, cr, cc, cc2)

        # C12 += A12 B22
        mul_rec_nocopy(A, B, C, ar1, ar, ac, ac2, br, br2, bc, bc2, cr1, cr, cc, cc2)

        # C21 += A21 B11
        mul_rec_nocopy(A, B, C, ar, ar2, ac1, ac, br1, br, bc1, bc, cr, cr2, cc1, cc)

        # C21 += A22 B21
        mul_rec_nocopy(A, B, C, ar, ar2, ac, ac2, br, br2, bc1, bc, cr, cr2, cc1, cc)

        # C22 += A21 B12
        mul_rec_nocopy(A, B, C, ar, ar2, ac1, ac, br1, br, bc, bc2, cr, cr2, cc, cc2)

        # C22 += A22 B22
        mul_rec_nocopy(A, B, C, ar, ar2, ac, ac2, br, br2, bc, bc2, cr, cr2, cc, cc2)


n = 8

A = np.random.random((n, n))
B = np.random.random((n, n))

C1 = np.zeros((n, n))
mul(A, B, C1, n)

C2 = np.zeros((n, n))
mul_rec_copy(A, B, C2, n)

C3 = np.zeros((n, n))
mul_rec_nocopy(A, B, C3, 0, n, 0, n, 0, n, 0, n, 0, n, 0, n)

print(np.linalg.norm(C1-C2))
print(np.linalg.norm(C1-C3))
