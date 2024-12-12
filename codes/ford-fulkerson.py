def dfs(graph, node, visited, pre):
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node].keys():
            dfs(graph, neighbor, visited, pre)
            pre[neighbor] = node

def augmenting_path(c):
    pre = dict()
    dfs(c, "s", [], pre)
    print(pre)
    
def ford_fulkerson(c, f):

    # 计算残存网络
    c_f = dict()
    for u in c:
        c_f[u] = dict()
    for u in c:
        for v in c[u]:
            if f[u][v] == c[u][v]:
                c_f[v][u] = c[u][v]
            elif f[u][v] == 0:
                c_f[u][v] = c[u][v]
            else:
                c_f[u][v] = c[u][v] - f[u][v]
                c_f[v][u] = f[u][v]

    print(c_f)

    augmenting_path(c_f)

c = {                            # 容量
    "s": {"v1": 16, "v2": 13},   # c(s,v1) = 16, c(s,v2) = 13
    "v1": {"v3": 12},            # c(v1,v3) = 12
    "v2": {"v1": 4, "v4": 14},   # c(v2,v1) = 4, c(v2,v4) = 14
    "v3": {"v2": 9, "t": 20},    # c(v3,v2) = 9, c(v3,t) = 20
    "v4": {"v3": 7, "t": 4},     # c(v4,v3) = 7, c(v4,t) = 4
    "t": {}
}

f = {
    "s": {"v1": 0, "v2": 0},
    "v1": {"v3": 0},
    "v2": {"v1": 0, "v4": 0},
    "v3": {"v2": 0, "t": 0},
    "v4": {"v3": 0, "t": 0},
}

f = {
    "s": {"v1": 4, "v2": 4},
    "v1": {"v3": 8},
    "v2": {"v1": 4, "v4": 4},
    "v3": {"v2": 4, "t": 4},
    "v4": {"v3": 0, "t": 4},
}

ford_fulkerson(c, f)





