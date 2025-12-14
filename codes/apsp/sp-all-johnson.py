def bellman_ford(s):
    d = dict()
    for v in g:  # 距离初始化为无穷大 前驱初始化为空
        d[v] = float("inf")
    d[s] = 0  # 源点到自己的最短路径长度为零

    for _ in range(len(g) - 1):  # 遍历|V|-1次
        for u in g:
            for v in g[u]:  # 内部的二重for循环遍历所有边
                d[v] = min(d[v], d[u] + g[u][v])  # 松弛

    for u in g:
        for v in g[u]:
            assert (d[v] <= d[u] + g[u][v]), "有负环"

    return d


def dijkstra(s):
    d, in_S = dict(), dict()
    for v in g:  # 距离初始化为无穷大 前驱初始化为空 S为空集
        d[v], in_S[v] = float("inf"), False
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
                d[v] = min(d[v], d[u] + g[u][v])  # 松弛

    return d


g = {
    "1": {"2": 3, "3": 8, "5": -4},  # w(1,2) = 3, w(1,3) = 8, w(1,5) = -4
    "2": {"4": 1, "5": 7},           # w(2,4) = 1, w(2,5) = 7
    "3": {"2": 4},                   # w(3,2) = 4
    "4": {"1": 2, "3": -5},          # w(4,1) = 2, w(4,3) = -5
    "5": {"4": 6},                   # w(5,4) = 6
}
g["0"] = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0}  # 添加新结点0
h = bellman_ford(s="0")  # 以0为源点运行Bellman-Ford算法

for u in g:
    for v in g[u]:
        g[u][v] += h[u] - h[v]  # 根据h重新给边赋权

D = dict()
for u in g:
    if u != "0":
        D[u] = dijkstra(u)  # 以每个结点为源点运行Dijkstra算法
        del D[u]["0"]

del g["0"]

for u in g:
    for v in g:
        D[u][v] += h[v] - h[u]  # 还原原权重下的最短路径长度

print(D)
------------------------------
'1': {'1': 0, '2': 1,  '3': -3, '4': 2, '5': -4}
'2': {'1': 3, '2': 0,  '3': -4, '4': 1, '5': -1}
'3': {'1': 7, '2': 4,  '3': 0,  '4': 5, '5': 3 }
'4': {'1': 2, '2': -1, '3': -5, '4': 0, '5': -2}
'5': {'1': 8, '2': 5,  '3': 1,  '4': 6, '5': 0 }