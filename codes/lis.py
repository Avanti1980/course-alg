from bisect import bisect_left

import numpy as np

np.random.seed(0)


def lis_dp(X, n):
    d = [1 for i in range(n)]
    b = [-1 for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            if X[j] < X[i] and d[i] < d[j] + 1:
                d[i] = d[j] + 1
                b[i] = j
    return d, b


def restore_lis(b, index, LIS):
    if index == -1:
        return
    restore_lis(b, b[index], LIS)
    LIS.append(X[index])


def lis_greedy(X, n):
    e = []
    b = -1 * np.ones(n, dtype=np.int32)
    for i in range(n):
        j = bisect_left(e, X[i])
        if j == len(e):
            if j > 0:
                b[i] = e[-1]
            e.append(X[i])
        else:
            e[j] = X[i]
            b[i] = e[j-1]
    return e, b


n = 10
X = np.random.permutation(n)
print('X =', X)

d, b = lis_dp(X, n)
print('d: %s' % d)
print('b: %s' % b)

LIS = []
restore_lis(b, np.argmax(d), LIS)
print('LIS =', LIS)

e, b = lis_greedy(X, n)
print('e: %s' % e)
print('b: %s' % b)
LIS = []
restore_lis(b, e, LIS)
print('LIS =', LIS)
