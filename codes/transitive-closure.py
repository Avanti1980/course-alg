def transitive_closure():
    t = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j or w[i][j] == 1:
                t[i][j] = 1
    for k in range(n):
        tt = [[t[i][j] for j in range(n)] for i in range(n)]  # 备份上一轮的t
        for i in range(n):
            for j in range(n):
                t[i][j] = tt[i][j] | (tt[i][k] & tt[k][j])    # 更新t
    return t


# 邻接矩阵
w = [[0, float('inf'), float('inf'), float('inf')],
     [float('inf'), 0, 1, 1],
     [float('inf'), 1, 0, float('inf')],
     [1, float('inf'), 1, 0]]
n = len(w)
print(transitive_closure())
