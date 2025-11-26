def find(parent, node):  # 返回给定结点所在树的根结点
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]


def union(parent, size, node1, node2):
    root1 = find(parent, node1)
    root2 = find(parent, node2)

    if root1 != root2:  # 结点少的树作为结点多的树的子树
        if size[root1] >= size[root2]:
            parent[root2] = root1
            size[root1] += size[root2]
        else:
            parent[root1] = root2
            size[root2] += size[root1]


def kruskal(graph):
    min_spanning_tree = []

    # 保存图中所有边并排序
    edges = []
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            edges.append((weight, node, neighbor))
    edges.sort()

    # 父图初始化
    parent = {node: node for node in graph}
    size = {node: 1 for node in graph}

    # 遍历所有边 若为横跨切割的轻量边 合并两个端点所在的树
    for edge in edges:
        weight, node1, node2 = edge
        if find(parent, node1) != find(parent, node2):
            union(parent, size, node1, node2)
            min_spanning_tree.append((weight, f"{node1} - {node2}"))

    return min_spanning_tree


graph = {
    'a': {'b': 4, 'h': 8},
    'b': {'a': 4, 'c': 8, 'h': 11},
    'c': {'b': 8, 'd': 7, 'i': 2, 'f': 4},
    'd': {'c': 7, 'e': 9, 'f': 14},
    'e': {'d': 9, 'f': 10},
    'f': {'c': 4, 'd': 14, 'e': 10, 'g': 2},
    'g': {'f': 2, 'h': 1, 'i': 6},
    'h': {'a': 8, 'b': 11, 'g': 1, 'i': 7},
    'i': {'c': 2, 'g': 6, 'h': 7}
}

mst_weight = 0
for edge in kruskal(graph):
    mst_weight += edge[0]
    print(edge)
print(f"最小生成树权重和为{mst_weight}")
# -------------------------------------------
# (1, 'g - h')
# (2, 'c - i')
# (2, 'f - g')
# (4, 'a - b')
# (4, 'c - f')
# (7, 'c - d')
# (8, 'a - h')
# (9, 'd - e')
# 最小生成树权重和为37
