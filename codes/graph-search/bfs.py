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


g = {
    "s": ["a", "b"],            #    a     e
    "a": ["s", "c"],            #   / \   /|
    "b": ["s", "c", "d"],       #  /   \ / |
    "c": ["a", "b", "d", "e"],  # s     c  |
    "d": ["b", "c", "e"],       #  \   / \ |
    "e": ["c", "d"],            #   \ /   \|
}                               #    b-----d

visted = bfs(g, "s")
print(visted)
# --------------------------------------------
# ['s', 'a', 'b', 'c', 'd', 'e']

visted = bfs(g, "c")
print(visted)
# --------------------------------------------
# ['c', 'a', 'b', 'd', 'e', 's']
