from bisect import bisect_left

import numpy as np

# np.random.seed(1)


def lis_dp(X, n):
    d, b = [1] * n, [-1] * n
    for i in range(1, n):
        for j in range(i):
            if X[j] < X[i] and d[i] < d[j] + 1:  # i接在j后面可以得到更长的LIS
                d[i] = d[j] + 1
                b[i] = j  # 更新前一个元素的索引
    return d, b


def restore_lis_dp(X, b, index, LIS):
    if index == -1:
        return
    restore_lis_dp(X, b, b[index], LIS)
    LIS.append(X[index])


def lis_greedy(X, n):
    e = []
    b = [-1] * n  # b[i]记录i在LIS中的前一个元素的值
    for i in range(n):
        j = bisect_left(e, X[i])  # 在e中对X[i]进行二分查找
        if j == len(e):           # X[i] > e[-1] 将其接在e的最后可得更长的LIS
            e.append(X[i])
            if j > 0:
                b[i] = e[-1]
        else:                     # e[j-1] < X[i] < e[j]
            e[j] = X[i]           # 将e[j]改为X[i] 可以改进现有长度为j的LIS
            if j > 0:
                b[i] = e[j-1]
    return e, b


def restore_lis_greedy(X, e, b):
    dict = {key: value for key, value in zip(X, range(n))}  # 倒排索引字典 X[i]: i
    pre = e[-1]  # e的最后一个元素是LIS的最后一个元素
    m = len(e)   # e的长度就是LIS的长度
    LIS = []
    restore_lis_greedy_aux(dict, m, b, pre, LIS)  # 从最后一个元素开始 向前将LIS构造出来
    return LIS


def restore_lis_greedy_aux(dict, m, b, pre, LIS):
    if pre < 0:
        return
    restore_lis_greedy_aux(dict, m, b, b[dict[pre]], LIS)
    LIS.append(pre)


n = 10
X = np.random.permutation(n)
print('X =', X)

d, b = lis_dp(X, n)
# print('d: %s' % d)
# print('b: %s' % b)

LIS = []
restore_lis_dp(X, b, np.argmax(d), LIS)
print('LIS =', LIS)

e, b = lis_greedy(X, n)
# print('e: %s' % e)
# print('b: %s' % b)

LIS = restore_lis_greedy(X, e, b)
print('LIS =', LIS)
