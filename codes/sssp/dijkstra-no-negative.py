# python自带的二叉堆库heapq不支持decrease-key操作
# 采用第三方库heapdict https://pypi.org/project/HeapDict/
import heapdict


def init_sssp(g, s):
    dist, pred = dict(), dict()
    for v in g:
        dist[v] = float("inf") if v != s else 0
        pred[v] = None
    return dist, pred


def dijkstra_no_negative(g, s):
    dist, pred = init_sssp(g, s)  # 初始化距离和前驱
    h, in_S = heapdict.heapdict(), dict()
    for v in g:
        h[v] = float("inf") if v != s else 0
        in_S[v] = False

    iter = 0
    while h:
        iter += 1
        print(f"第{iter}轮")
        u, d = h.popitem()  # 弹出最小元
        dist[u] = d  # 此时u的值已经是最短路径
        in_S[u] = True
        print(f"({u},{d})出堆，{s}到{u}的最短路径长度确定为{d}")
        for v in g[u]:  # 遍历u的所有出边(u,v)
            if not in_S[v] and h[v] > dist[u] + g[u][v]:
                print(f"放松边({u}->{v})，{s}到{v}的最短路径：{h[v]} => {dist[u] + g[u][v]}")
                h[v] = d + g[u][v]
                pred[v] = u
        print()
    return dist, pred


g = {
    "s": {"t": 10, "y": 5},  # w(s,t) = 6, w(s,y) = 5
    "t": {"x": 1, "y": 2},  # w(t,x) = 1, w(t,y) = 2
    "y": {"t": 3, "z": 2, "x": 9},  # w(y,t) = 3, w(y,z) = 2, w(y,x) = 9
    "z": {"s": 7, "x": 6},  # w(z,s) = 7, w(z,x) = 6
    "x": {"z": 4},  # w(x,z) = 4
}

dist, pred = dijkstra_no_negative(g, "s")
print(dist)
print(pred)
# --------------------------------------
# 第1轮
# (s,0)出堆，s到s的最短路径长度确定为0
# 放松边(s->t)，s到t的最短路径：inf => 10
# 放松边(s->y)，s到y的最短路径：inf => 5
#
# 第2轮
# (y,5)出堆，s到y的最短路径长度确定为5
# 放松边(y->t)，s到t的最短路径：10 => 8
# 放松边(y->z)，s到z的最短路径：inf => 7
# 放松边(y->x)，s到x的最短路径：inf => 14
#
# 第3轮
# (z,7)出堆，s到z的最短路径长度确定为7
# 放松边(z->x)，s到x的最短路径：14 => 13
#
# 第4轮
# (t,8)出堆，s到t的最短路径长度确定为8
# 放松边(t->x)，s到x的最短路径：13 => 9
#
# 第5轮
# (x,9)出堆，s到x的最短路径长度确定为9
#
# {'s': 0, 't': 8, 'y': 5, 'z': 7, 'x': 9}
# {'s': None, 't': 'y', 'y': 's', 'z': 'y', 'x': 't'}

# dijkstra_no_negative处理带负边的图的会输出错误的结果
# 下图为Bellman-Ford例子中的图
g = {
    "s": {"t": 6, "y": 7},  # w(s,t) = 6, w(s,y) = 7
    "t": {"x": 5, "z": -4, "y": 8},  # w(t,x) = 5, w(t,z) = -4, w(t,y) = 8
    "y": {"z": 9, "x": -3},  # w(y,z) = 9, w(y,x) = -3
    "z": {"x": 7, "s": 2},  # w(z,x) = 7, w(z,s) = 2
    "x": {"t": -2},  # w(x,t) = -2
}

dist, pred = dijkstra_no_negative(g, "s")
print(dist)
print(pred)
# --------------------------------------
# 第1轮
# (s,0)出堆，s到s的最短路径长度确定为0
# 放松边(s->t)，s到t的最短路径：inf => 6
# 放松边(s->y)，s到y的最短路径：inf => 7
#
# 第2轮
# (t,6)出堆，s到t的最短路径长度确定为6
# 放松边(t->x)，s到x的最短路径：inf => 11
# 放松边(t->z)，s到z的最短路径：inf => 2
#
# 第3轮
# (z,2)出堆，s到z的最短路径长度确定为2
# 放松边(z->x)，s到x的最短路径：11 => 9
#
# 第4轮
# (y,7)出堆，s到y的最短路径长度确定为7
# 放松边(y->x)，s到x的最短路径：9 => 4
#
# 第5轮
# (x,4)出堆，s到x的最短路径长度确定为4
#
# {'s': 0, 't': 6, 'y': 7, 'z': 2, 'x': 4}
# {'s': None, 't': 's', 'y': 's', 'z': 't', 'x': 'y'}
