import numpy as np


def matrix_chain(p, n):
    m, s = np.zeros((n + 1, n + 1)), np.zeros((n + 1, n + 1))
    for l in range(2, n + 1):           # 子问题长度 l = 2 -> n
        for i in range(1, n - l + 2):   # 从第i个矩阵开始
            j = i + l - 1               # 到第j个矩阵结束
            m[i, j] = float("inf")      # 初始化为无穷大
            for k in range(i, j):       # 遍历最优分开位置
                cost = m[i, k] + m[k + 1, j] + p[i - 1] * p[k] * p[j]
                if cost < m[i, j]:
                    m[i, j] = cost
                    s[i, j] = k
    return m.astype(int), s.astype(int)


def print_sol(s, i, j):
    if i == j:
        print("A%d" % (i), end='')
    else:
        print("(", end='')
        print_sol(s, i, s[i, j])
        print_sol(s, s[i, j] + 1, j)
        print(")", end='')


p = [30, 35, 15, 5, 10, 20, 25]
n = len(p) - 1  # 矩阵个数
m, s = matrix_chain(p, n)
print(m[1, n])
print(m[1:, 1:])
print(s[1:, 1:])
print_sol(s, 1, n)
------------------------------------------
15125
[[    0 15750  7875  9375 11875 15125]
 [    0     0  2625  4375  7125 10500]
 [    0     0     0   750  2500  5375]
 [    0     0     0     0  1000  3500]
 [    0     0     0     0     0  5000]
 [    0     0     0     0     0     0]]
[[0 1 1 3 3 3]
 [0 0 2 3 3 3]
 [0 0 0 3 3 3]
 [0 0 0 0 4 5]
 [0 0 0 0 0 5]
 [0 0 0 0 0 0]]
((A1(A2A3))((A4A5)A6))
