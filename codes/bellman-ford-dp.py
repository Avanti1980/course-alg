def bellman_ford(g, s):
    d, p = dict(), dict()
    for v in g:  # 距离初始化为无穷大 前驱初始化为空
        d[v], p[v] = float("inf"), None
    d[s] = 0  # 源点到自己的最短路径长度为零

    print("初始：", d)

    for i in range(len(g) - 1):  # 遍历|V|-1次
        
        for u in g:
            for v in g[u]:  # 内部的二重for循环遍历所有边
                if d[v] > d[u] + g[u][v]:           # 松弛
                    d[v], p[v] = d[u] + g[u][v], u  # 更新当前最短距离和前驱

        print("初始：", d)

    for u in g:
        for v in g[u]:
            assert (d[v] <= d[u] + g[u][v]), "有负环"

    return d, p


g1 = {               # 用集合表示有向图g 元素为字典
    "s": {"x": 1},  # w(s,x) = 1
    "x": {"y": 1},  # w(x,y) = 1
    "y": {"z": 1},  # w(y,z) = 1
    "z": {"t": 1},  # w(z,t) = 1
    "t": {}
}

g2 = {               # 用集合表示有向图g 元素为字典
    "t": {},
    "z": {"t": 1},  # w(z,t) = 1
    "y": {"z": 1},  # w(y,z) = 1
    "x": {"y": 1},  # w(x,y) = 1
    "s": {"x": 1},  # w(s,x) = 1
}

d, p = bellman_ford(g1, s="s")
print(d)

d, p = bellman_ford(g2, s="s")
print(d)
# ---------------------------------------------------
# {'s': 0, 't': 2, 'y': 7, 'z': -2, 'x': 4}
# {'s': None, 't': 'x', 'y': 's', 'z': 't', 'x': 'y'}