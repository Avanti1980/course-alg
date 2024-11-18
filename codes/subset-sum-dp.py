import numpy as np


def subset_sum_dp(w, M):
    n = len(w)
    ss = np.zeros((n, M + 1), dtype='bool')
    ss[:, 0] = True                # 第0列全为真
    if w[-1] <= M:
        ss[-1, w[-1]] = True       # 填最后一行
    for i in range(n - 2, 0, -1):  # 从下往上填
        for m in range(1, M + 1):  # 每行从左往右填
            if m < w[i]:           # 如果目标和小于w[i]
                ss[i, m] = ss[i + 1, m]
            else:
                ss[i, m] = ss[i + 1, m] or ss[i + 1, m - w[i]]
    return ss


def print_sol(ss, w, i, m, M, list):
    if w[i] == m:  # 如果当前目标和等于w[i] 则找到一个解
        for j in list:
            print("%d + " % j, end='')
        print("%d = %d" % (w[i], M))
    else:
        if ss[i + 1, m - w[i]]:  # 如果w[i]是加数之一
            list.append(w[i])    # 入栈
            print_sol(ss, w, i + 1, m - w[i], M, list)
            list.pop()           # 出栈
        if ss[i + 1, m]:
            print_sol(ss, w, i + 1, m, M, list)


w, M = [0, 5, 10, 12, 13, 15, 18], 30
ss = subset_sum_dp(w, M)
print(ss[1, M])
print_sol(ss, w, 1, M, M, [])
------------------------------------------
True
5 + 10 + 15 = 30
5 + 12 + 13 = 30
12 + 18 = 30
