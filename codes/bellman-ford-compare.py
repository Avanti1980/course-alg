def bellman_ford_dp(g, s):
    d = dict()
    for v in g:  # 距离初始化为无穷大 前驱初始化为空
        d[v] = float("inf")
    d[s] = 0  # 源点到自己的最短路径长度为零
    print(0, d)
    for i in range(len(g) - 1):  # 遍历|V|-1次
        dd = {key: value for (key, value) in d.items()}  # 备份上一轮的d
        for u in g:
            for v in g[u]:  # 内部的二重for循环遍历所有边
                d[v] = min(d[v], dd[u] + g[u][v])  # 松弛
        print(i+1, d)
    return d


def bellman_ford(g, s):
    d = dict()
    for v in g:  # 距离初始化为无穷大 前驱初始化为空
        d[v] = float("inf")
    d[s] = 0  # 源点到自己的最短路径长度为零
    print(0, d)
    for i in range(len(g) - 1):  # 遍历|V|-1次
        for u in g:
            for v in g[u]:  # 内部的二重for循环遍历所有边
                d[v] = min(d[v], d[u] + g[u][v])  # 松弛
        print(i+1, d)
    return d


g = {  # 顺序遍历所有点 s -> x -> y -> z -> t
    "s": {"x": 1},  # w(s,x) = 1
    "x": {"y": 1},  # w(x,y) = 1
    "y": {"z": 1},  # w(y,z) = 1
    "z": {"t": 1},  # w(z,t) = 1
    "t": {}
}

print("顺序 使用上一轮的d")
d = bellman_ford_dp(g, s="s")
# ---------------------------------------------------
# 顺序 使用上一轮的d
# 0 {'s': 0, 'x': inf, 'y': inf, 'z': inf, 't': inf}
# 1 {'s': 0, 'x': 1, 'y': inf, 'z': inf, 't': inf}
# 2 {'s': 0, 'x': 1, 'y': 2, 'z': inf, 't': inf}
# 3 {'s': 0, 'x': 1, 'y': 2, 'z': 3, 't': inf}
# 4 {'s': 0, 'x': 1, 'y': 2, 'z': 3, 't': 4}

print("顺序 使用即时的d")
d = bellman_ford(g, s="s")
# ---------------------------------------------------
# 顺序 使用即时的d
# 0 {'s': 0, 'x': inf, 'y': inf, 'z': inf, 't': inf}
# 1 {'s': 0, 'x': 1, 'y': 2, 'z': 3, 't': 4}
# 2 {'s': 0, 'x': 1, 'y': 2, 'z': 3, 't': 4}
# 3 {'s': 0, 'x': 1, 'y': 2, 'z': 3, 't': 4}
# 4 {'s': 0, 'x': 1, 'y': 2, 'z': 3, 't': 4}

g = {  # 逆序遍历所有点 t -> z -> y -> x -> s
    "t": {},
    "z": {"t": 1},  # w(z,t) = 1
    "y": {"z": 1},  # w(y,z) = 1
    "x": {"y": 1},  # w(x,y) = 1
    "s": {"x": 1},  # w(s,x) = 1
}

print("逆序 使用上一轮的d")
d = bellman_ford_dp(g, s="s")
# ---------------------------------------------------
# 逆序 使用上一轮的d
# 0 {'t': inf, 'z': inf, 'y': inf, 'x': inf, 's': 0}
# 1 {'t': inf, 'z': inf, 'y': inf, 'x': 1, 's': 0}
# 2 {'t': inf, 'z': inf, 'y': 2, 'x': 1, 's': 0}
# 3 {'t': inf, 'z': 3, 'y': 2, 'x': 1, 's': 0}
# 4 {'t': 4, 'z': 3, 'y': 2, 'x': 1, 's': 0}

print("逆序 使用即时的d")
d = bellman_ford(g, s="s")
# ---------------------------------------------------
# 逆序 使用即时的d
# 0 {'t': inf, 'z': inf, 'y': inf, 'x': inf, 's': 0}
# 1 {'t': inf, 'z': inf, 'y': inf, 'x': 1, 's': 0}
# 2 {'t': inf, 'z': inf, 'y': 2, 'x': 1, 's': 0}
# 3 {'t': inf, 'z': 3, 'y': 2, 'x': 1, 's': 0}
# 4 {'t': 4, 'z': 3, 'y': 2, 'x': 1, 's': 0}
