import numpy as np


def lcs(X, Y):
    m, n = len(X), len(Y)
    c, b = np.zeros((m + 1, n + 1), dtype=int), np.empty((m, n), dtype=str)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:  # 如果当前两个子串的最后一个字符相同
                c[i, j] = c[i - 1, j - 1] + 1
                b[i - 1, j - 1] = "↖"
            elif c[i - 1, j] >= c[i, j - 1]:
                c[i, j] = c[i - 1, j]
                b[i - 1, j - 1] = "↑"
            else:
                c[i, j] = c[i, j - 1]
                b[i - 1, j - 1] = "←"
    return c, b


def restore_lcs(i, j, LCS):
    if i == -1 or j == -1:
        return
    if b[i, j] == "↖":
        restore_lcs(i - 1, j - 1, LCS)
        LCS.append(X[i])
    elif b[i, j] == "↑":
        restore_lcs(i - 1, j, LCS)
    else:
        restore_lcs(i, j - 1, LCS)


X = ["A", "B", "C", "B", "D", "A", "B"]
Y = ["B", "D", "C", "A", "B", "A"]
c, b = lcs(X, Y)
print(c)
print(b)

LCS = []
restore_lcs(len(X) - 1, len(Y) - 1, LCS)
print(LCS)
# -----------------------------------
# [[0 0 0 0 0 0 0]
#  [0 0 0 0 1 1 1]
#  [0 1 1 1 1 2 2]
#  [0 1 1 2 2 2 2]
#  [0 1 1 2 2 3 3]
#  [0 1 2 2 2 3 3]
#  [0 1 2 2 3 3 4]
#  [0 1 2 2 3 4 4]]
# [['↑' '↑' '↑' '↖' '←' '↖']
#  ['↖' '←' '←' '↑' '↖' '←']
#  ['↑' '↑' '↖' '←' '↑' '↑']
#  ['↖' '↑' '↑' '↑' '↖' '←']
#  ['↑' '↖' '↑' '↑' '↑' '↑']
#  ['↑' '↑' '↑' '↖' '↑' '↖']
#  ['↖' '↑' '↑' '↑' '↖' '↑']]
# ['B', 'C', 'B', 'A']