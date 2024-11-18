import numpy as np


def edit_dis(X, Y):
    m, n = len(X), len(Y)
    c, b = np.empty((m + 1, n + 1)), np.empty((m, n), dtype='str')
    for i in range(m + 1):
        c[i, 0] = i
    for j in range(n + 1):
        c[0, j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            a = [c[i - 1, j - 1] + int(X[i - 1] != Y[j - 1]), c[i, j - 1] + 1, c[i - 1, j] + 1]
            index = np.argmin(a)
            c[i, j] = a[index]
            if index == 0:
                b[i - 1, j - 1] = '↖'
            elif index == 1:
                b[i - 1, j - 1] = '←'
            else:
                b[i - 1, j - 1] = '↑'
    return c.astype(int), b


def restore_sol(i, j, b, l):
    if i == -1:
        for k in range(j + 1):
            l.append([' ', Y[j]])
        return
    if j == -1:
        for k in range(i + 1):
            l.append([X[i], ' '])
        return
    if b[i, j] == '↖':
        restore_sol(i - 1, j - 1, b, l)
        l.append([X[i], Y[j]])
    elif b[i, j] == '↑':
        restore_sol(i - 1, j, b, l)
        l.append([X[i], ' '])
    else:
        restore_sol(i, j - 1, b, l)
        l.append([' ', Y[j]])


X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
Y = ['B', 'D', 'C', 'A', 'B', 'A']
c, b = edit_dis(X, Y)
l = []
restore_sol(len(X) - 1, len(Y) - 1, b, l)
l = np.array(l).T

print(c)
print(b)
print(c[len(X) - 1, len(Y) - 1])
print(l)
----------------------------------------
[[0 1 2 3 4 5 6]
 [1 1 2 3 3 4 5]
 [2 1 2 3 4 3 4]
 [3 2 2 2 3 4 4]
 [4 3 3 3 3 3 4]
 [5 4 3 4 4 4 4]
 [6 5 4 4 4 5 4]
 [7 6 5 5 5 4 5]]
[['↖' '↖' '↖' '↖' '←' '↖']
 ['↖' '↖' '↖' '↖' '↖' '←']
 ['↑' '↖' '↖' '←' '←' '↖']
 ['↖' '↖' '↖' '↖' '↖' '←']
 ['↑' '↖' '↖' '↖' '↖' '↖']
 ['↑' '↑' '↖' '↖' '↖' '↖']
 ['↖' '↑' '↖' '↖' '↖' '←']]
5
[['A' 'B' 'C' 'B' 'D' 'A' 'B' ' ']
 [' ' 'B' ' ' 'D' 'C' 'A' 'B' 'A']]
