def bellman_ford(g, s):
    d, p = dict(), dict()
    for v in g:  # 距离初始化为无穷大 前驱初始化为空
        d[v], p[v] = float("inf"), None
    d[s] = 0  # 源点到自己的距离为零

    for _ in range(len(g) - 1):
        for u in g:
            for v in g[u]:
                if d[v] > d[u] + g[u][v]:  # 如果 e(s,v) > e(s,u) + e(u,v)
                    d[v], p[v] = (d[u] + g[u][v], u)  # 更新

    for u in g:
        for v in g[u]:
            assert (d[v] <= d[u] + g[u][v]), "有负环"

    return d, p


g = {
    "s": {"t": 6, "y": 7},           # e(s,t) = 6, e(s,y) = 7
    "t": {"x": 5, "z": -4, "y": 8},  # e(t,x) = 5, e(t,z) = -4, e(t,y) = 8
    "y": {"z": 9, "x": -3},          # e(y,z) = 9, e(y,x) = -3
    "z": {"x": 7, "s": 2},           # e(z,x) = 7, e(z,s) = 2
    "x": {"t": -2},                  # e(x,t) = -2
}

d, p = bellman_ford(g, s="s")
print(d)
