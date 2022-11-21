def bellman_ford(g, s):
    d, p = dict(), dict()
    for v in g:  # 距离初始化为无穷大 前驱初始化为空
        d[v], p[v] = float("inf"), None
    d[s] = 0  # 源点到自己的距离为零

    for _ in range(len(g) - 1):  # 遍历|V|-1次
        for u in g:
            for v in g[u]:
                if d[v] > d[u] + g[u][v]:  # 如果 d(s,v) > d(s,u) + w(u,v)
                    d[v], p[v] = (d[u] + g[u][v], u)  # 更新当前最短距离和前驱

    for u in g:
        for v in g[u]:
            assert (d[v] <= d[u] + g[u][v]), "有负环"

    return d, p


g = {
    "s": {"t": 6, "y": 7},           # w(s,t) = 6, w(s,y) = 7
    "t": {"x": 5, "z": -4, "y": 8},  # w(t,x) = 5, w(t,z) = -4, w(t,y) = 8
    "y": {"z": 9, "x": -3},          # w(y,z) = 9, w(y,x) = -3
    "z": {"x": 7, "s": 2},           # w(z,x) = 7, w(z,s) = 2
    "x": {"t": -2},                  # w(x,t) = -2
}

d, p = bellman_ford(g, s="s")
print(d)
