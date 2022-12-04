def optimal_bst():
    e = [[float("inf") for j in range(n+1)] for i in range(n+2)]
    w = [[0 for j in range(n+1)] for i in range(n+2)]
    root = [[0 for j in range(n+1)] for i in range(n+1)]
    for i in range(1, n+2):
        e[i][i-1] = w[i][i-1] = q[i-1]          # 边界情况
    for l in range(1, n+1):                     # 子问题 l = 1 -> n
        for i in range(1, n-l+2):               # 从第i个关键字
            j = i + l - 1                       # 到第j个关键字
            w[i][j] = w[i][j-1] + p[j] + q[j]   # 填写w表
            for r in range(i, j+1):             # 遍历寻找最优根节点
                t = e[i][r-1] + e[r+1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j] = t                 # 更新期望搜索代价
                    root[i][j] = r              # 更新最优根节点
    return e, w, root


p = [0, 0.15, 0.1, 0.05, 0.1, 0.2]
q = [0.05, 0.1, 0.05, 0.05, 0.05, 0.1]
n = len(p) - 1
e, w, root = optimal_bst()
print(e[1][n])
print("e =", [e[i][:n+1] for i in range(1, n+2)])
print("w =", [w[i][:n+1] for i in range(1, n+2)])
print("root =", [root[i][1:n+1] for i in range(1, n+1)])
--------------------------------------------------------
2.75
e = [[0.05, 0.45, 0.9,  1.25, 1.75, 2.75],
     [inf,  0.1,  0.4,  0.7,  1.2,  2   ],
     [inf,  inf,  0.05, 0.25, 0.6,  1.3 ],
     [inf,  inf,  inf,  0.05, 0.3,  0.9 ],
     [inf,  inf,  inf,  inf,  0.05, 0.5 ],
     [inf,  inf,  inf,  inf,  inf,  0.1 ]]
w = [[0.05, 0.3,  0.45, 0.55, 0.7,  1.0 ],
     [0,    0.1,  0.25, 0.35, 0.5,  0.8 ],
     [0,    0,    0.05, 0.15, 0.3,  0.6 ],
     [0,    0,    0,    0.05, 0.2,  0.5 ],
     [0,    0,    0,    0,    0.05, 0.35],
     [0,    0,    0,    0,    0,    0.1 ]]
root = [[1, 1, 2, 2, 2],
        [0, 2, 2, 2, 4],
        [0, 0, 3, 4, 5],
        [0, 0, 0, 4, 5],
        [0, 0, 0, 0, 5]]
