import itertools
import heapdict


def initialize_flow(c):  # 零初始化
    f = {}
    for u in c:
        f[u] = {}
    for u in c:
        for v in c[u]:
            f[u][v] = 0
    return f


def res_net(c, f):                             # 计算残存网络
    c_f = {}
    for u in c:
        c_f[u] = {}
    for u in c:
        for v in c[u]:
            if f[u][v] == c[u][v]:             # 满流量
                c_f[v][u] = c[u][v]
            elif f[u][v] == 0:                 # 无流量
                c_f[u][v] = c[u][v]
            else:
                c_f[u][v] = c[u][v] - f[u][v]  # 正向边容量等于剩余容量
                c_f[v][u] = f[u][v]            # 反向边容量等于当前流量
    return c_f


def dfs_rec(c_f, pre, visited, u):  # 深度优先 递归
    if u == "t":
        return
    for v in c_f[u].keys():         # 残存网络中 u -> v
        if v not in visited:
            visited.append(v)
            pre[v] = u
            dfs_rec(c_f, pre, visited, v)


def xxfs_iter(c_f, n):
    pre, visited, l = {}, ["s"], ["s"]  # 前驱表 访问标记 用于做搜索的数据结构
    while l:
        u = l.pop(n)                    # 弹出第n个元素
        for v in c_f[u].keys():         # 残存网络中 u -> v
            if v not in visited:
                visited.append(v)
                l.append(v)
                pre[v] = u
                if v == "t":
                    return pre
    return pre


def longest_path(c_f):  # 穷举检查 带环有向图中寻找最长简单路径是NP难的
    nodes = []          # 存储全部中间结点
    for u in c_f:
        if u != "s" and u != "t":
            nodes.append(u)
    pre = {}
    for i in range(len(nodes), 0, -1):
        combination = list(itertools.combinations(nodes, i))  # 按结点数从多到少遍历幂集
        for comb in combination:
            permutation = list(itertools.permutations(comb))  # 对于某个结点子集 生成全排列
            for perm in permutation:
                find_path = True
                if perm[0] not in c_f["s"].keys():   # 如果没有 s -> 第一个点
                    find_path = False
                if "t" not in c_f[perm[-1]].keys():  # 如果没有 最后一个点 -> t
                    find_path = False
                for j in range(1, len(perm)):
                    if perm[j] not in c_f[perm[j - 1]].keys():
                        find_path = False
                        break
                if find_path:
                    pre["t"] = perm[-1]
                    for j in range(len(perm) - 1, 0, -1):
                        pre[perm[j]] = perm[j - 1]
                    pre[perm[0]] = "s"
                    return pre
    return pre


def max_res_cap(c_f):    # 化用Dijkstra算法
    pre, bottleneck, in_S = dict(), dict(), dict()
    h = heapdict.heapdict()
    for v in c_f:
        h[v] = 0 if v != "s" else -float("inf")
        in_S[v] = False

    while h:
        u, d = h.popitem()  # 弹出最小元
        bottleneck[u] = -d  # 此时u的值已经是s到其的瓶颈边残存容量
        in_S[u] = True
        for v in c_f[u]:
            if not in_S[v] and h[v] > -min(bottleneck[u], c_f[u][v]):
                h[v] = -min(bottleneck[u], c_f[u][v])
                pre[v] = u

    return pre


def increase_flow(c_f, f, pre):
    v, path = "t", []
    while True:                      # 根据前驱表生成增广路径
        path.append((pre[v], v))
        v = pre[v]
        if v == "s":
            break
    path.reverse()
    print("增广路径:", path)

    res_cap_edge = []                # 存储增广路径上边的容量
    for u, v in path:
        res_cap_edge.append(c_f[u][v])
        res_cap = min(res_cap_edge)  # 确定残存容量
    print("残存容量:", res_cap)

    for u, v in path:
        if v in f[u].keys():
            f[u][v] += res_cap       # 正向边流量增大
        else:
            f[v][u] -= res_cap       # 反向边流量减小


def calculate_flow(f):
    value = 0
    for v in f["s"].keys():
        value += f["s"][v]
    return value


