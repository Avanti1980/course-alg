# python自带的二叉堆库heapq不支持decrease-key操作
# 采用第三方库heapdict https://pypi.org/project/HeapDict/
import heapdict


def init_sssp(g, s):
    dist, pred = dict(), dict()
    for v in g:
        dist[v] = float("inf") if v != s else 0
        pred[v] = None
    return dist, pred


def dijkstra(g, s):
    dist, pred = init_sssp(g, s)  # 初始化距离和前驱
    h = heapdict.heapdict()
    h[s] = 0  # 将源点加入二叉堆

    # 有负边时堆首弹出的点的最短路径不一定正确 故无需集合S
    # 引入in_heap判断某个点是否在堆中
    in_heap = dict()
    for v in g:
        in_heap[v] = False if v != s else True

    iter = 0
    while h:
        iter += 1
        print(f"第{iter}轮")
        u, d = h.popitem()  # 弹出最小元
        print(f"({u},{d})出堆")
        in_heap[u] = False
        for v in g[u]:  # 遍历u的所有出边(u,v)
            if dist[v] > dist[u] + g[u][v]:  # 边(u,v)可以松弛
                print(f"放松边({u}->{v})，{s}到{v}的最短路径：{dist[v]} => {dist[u] + g[u][v]}")

                # 边(u,v)松弛后 v出发的边或许可以继续松弛 故v入堆
                if not in_heap[v]:
                    in_heap[v] = True
                    h[v] = dist[v] = dist[u] + g[u][v]
                    print(f"({v},{h[v]})入堆")
                else:
                    print(f"更新：({v},{h[v]}) => ({v},{dist[u] + g[u][v]})")
                    h[v] = dist[v] = dist[u] + g[u][v]
                pred[v] = u
        print()
    return dist, pred

# 下图为Bellman-Ford例子中的图 dijkstra_no_negative无法得到正确结果 dijkstra可以得到正确结果
g = {
    "s": {"t": 6, "y": 7},  # w(s,t) = 6, w(s,y) = 7
    "t": {"x": 5, "z": -4, "y": 8},  # w(t,x) = 5, w(t,z) = -4, w(t,y) = 8
    "y": {"z": 9, "x": -3},  # w(y,z) = 9, w(y,x) = -3
    "z": {"x": 7, "s": 2},  # w(z,x) = 7, w(z,s) = 2
    "x": {"t": -2},  # w(x,t) = -2
}

dist, pred = dijkstra(g, "s")
print(dist)
print(pred)
# --------------------------------------
# 第1轮
# (s,0)出堆
# 放松边(s->t)，s到t的最短路径：inf => 6
# (t,6)入堆
# 放松边(s->y)，s到y的最短路径：inf => 7
# (y,7)入堆
#
# 第2轮
# (t,6)出堆
# 放松边(t->x)，s到x的最短路径：inf => 11
# (x,11)入堆
# 放松边(t->z)，s到z的最短路径：inf => 2
# (z,2)入堆
#
# 第3轮
# (z,2)出堆
# 放松边(z->x)，s到x的最短路径：11 => 9
# 更新：(x,11) => (x,9)
#
# 第4轮
# (y,7)出堆
# 放松边(y->x)，s到x的最短路径：9 => 4
# 更新：(x,9) => (x,4)
#
# 第5轮
# (x,4)出堆
# 放松边(x->t)，s到t的最短路径：6 => 2
# (t,2)入堆
#
# 第6轮
# (t,2)出堆
# 放松边(t->z)，s到z的最短路径：2 => -2
# (z,-2)入堆
#
# 第7轮
# (z,-2)出堆
#
# {'s': 0, 't': 2, 'y': 7, 'z': -2, 'x': 4}
# {'s': None, 't': 'x', 'y': 's', 'z': 't', 'x': 'y'}
