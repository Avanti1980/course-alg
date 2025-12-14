def bfs(g, s):
    visted = [s]  # 初始化已访问列表
    q = [s]  # 源点入队
    while q:  # 当队列非空时
        u = q.pop(0)  # 队首元素出队
        for v in g[u]:  # 对每条边(u,v)
            if v not in visted:
                visted.append(v)
                q.append(v)  # 点v入队
    return visted


def init_sssp(g, s):
    dist, pred = dict(), dict()
    for v in g:
        dist[v] = float("inf") if v != s else 0
        pred[v] = None
    return dist, pred


def bfs_sssp(g, s):
    dist, pred = init_sssp(g, s)  # 初始化距离和前驱
    q = [s]  # 源点入队
    while q:  # 当队列非空时
        u = q.pop(0)  # 队首元素出队
        for v in g[u]:  # 对每条边(u,v)
            if dist[v] > dist[u] + 1:  # 若可以松弛
                dist[v] = dist[u] + 1  # 更新距离
                pred[v] = u  # 更新前驱
                q.append(v)  # 点v入队
    return dist, pred


g = {
    "s": ["a", "b"],            #    a     e
    "a": ["s", "c"],            #   / \   /|
    "b": ["s", "c", "d"],       #  /   \ / |
    "c": ["a", "b", "d", "e"],  # s     c  |
    "d": ["b", "c", "e"],       #  \   / \ |
    "e": ["c", "d"],            #   \ /   \|
}                               #    b-----d

visited = bfs(g, "s")
print(visited)
# --------------------------------------------
# ['s', 'a', 'b', 'c', 'd', 'e']

dist, pred = bfs_sssp(g, "s")
print(dist)
print(pred)
# --------------------------------------------
# {'s': 0, 'a': 1, 'b': 1, 'c': 2, 'd': 2, 'e': 3}
# {'s': None, 'a': 's', 'b': 's', 'c': 'a', 'd': 'b', 'e': 'c'}