def ford_fulkerson(c, mode):

    f, i = initialize_flow(c), 1  # 初始化流值为零

    while True:
        print("第%d轮" % i)
        print("当前的流:", f)

        c_f = res_net(c, f)  # 计算残存网络
        print("残存网络:", c_f)

        match mode:
            case 1:  # 深度优先 递归
                pre = {}
                dfs_rec(c_f, pre, ["s"], "s")
            case 2:  # 深度优先 循环 栈
                pre = xxfs_iter(c_f, -1)
            case 3:  # 广度优先 循环 队列 or 最少边数
                pre = xxfs_iter(c_f, 0)
            case 4:  # 最多边数
                pre = longest_path(c_f)
            case 5:  # 最大残存容量
                pre = max_res_cap(c_f)
            case _:
                print("mode取值必须是{1,2,3,4,5}!")
                return

        if "t" not in pre.keys():   # 若汇点、源点已不再连通
            print("最大流值为%d" % calculate_flow(f))
            return
        else:
            increase_flow(c_f, f, pre)

        i += 1


c = {                           # 容量
    "s": {"v1": 16, "v2": 13},  # c(s,v1) = 16, c(s,v2) = 13        v1 -- v3
    "v1": {"v3": 12},           # c(v1,v3) = 12                   / |   / | \
    "v2": {"v1": 4, "v4": 14},  # c(v2,v1) = 4, c(v2,v4) = 14   s   |  /  |  t
    "v3": {"v2": 9, "t": 20},   # c(v3,v2) = 9, c(v3,t) = 20      \ | /   | /
    "v4": {"v3": 7, "t": 4},    # c(v4,v3) = 7, c(v4,t) = 4        v2 -- v4
    "t": {}
}
ford_fulkerson(c, mode=5)
# -----------------------------------------------------
# 第1轮
# 当前的流: {'s': {'v1': 0, 'v2': 0}, 'v1': {'v3': 0}, 'v2': {'v1': 0, 'v4': 0}, 'v3': {'v2': 0, 't': 0}, 'v4': {'v3': 0, 't': 0}, 't': {}}
# 残存网络: {'s': {'v1': 16, 'v2': 13}, 'v1': {'v3': 12}, 'v2': {'v1': 4, 'v4': 14}, 'v3': {'v2': 9, 't': 20}, 'v4': {'v3': 7, 't': 4}, 't': {}}
# 增广路径: [('s', 'v1'), ('v1', 'v3'), ('v3', 't')]
# 残存容量: 12
# 第2轮
# 当前的流: {'s': {'v1': 12, 'v2': 0}, 'v1': {'v3': 12}, 'v2': {'v1': 0, 'v4': 0}, 'v3': {'v2': 0, 't': 12}, 'v4': {'v3': 0, 't': 0}, 't': {}}
# 残存网络: {'s': {'v1': 4, 'v2': 13}, 'v1': {'s': 12}, 'v2': {'v1': 4, 'v4': 14}, 'v3': {'v1': 12, 'v2': 9, 't': 8}, 'v4': {'v3': 7, 't': 4}, 't': {'v3': 12}}
# 增广路径: [('s', 'v2'), ('v2', 'v4'), ('v4', 'v3'), ('v3', 't')]
# 残存容量: 7
# 第3轮
# 当前的流: {'s': {'v1': 12, 'v2': 7}, 'v1': {'v3': 12}, 'v2': {'v1': 0, 'v4': 7}, 'v3': {'v2': 0, 't': 19}, 'v4': {'v3': 7, 't': 0}, 't': {}}
# 残存网络: {'s': {'v1': 4, 'v2': 6}, 'v1': {'s': 12}, 'v2': {'s': 7, 'v1': 4, 'v4': 7}, 'v3': {'v1': 12, 'v2': 9, 't': 1, 'v4': 7}, 'v4': {'v2': 7, 't': 4}, 't': {'v3': 19}}
# 增广路径: [('s', 'v2'), ('v2', 'v4'), ('v4', 't')]
# 残存容量: 4
# 第4轮
# 当前的流: {'s': {'v1': 12, 'v2': 11}, 'v1': {'v3': 12}, 'v2': {'v1': 0, 'v4': 11}, 'v3': {'v2': 0, 't': 19}, 'v4': {'v3': 7, 't': 4}, 't': {}}
# 残存网络: {'s': {'v1': 4, 'v2': 2}, 'v1': {'s': 12}, 'v2': {'s': 11, 'v1': 4, 'v4': 3}, 'v3': {'v1': 12, 'v2': 9, 't': 1, 'v4': 7}, 'v4': {'v2': 11}, 't': {'v3': 19, 'v4': 4}}
# 最大流值为23

