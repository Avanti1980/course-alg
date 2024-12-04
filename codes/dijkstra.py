from queue import PriorityQueue


def dijkstra(s):
    q, in_q, d, p = PriorityQueue(), dict(), dict(), dict()

    for v in g:  # 距离初始化为无穷大 前驱初始化为空
        in_q[v], d[v], p[v] = False, float("inf"), None

    in_q["s"], d["s"] = True, 0
    q.put([0, "s"])  # 源点入队

    while not q.empty():
        _, u = q.get()  # 获取队首元素点u
        in_q[u] = False  # 更新点u的在队状态
        for v in g[u]:  # 更新u指向的点的最短路径
            if d[v] > d[u] + g[u][v]:  # 边(u,v)可以松弛
                if in_q[v]:  # 如果点v已在队 让其出队
                    q.queue.remove([d[v], v])
                d[v], p[v] = d[u] + g[u][v], u  # 更新最短距离和前驱
                q.put([d[v], v])  # 点v入队
                in_q[v] = True

    return d, p


g = {
    "s": {"t": 10, "y": 5},  # w(s,t) = 6, w(s,y) = 5
    "t": {"x": 1, "y": 2},  # w(t,x) = 1, w(t,y) = 2
    "y": {"t": 3, "z": 2, "x": 9},  # w(y,t) = 3, w(y,z) = 2, w(y,x) = 9
    "z": {"s": 7, "x": 6},  # w(z,s) = 7, w(z,x) = 6
    "x": {"z": 4},  # w(x,z) = 4
}

d, p = dijkstra("s")
print(d)
print(p)
# ---------------------------------------------------
# {'s': 0, 't': 8, 'y': 5, 'z': 7, 'x': 9}
# {'s': None, 't': 'y', 'y': 's', 'z': 'y', 'x': 't'}

g = {  # dijkstra也是可以处理带负边的图的
    "s": {"t": 6, "y": 7},  # w(s,t) = 6, w(s,y) = 7
    "t": {"x": 5, "z": -4, "y": 8},  # w(t,x) = 5, w(t,z) = -4, w(t,y) = 8
    "y": {"z": 9, "x": -3},  # w(y,z) = 9, w(y,x) = -3
    "z": {"x": 7, "s": 2},  # w(z,x) = 7, w(z,s) = 2
    "x": {"t": -2},  # w(x,t) = -2
}

d, p = dijkstra("s")
print(d)
print(p)
# ---------------------------------------------------
# {'s': 0, 't': 2, 'y': 7, 'z': -2, 'x': 4}
# {'s': None, 't': 'x', 'y': 's', 'z': 't', 'x': 'y'}
