def bellman_ford(s):
    d, p = dict(), dict()
    for v in g:  # 距离初始化为无穷大 前驱初始化为空
        d[v], p[v] = float("inf"), None
    d[s] = 0  # 源点到自己的最短路径长度为零

    for _ in range(len(g) - 1):  # 遍历|V|-1次
        for u in g:
            for v in g[u]:  # 内部的二重for循环遍历所有边
                if d[v] > d[u] + g[u][v]:           # 松弛
                    d[v], p[v] = d[u] + g[u][v], u  # 更新当前最短距离和前驱

    for u in g:
        for v in g[u]:
            assert (d[v] <= d[u] + g[u][v]), "有负环"

    return d, p


g = {                                # 用集合表示有向图g 元素为字典
    "s": {"t": 6, "y": 7},           # w(s,t) = 6, w(s,y) = 7
    "t": {"x": 5, "z": -4, "y": 8},  # w(t,x) = 5, w(t,z) = -4, w(t,y) = 8
    "y": {"z": 9, "x": -3},          # w(y,z) = 9, w(y,x) = -3
    "z": {"x": 7, "s": 2},           # w(z,x) = 7, w(z,s) = 2
    "x": {"t": -2},                  # w(x,t) = -2
}

d, p = bellman_ford(s="s")
print(d)
print(p)
# ---------------------------------------------------
# {'s': 0, 't': 2, 'y': 7, 'z': -2, 'x': 4}
# {'s': None, 't': 'x', 'y': 's', 'z': 't', 'x': 'y'}