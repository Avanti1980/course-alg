import numpy as np


def init_p():  # 初始化前驱矩阵
    p = np.full((n, n), None)
    for i in range(n):
        for j in range(n):
            if j != i and not np.isinf(w[i, j]):
                p[i, j] = i + 1
    return p


def sp_all_dp():
    l = np.array(w, copy=True)
    p = init_p()  # 初始化前驱矩阵
    for _ in range(n - 2):
        ll = np.array(l, copy=True)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if ll[i, k] + w[k, j] < l[i, j]:
                        l[i, j] = ll[i, k] + w[k, j]  # 更新L
                        p[i, j] = k + 1  # 更新前驱
    return l, p


def sp_all_dp_plus():
    l = np.array(w, copy=True)
    p = init_p()  # 初始化前驱矩阵
    m = 1
    while m < n - 1:
        ll = np.array(l, copy=True)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if ll[i, k] + ll[k, j] < l[i, j]:
                        l[i, j] = ll[i, k] + ll[k, j]  # 更新L
                        p[i, j] = p[k, j]  # 更新前驱
        m *= 2
    return l, p


def floyd_warshall():
    d = np.array(w, copy=True)
    p = init_p()  # 初始化前驱矩阵
    for k in range(n):
        dd = np.array(d, copy=True)
        for i in range(n):
            for j in range(n):
                if dd[i, k] + dd[k, j] < d[i, j]:
                    d[i, j] = dd[i, k] + dd[k, j]  # 更新d
                    p[i, j] = p[k, j]  # 更新前驱
        print(d)
        print(p)
    return d, p


# 邻接矩阵
I = float("inf")
w = np.array(
    [
        [0, 3, 8, I, -4],
        [I, 0, I, 1, 7],
        [I, 4, 0, I, I],
        [2, I, -5, 0, I],
        [I, I, I, 6, 0],
    ]
)
n = len(w)

print(sp_all_dp())
print(sp_all_dp_plus())
print(floyd_warshall())