c = {                           # 容量                             v
    "s": {"u": 100, "v": 100},  # c(s,u) = 100, c(s,v) = 100    / | \
    "u": {"v": 1, "t": 100},    # c(u,v) = 1, c(u,t) = 100     s  |  t
    "v": {"t": 100},            # c(v,t) = 100                  \ | /
    "t": {}                     # #                               u
}
ford_fulkerson(c, mode=4)
# ------------------------------------
# 第1轮
# 当前的流: {'s': {'u': 0, 'v': 0}, 'u': {'v': 0, 't': 0}, 'v': {'t': 0}, 't': {}}
# 残存网络: {'s': {'u': 100, 'v': 100}, 'u': {'v': 1, 't': 100}, 'v': {'t': 100}, 't': {}}
# 增广路径: [('s', 'u'), ('u', 'v'), ('v', 't')]
# 残存容量: 1
# 第2轮
# 当前的流: {'s': {'u': 1, 'v': 0}, 'u': {'v': 1, 't': 0}, 'v': {'t': 1}, 't': {}}
# 残存网络: {'s': {'u': 99, 'v': 100}, 'u': {'s': 1, 't': 100}, 'v': {'u': 1, 't': 99}, 't': {'v': 1}}
# 增广路径: [('s', 'v'), ('v', 'u'), ('u', 't')]
# 残存容量: 1
# 第3轮
# 当前的流: {'s': {'u': 1, 'v': 1}, 'u': {'v': 0, 't': 1}, 'v': {'t': 1}, 't': {}}
# 残存网络: {'s': {'u': 99, 'v': 99}, 'u': {'s': 1, 'v': 1, 't': 99}, 'v': {'s': 1, 't': 99}, 't': {'u': 1, 'v': 1}}
# 增广路径: [('s', 'u'), ('u', 'v'), ('v', 't')]
# 残存容量: 1
# 第4轮
# 当前的流: {'s': {'u': 2, 'v': 1}, 'u': {'v': 1, 't': 1}, 'v': {'t': 2}, 't': {}}
# 残存网络: {'s': {'u': 98, 'v': 99}, 'u': {'s': 2, 't': 99}, 'v': {'s': 1, 'u': 1, 't': 98}, 't': {'u': 1, 'v': 2}}
# 增广路径: [('s', 'v'), ('v', 'u'), ('u', 't')]
# 残存容量: 1
# 第5轮
# 当前的流: {'s': {'u': 2, 'v': 2}, 'u': {'v': 0, 't': 2}, 'v': {'t': 2}, 't': {}}
# 残存网络: {'s': {'u': 98, 'v': 98}, 'u': {'s': 2, 'v': 1, 't': 98}, 'v': {'s': 2, 't': 98}, 't': {'u': 2, 'v': 2}}
# 增广路径: [('s', 'u'), ('u', 'v'), ('v', 't')]
# 残存容量: 1
# ...
# 第201轮
# 当前的流: {'s': {'u': 100, 'v': 100}, 'u': {'v': 0, 't': 100}, 'v': {'t': 100}, 't': {}}
# 残存网络: {'s': {}, 'u': {'s': 100, 'v': 1}, 'v': {'s': 100}, 't': {'u': 100, 'v': 100}}
# 最大流值为200

c = {                               # #         s
    "s": {"a": 1, "b": 1, "d": 1},  # #      ╱|  ╲
    "a": {"t": 1},                  # #   ╱  |     ╲
    "b": {"a": 1, "c": 1},          # # a -- b -- c -- d
    "c": {"t": 1},                  # #   ╲     /  ╱
    "d": {"c": 1, "t": 1},          # #     ╲ / ╱
    "t": {}                         # #       t
}
ford_fulkerson(c, mode=1)
