import numpy as np


def subset_sum_dp(w, M):
    n = len(w)
    ss = np.full((n, M + 1), False)
    ss[:, 0] = True  # 第0列全为真
    if w[-1] <= M:
        ss[-1, w[-1]] = True  # 填最后一行
    for i in range(n - 2, 0, -1):  # 倒数第二行 -> 第一行
        for m in range(1, M + 1):  # 每行 左 -> 右
            if m < w[i]:  # 如果目标和小于w[i] 只产生一个子问题
                ss[i, m] = ss[i + 1, m]
            else:
                ss[i, m] = ss[i + 1, m] or ss[i + 1, m - w[i]]
    return ss


def print_sol(ss, w, i, m, M, sol):
    if w[i] == m:  # 如果当前目标和等于w[i] 则找到一个解
        for j in sol:
            print("%d + " % j, end="")
        print("%d = %d" % (w[i], M))
    else:
        if ss[i + 1, m - w[i]]:  # 如果w[i]是加数之一
            sol.append(w[i])  # 入栈
            print_sol(ss, w, i + 1, m - w[i], M, sol)
            sol.pop()  # 出栈
        if ss[i + 1, m]:
            print_sol(ss, w, i + 1, m, M, sol)


w, M = [0, 5, 10, 12, 13, 15, 18], 30
ss = subset_sum_dp(w, M)
print(ss[1, M])
print_sol(ss, w, 1, M, M, sol=[])
# ------------------------------------------
# True
# 5 + 10 + 15 = 30
# 5 + 12 + 13 = 30
# 12 + 18 = 30
