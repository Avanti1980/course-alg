def bellman_ford(g, s):
    d, p = dict(), dict()
    for v in g:  # 距离初始化为无穷大 前驱初始化为空
        d[v], p[v] = float("inf"), None
    d[s] = 0  # 源点到自己的最短路径长度为零
    print(0, d)
    for i in range(len(g) - 1):  # 遍历|V|-1次
        dd = {key: value for (key, value) in d.items()}  # 备份上一轮的d
        for u in g:
            for v in g[u]:  # 内部的二重for循环遍历所有边
                if d[v] > dd[u] + g[u][v]:           # 松弛
                    d[v], p[v] = dd[u] + g[u][v], u  # 更新当前最短距离和前驱
        print(i+1, d)

    for u in g:
        for v in g[u]:
            assert (d[v] <= d[u] + g[u][v]), "有负环"

    return d, p


g = {  # s -> x -> y -> z -> t
    "s": {"x": 1},  # w(s,x) = 1
    "x": {"y": 1},  # w(x,y) = 1
    "y": {"z": 1},  # w(y,z) = 1
    "z": {"t": 1},  # w(z,t) = 1
    "t": {}
}

d, p = bellman_ford(g, s="s")
# ---------------------------------------------------
# 0 {'s': 0, 'x': inf, 'y': inf, 'z': inf, 't': inf}
# 1 {'s': 0, 'x': 1, 'y': inf, 'z': inf, 't': inf}
# 2 {'s': 0, 'x': 1, 'y': 2, 'z': inf, 't': inf}
# 3 {'s': 0, 'x': 1, 'y': 2, 'z': 3, 't': inf}
# 4 {'s': 0, 'x': 1, 'y': 2, 'z': 3, 't': 4}

g = {  # s -> x -> y -> {z, t}
    "s": {"x": 1},          # w(s,x) = 1
    "x": {"y": 1},          # w(x,y) = 1
    "y": {"z": 1, "t": 1},  # w(y,z) = 1, w(y,t) = 1
    "z": {},
    "t": {}
}

d, p = bellman_ford(g, s="s")
# ---------------------------------------------------
# 0 {'s': 0, 'x': inf, 'y': inf, 'z': inf, 't': inf}
# 1 {'s': 0, 'x': 1, 'y': inf, 'z': inf, 't': inf}
# 2 {'s': 0, 'x': 1, 'y': 2, 'z': inf, 't': inf}
# 3 {'s': 0, 'x': 1, 'y': 2, 'z': 3, 't': 3}
# 4 {'s': 0, 'x': 1, 'y': 2, 'z': 3, 't': 3}

g = {  # s -> {x, y}, y -> {z, t}
    "s": {"x": 1, "y": 1},  # w(s,x) = 1, w(s,y) = 1
    "x": {},
    "y": {"z": 1, "t": 1},  # w(y,z) = 1, w(y,t) = 1
    "z": {},
    "t": {}
}

d, p = bellman_ford(g, s="s")
# ---------------------------------------------------
# 0 {'s': 0, 'x': inf, 'y': inf, 'z': inf, 't': inf}
# 1 {'s': 0, 'x': 1, 'y': 1, 'z': inf, 't': inf}
# 2 {'s': 0, 'x': 1, 'y': 1, 'z': 2, 't': 2}
# 3 {'s': 0, 'x': 1, 'y': 1, 'z': 2, 't': 2}
# 4 {'s': 0, 'x': 1, 'y': 1, 'z': 2, 't': 2}
