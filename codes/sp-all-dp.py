def init_p(w):  # 初始化前驱矩阵
    p = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if j != i and w[i][j] < float("inf"):
                p[i][j] = i + 1
    return p


def sp_all_dp(w, n):
    l = [[w[i][j] for j in range(n)] for i in range(n)]
    p = init_p(w)  # 初始化前驱矩阵
    for m in range(n-2):
        sp_all_dp_extend(l, p, w, n)
    return l, p


def sp_all_dp_extend(l, p, w, n):
    ll = [[l[i][j] for j in range(n)] for i in range(n)]  # 备份上一轮的L
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if ll[i][k] + w[k][j] < l[i][j]:
                    l[i][j] = ll[i][k] + w[k][j]  # 更新L
                    p[i][j] = k + 1               # 更新前驱


def sp_all_dp_plus(w, n):
    l = [[w[i][j] for j in range(n)] for i in range(n)]
    p = init_p(w)  # 初始化前驱矩阵
    m = 1
    while m < n-1:
        sp_all_dp_plus_extend(l, p, n)
        m *= 2
    return l, p


def sp_all_dp_plus_extend(l, p, n):
    ll = [[l[i][j] for j in range(n)] for i in range(n)]  # 备份上一轮的L
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if ll[i][k] + ll[k][j] < l[i][j]:
                    l[i][j] = ll[i][k] + ll[k][j]  # 更新L
                    p[i][j] = p[k][j]              # 更新前驱


def floyd_warshall(w, n):
    d = [[w[i][j] for j in range(n)] for i in range(n)]
    p = init_p(w)  # 初始化前驱矩阵
    for k in range(n):
        dd = [[d[i][j] for j in range(n)] for i in range(n)]  # 备份上一轮的d
        for i in range(n):
            for j in range(n):
                if dd[i][k] + dd[k][j] < d[i][j]:
                    d[i][j] = dd[i][k] + dd[k][j]  # 更新d
                    p[i][j] = p[k][j]              # 更新前驱
    return d, p


# 邻接矩阵
w = [[0, 3, 8, float('inf'), -4],
     [float('inf'), 0, float('inf'), 1, 7],
     [float('inf'), 4, 0, float('inf'), float('inf')],
     [2, float('inf'), -5, 0, float('inf')],
     [float('inf'), float('inf'), float('inf'), 6, 0]
     ]
n = len(w)

l, p = sp_all_dp(w, n)
print(l, p)

l, p = sp_all_dp_plus(w, n)
print(l, p)

d, p = floyd_warshall(w, n)
print(d, p)
