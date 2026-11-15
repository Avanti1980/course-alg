def lcs(X: list[str], Y: list[str]) -> tuple[list[list[int]], list[list[str]]]:
    m, n = len(X), len(Y)
    c: list[list[int]] = [[0] * (n+1) for _ in range(m+1)]
    b: list[list[str]] = [[None] * (n+1) for _ in range(m+1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "↖"
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = "↑"
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = "←"
    return c, b


def restore_lcs(i: int, j: int,
                LCS: list[str]) -> None:
    if i == 0 or j == 0:
        return
    if b[i][j] == "↖":
        restore_lcs(i - 1, j - 1, LCS)
        LCS.append(X[i-1])
    elif b[i][j] == "↑":
        restore_lcs(i - 1, j, LCS)
    else:
        restore_lcs(i, j - 1, LCS)


X = ["A", "B", "C", "B", "D", "A", "B"]
Y = ["B", "D", "C", "A", "B", "A"]
c, b = lcs(X, Y)
print(c)
print(b)

LCS = []
restore_lcs(len(X), len(Y), LCS)
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
