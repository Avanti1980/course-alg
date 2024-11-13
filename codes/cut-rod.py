from math import ceil  # 向上取整


def cut_rod_rec(n, p):  # 分治 单子问题
    if n == 1:
        return p[1]
    else:
        v = p[n]
        for i in range(1, n):
            v = max(v, p[i] + cut_rod_rec(n-i, p))
    return v


def cut_rod_rec2(n, p):  # 分治 双子问题
    if n == 1:
        return p[1]
    else:
        v = p[n]
        for i in range(1, ceil(n/2)):
            v = max(v, cut_rod_rec2(i, p) + cut_rod_rec2(n-i, p))
    return v


def cut_rod_dp_memoized(n, p):
    r = [-float("inf")] * len(p)  # 备忘录初始化为负无穷
    return cut_rod_dp_memoized_aux(n, r, p)


def cut_rod_dp_memoized_aux(n, r, p):
    if r[n] >= 0:  # 查备忘录 若之前已计算过就直接用
        return r[n]
    if n == 0:
        v = 0
    else:
        v = -float("inf")
        for i in range(1, min(n+1, len(p))):
            v = max(v, p[i] + cut_rod_dp_memoized_aux(n-i, r, p))
    r[n] = v  # 保存当前计算的结果
    return v


def cut_rod_dp_bottom_up(n, p):
    r = [0] * len(p)
    for j in range(1, n+1):  # 依次求解 r[1], r[2], ...
        v = -float("inf")
        for i in range(1, j+1):  # 求解 r[j] 时 遍历 i = 1, 2, ..., j
            v = max(v, p[i] + r[j-i])  # 此时 r[1], r[2], ..., r[j-1] 均已求好
        r[j] = v
    return r[n]


def cut_rod_dp_bottom_up_print_sol(n, p):
    r = [0] * len(p)
    s = [0] * len(p)  # s[i]是长度为i的钢条的第一刀最优切割位置
    for j in range(1, n+1):
        v = -float("inf")
        for i in range(1, j+1):
            if v < p[i] + r[j-i]:
                v = p[i] + r[j-i]
                s[j] = i  # 更新最优切割位置
        r[j] = v
    while n > 0:  # 打印最优切割方案
        print(s[n], end=' ')
        n = n - s[n]


p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]   # 价格表
n = 7
print(cut_rod_rec(n, p))
print(cut_rod_rec2(n, p))
print(cut_rod_dp_memoized(n, p))
print(cut_rod_dp_bottom_up(n, p))
cut_rod_dp_bottom_up_print_sol(n, p)
