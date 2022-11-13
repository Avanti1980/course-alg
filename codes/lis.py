import random

random.seed(0)


def lis(X):
    n = len(X)
    d = [1 for i in range(n)]
    b = [-1 for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            if X[j] < X[i] and d[i] < d[j] + 1:
                d[i] = d[j] + 1
                b[i] = j
    return d, b


def restore_lis(b, index):
    if index == -1:
        return
    restore_lis(b, b[index])
    LIS.append(X[index])


n = 10
X = [i for i in range(n)]
random.shuffle(X)
d, b = lis(X)

print('d: %s' % d)
print('b: %s' % b)

LIS = []
restore_lis(b, d.index(max(d)))
print('X =', X)
print('LIS =', LIS)
