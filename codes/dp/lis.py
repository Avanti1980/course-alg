from bisect import bisect_left

import numpy as np

# np.random.seed(0)


def lis_dp(X, n):
    d, b = [1] * n, [-1] * n
    for i in range(1, n):
        for j in range(i):
            if X[j] < X[i] and d[i] < d[j] + 1:  # X[i]可接在X[j]后面
                d[i] = d[j] + 1
                b[i] = j  # 更新前一个元素的索引
    return d, b


def restore_lis_dp(X, b, index, LIS):
    if index == -1:
        return
    restore_lis_dp(X, b, b[index], LIS)
    LIS.append(X[index])


def lis_dp_plus(X, n):
    e = []
    b = [-1] * n  # b[i]记录i在LIS中的前一个元素的值
    for i in range(n):
        j = bisect_left(e, X[i])  # 在e中对X[i]进行二分查找
        if j == len(e):  # X[i] > e[-1]
            if j > 0:
                b[i] = e[-1]
            e.append(X[i])  # 将其接在e后面表示找到了更长的递增子序列
        else:  # e[j-1] < X[i] < e[j]
            if j > 0:
                b[i] = e[j - 1]
            e[j] = X[i]  # 将e[j]改为X[i] 可以改进现有长度为j的递增子序列
    return e, b


def restore_lis_dp_plus(X, n, e, b):
    dict = {key: value for key, value in zip(X, range(n))}  # 倒排索引字典 X[i]: i
    pre = e[-1]  # e的最后一个元素是LIS的最后一个元素
    LIS = []
    restore_lis_dp_plus_aux(dict, b, pre, LIS)  # 从最后一个元素开始 向前将LIS构造出来
    return LIS


def restore_lis_dp_plus_aux(dict, b, pre, LIS):
    if pre < 0:
        return
    restore_lis_dp_plus_aux(dict, b, b[dict[pre]], LIS)
    LIS.append(pre)


n = 10
X = np.random.permutation(n)
print("X =", X)

d, b = lis_dp(X, n)
# print('d: %s' % d)
# print('b: %s' % b)

LIS = []
restore_lis_dp(X, b, np.argmax(d), LIS)
print("LIS =", LIS)

e, b = lis_dp_plus(X, n)
# print('e: %s' % e)
# print('b: %s' % b)

LIS = restore_lis_dp_plus(X, n, e, b)
print("LIS =", LIS)
