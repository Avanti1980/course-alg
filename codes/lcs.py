import numpy as np


def restore_lcs(b, x, i, j, lcs):
    if i == -1 or j == -1:
        return
    if b[i][j] == '↖':
        restore_lcs(b, x, i-1, j-1, lcs)
        lcs.append(x[i])
    elif b[i][j] == '↑':
        restore_lcs(b, x, i-1, j, lcs)
    else:
        restore_lcs(b, x, i, j-1, lcs)


X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
Y = ['B', 'D', 'C', 'A', 'B', 'A']
m, n = len(X), len(Y)
b = [[0 for i in range(m)] for j in range(n)]
c = [[0 for i in range(m+1)] for j in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if X[i-1] == Y[j-1]:           # 如果当前两个子串的最后一个字符相同
            c[i][j] = c[i-1][j-1] + 1
            b[i-1][j-1] = '↖'
        elif c[i-1][j] >= c[i][j-1]:
            c[i][j] = c[i-1][j]
            b[i-1][j-1] = '↑'
        else:
            c[i][j] = c[i][j-1]
            b[i-1][j-1] = '←'

lcs = []
restore_lcs(b, X, n-1, n-1, lcs)
print('LCS: %s' % lcs)
print(c)
print(b)
