def dijkstra(s):
    d, p, in_S = dict(), dict(), dict()
    for v in g:  # 距离初始化为无穷大 前驱初始化为空 S为空集
        d[v], p[v], in_S[v] = float("inf"), None, False
    d[s] = 0  # 源点到自己的最短路径长度为零

    for _ in range(len(g)):
        min_value = float('inf')
        u = None

        # 遍历所有点 寻找不在S中且最短路径估计值最小的点 
        # 我们这儿就是用个无序的字典实现d[] 遍历找最小时间复杂度O(V)
        # d[]可以用二叉堆、斐波那契堆等数据结构实现 找最小的时间复杂度可以改进
        for v in g:  
            if not in_S[v] and d[v] < min_value:
                min_value = d[v]  
                u = v

        if u != None:
            in_S[u] = True  # 将u加入S
            for v in g[u]:  # 更新u指向的点的最短路径的估计值
                if d[v] > d[u] + g[u][v]:           # 松弛
                    d[v], p[v] = d[u] + g[u][v], u  # 更新当前最短距离和前驱

    return d, p, in_S


g = {
    "s": {"t": 10, "y": 5},         # w(s,t) = 6, w(s,y) = 5
    "t": {"x": 1, "y": 2},          # w(t,x) = 1, w(t,y) = 2
    "y": {"t": 3, "z": 2, "x": 9},  # w(y,t) = 3, w(y,z) = 2, w(y,x) = 9
    "z": {"s": 7, "x": 6},          # w(z,s) = 7, w(z,x) = 6
    "x": {"z": 4},                  # w(x,z) = 4
}

d, p, in_S = dijkstra("s")
print(d)
print(p)
# ---------------------------------------------------
# {'s': 0, 't': 8, 'y': 5, 'z': 7, 'x': 9}
# {'s': None, 't': 'y', 'y': 's', 'z': 'y', 'x': 't'}