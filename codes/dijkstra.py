def dijkstra(matrix, s):

    nodes = len(matrix)
    in_S = [False] * nodes
    d = [float('inf')] * nodes

    # 初始化，将起始节点的最短路径修改成0
    d[s] = 0

    # 将访问节点中未访问的个数作为循环值，其实也可以用个点长度代替。
    while in_S.count(False):
        min_value = float('inf')
        min_value_index = 999

        # 在最短路径节点中找到最小值，已经访问过的不在参与循环。
        # 得到最小值下标，每循环一次肯定有一个最小值
        for index in range(nodes):
            if not in_S[index] and d[index] < min_value:
                min_value = d[index]
                min_value_index = index

        # 将访问节点数组对应的值修改成True，标志其已经访问过了
        in_S[min_value_index] = True

        # 更新d数组。
        # 以B点为例：d[x] 起始点达到B点的距离，
        # d[min_value_index] + matrix[min_value_index][index] 是起始点经过某点达到B点的距离，比较两个值，取较小的那个。
        for index in range(nodes):
            d[index] = min(d[index], d[min_value_index] + matrix[min_value_index][index])

    return d


matrix = [
    [0, 10, float('inf'), 4, float('inf'), float('inf')],
    [10, 0, 8, 2, 6, float('inf')],
    [float('inf'), 8, 10, 15, 1, 5],
    [4, 2, 15, 0, 6, float('inf')],
    [float('inf'), 6, 1, 6, 0, 12],
    [float('inf'), float('inf'), 5, float('inf'), 12, 0]
]

result = dijkstra(matrix, 0)
print('起始节点到其他点距离：%s' % result)
