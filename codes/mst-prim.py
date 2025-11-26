from queue import PriorityQueue


def prim(graph, start):
    min_spanning_tree = []
    in_mst = {start}  # 已在mst中的结点
    q = PriorityQueue()
    for neighbor, weight in graph[start].items():
        q.put((weight, start, neighbor))  # 初始点相连的边入队

    while not q.empty():
        weight, node1, node2 = q.get()
        if node2 not in in_mst:  # 是横跨切割的轻量边
            in_mst.add(node2)
            min_spanning_tree.append((weight, f"{node1} - {node2}"))

            for node2_neighbor, weight in graph[node2].items():
                if node2_neighbor not in in_mst:  # node2相连的横跨切割的边
                    q.put((weight, node2, node2_neighbor))

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
for edge in prim(graph, 'a'):
    mst_weight += edge[0]
    print(edge)
print(f"最小生成树权重和为{mst_weight}")
# -------------------------------------------
# (4, 'a - b')
# (8, 'a - h')
# (1, 'h - g')
# (2, 'g - f')
# (4, 'f - c')
# (2, 'c - i')
# (7, 'c - d')
# (9, 'd - e')
# 最小生成树权重和为37
