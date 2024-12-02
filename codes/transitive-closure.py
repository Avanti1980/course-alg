import numpy as np


def transitive_closure():
    t = np.zeros((n, n), dtype="int")
    for i in range(n):
        for j in range(n):
            if i == j or w[i, j] == 1:
                t[i, j] = 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                t[i, j] = t[i, j] | (t[i, k] & t[k, j])  # 更新t
    return t


# 邻接矩阵
w = np.array(
    [
        [0, float("inf"), float("inf"), float("inf")],
        [float("inf"), 0, 1, 1],
        [float("inf"), 1, 0, float("inf")],
        [1, float("inf"), 1, 0],
    ]
)
n = len(w)
print(transitive_closure())
