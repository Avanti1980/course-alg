def dfs(g, u):
    if u not in visited:
        visited.append(u)
        for v in g[u]:
            dfs(g, v)
        label.append(u)  # 后序DFS可以保得到结点的逆拓扑序


g = {
    "s": {"a": 3, "b": 8, "c": 7},
    "a": {"b": 6, "d": 12},
    "b": {"c": -2, "d": 5, "e": 0},
    "c": {"e": 10},
    "d": {"e": 1, "f": -3},
    "e": {"f": 1},
    "f": {}
}
visited, label = [], []
dfs(g, "s")
label.reverse()  # 反转得到拓扑序
print(label)
# -------------------------------------------
# ['s', 'a', 'b', 'd', 'c', 'e', 'f']

gg = {}  # g记录每个点的出边 gg记录每个点的入边
for u in g:
    gg[u] = {}
for u in g:
    for v in g[u]:
        gg[v][u] = g[u][v]

dist, pred = {"s": 0}, {"s": None}
for v in label:  # 按拓扑序遍历求最短路径
    if v != "s":
        dist[v] = float("inf")
        for u in gg[v]:
            if dist[v] > dist[u] + gg[v][u]:
                dist[v] = dist[u] + gg[v][u]
                pred[v] = u
print(dist)
print(pred)
# ----------------------------------------------------------------------
# {'s': 0, 'a': 3, 'b': 8, 'd': 13, 'c': 6, 'e': 8, 'f': 9}
# {'s': None, 'a': 's', 'b': 's', 'd': 'b', 'c': 'b', 'e': 'b', 'f': 'e'}
