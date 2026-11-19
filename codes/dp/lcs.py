def lcs(X: list, Y: list) -> tuple[list[list[int]], list[list[str]]]:
    m, n = len(X), len(Y)
    c: list[list[int]] = [[0] * (n+1) for _ in range(m+1)]
    b: list[list[str]] = [[None] * (n+1) for _ in range(m+1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                c[i][j], b[i][j] = c[i - 1][j - 1] + 1, "↖"
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j], b[i][j] = c[i - 1][j], "↑"
            else:
                c[i][j], b[i][j] = c[i][j - 1], "←"
    return c, b


X = ["A", "B", "C", "B", "D", "A", "B"]
Y = ["B", "D", "C", "A", "B", "A"]
c, b = lcs(X, Y)

print(c[len(X)][len(Y)])
print("***** c *****")
for row in c:
    print(*row)
print("****** b ******")
for row in b[1:]:
    print(*[f"{item}" for item in row[1:]])
# -----------------------------------
# 4
# ***** c *****
# 0 0 0 0 0 0 0
# 0 0 0 0 1 1 1
# 0 1 1 1 1 2 2
# 0 1 1 2 2 2 2
# 0 1 1 2 2 3 3
# 0 1 2 2 2 3 3
# 0 1 2 2 3 3 4
# 0 1 2 2 3 4 4
# ****** b *******
# ↑ ↑ ↑ ↖ ← ↖
# ↖ ← ← ↑ ↖ ←
# ↑ ↑ ↖ ← ↑ ↑
# ↖ ↑ ↑ ↑ ↖ ←
# ↑ ↖ ↑ ↑ ↑ ↑
# ↑ ↑ ↑ ↖ ↑ ↖
# ↖ ↑ ↑ ↑ ↖ ↑


def restore_lcs_iter(X: list, b: list[list[str]]) -> list:
    LCS = []
    i, j = len(b)-1, len(b[0])-1

    while i > 0 and j > 0:
        if b[i][j] == "↖":
            LCS.append(X[i-1])
            i -= 1
            j -= 1
        elif b[i][j] == "↑":
            i -= 1
        else:
            j -= 1

    LCS.reverse()
    return LCS


print(*restore_lcs_iter(X, b))
# -----------------------------------
# B C B A


def restore_lcs_rec(X: list, b: list[list[str]]) -> list:
    LCS = []
    m, n = len(b)-1, len(b[0])-1

    def _restore_lcs_rec(i: int, j: int) -> None:
        if i == 0 or j == 0:
            return
        if b[i][j] == "↖":
            _restore_lcs_rec(i - 1, j - 1)
            LCS.append(X[i-1])
        elif b[i][j] == "↑":
            _restore_lcs_rec(i - 1, j)
        else:
            _restore_lcs_rec(i, j - 1)

    _restore_lcs_rec(m, n)
    return LCS


print(*restore_lcs_rec(X, b))
# -----------------------------------
# B C B A
