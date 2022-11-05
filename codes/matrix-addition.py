import numpy as np


def add(A, B, C, n):
    for i in range(n):
        for j in range(n):
            C[i, j] = A[i, j] + B[i, j]


def add_rec_copy(A, B, C, n):
    if n == 1:
        C[0, 0] = A[0, 0] + B[0, 0]
    else:
        mid = int(n/2)

        # 复制子矩阵到 A11 A12 A21 A22 B11 B12 B21 B22
        A11, B11 = A[:mid, :mid], B[:mid, :mid]
        A12, B12 = A[:mid, mid:], B[:mid, mid:]
        A21, B21 = A[mid:, :mid], B[mid:, :mid]
        A22, B22 = A[mid:, mid:], B[mid:, mid:]

        # 依次计算 C11 C12 C21 C22 并复制到 C 的对应位置
        add_rec_copy(A11, B11, C[:mid, :mid], mid)
        add_rec_copy(A12, B12, C[:mid, mid:], mid)
        add_rec_copy(A21, B21, C[mid:, :mid], mid)
        add_rec_copy(A22, B22, C[mid:, mid:], mid)


def add_rec_nocopy(A, B, C, ar1, ar2, ac1, ac2, br1, br2, bc1, bc2, cr1, cr2, cc1, cc2):
    if ar1 == ar2 - 1:
        C[cr1, cc1] = A[ar1, ac1] + B[br1, bc1]
    else:
        ar, ac = int((ar1 + ar2) / 2), int((ac1 + ac2) / 2)
        br, bc = int((br1 + br2) / 2), int((bc1 + bc2) / 2)
        cr, cc = int((cr1 + cr2) / 2), int((cc1 + cc2) / 2)

        # C11 = A11 + B11
        add_rec_nocopy(A, B, C, ar1, ar, ac1, ac, br1, br, bc1, bc, cr1, cr, cc1, cc)

        # C12 = A12 + B12
        add_rec_nocopy(A, B, C, ar1, ar, ac, ac2, br1, br, bc, bc2, cr1, cr, cc, cc2)

        # C21 = A21 + B21
        add_rec_nocopy(A, B, C, ar, ar2, ac1, ac, br, br2, bc1, bc, cr, cr2, cc1, cc)

        # C22 = A22 + B22
        add_rec_nocopy(A, B, C, ar, ar2, ac, ac2, br, br2, bc, bc2, cr, cr2, cc, cc2)


m = n = 5
A = np.random.random((n, n))
B = np.random.random((n, n))

C1 = np.zeros((n, n))
add(A, B, C1, n)

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
add_rec_copy(A, B, C2, m)
C2 = C2[:n, :n]

C3 = np.zeros((m, m))
add_rec_nocopy(A, B, C3, 0, m, 0, m, 0, m, 0, m, 0, m, 0, m)
C3 = C3[:n, :n]

# print("C1 = ", C1)
# print("C2 = ", C2)
# print("C3 = ", C3)

print((C1-C2).max(), (C1-C2).min())
print((C1-C3).max(), (C1-C3).min())
