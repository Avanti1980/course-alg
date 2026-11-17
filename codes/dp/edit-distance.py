def edit_dis(X: list[str], Y: list[str]) -> tuple[list[list[int]], list[list[str]]]:
    m, n = len(X), len(Y)
    c: list[list[int]] = [[0] * (n+1) for _ in range(m+1)]
    b: list[list[str]] = [[None] * (n+1) for _ in range(m+1)]
    for i in range(m+1):
        c[i][0] = i
    for j in range(n+1):
        c[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            diag = c[i-1][j-1]
            if X[i-1] != Y[j-1]:
                diag += 1
            left = c[i][j-1] + 1
            up = c[i-1][j] + 1
            if diag <= left and diag <= up:
                c[i][j], b[i][j] = diag, '↖'
            elif left <= up:
                c[i][j], b[i][j] = left, '←'
            else:
                c[i][j], b[i][j] = up, '↑'
    return c, b


def restore_sol_iter(X: list, b: list[list[str]]) -> list:
    l = []
    i, j = len(b)-1, len(b[0])-1

    while i > 0 and j > 0:
        if b[i][j] == "↖":
            l.append([X[i-1], Y[j-1]])
            i -= 1
            j -= 1
        elif b[i][j] == "↑":
            l.append([X[i-1], ' '])
            i -= 1
        else:
            l.append([' ', Y[j-1]])
            j -= 1
    if i == 0:
        for _ in range(j):
            l.append([' ', Y[j-1]])
    if j == 0:
        for _ in range(i):
            l.append([X[i-1], ' '])

    l.reverse()
    return [list(row) for row in zip(*l)]


def restore_sol_rec(X: list, b: list[list[str]]) -> list:
    l = []
    m, n = len(b)-1, len(b[0])-1

    def _restore_sol_rec(i: int, j: int) -> None:
        if i == 0:
            for _ in range(j):
                l.append([' ', Y[j-1]])
            return
        if j == 0:
            for _ in range(i):
                l.append([X[i-1], ' '])
            return

        if b[i][j] == '↖':
            _restore_sol_rec(i-1, j-1)
            l.append([X[i-1], Y[j-1]])
        elif b[i][j] == '↑':
            _restore_sol_rec(i-1, j)
            l.append([X[i-1], ' '])
        else:
            _restore_sol_rec(i, j-1)
            l.append([' ', Y[j-1]])

    _restore_sol_rec(m, n)
    return [list(row) for row in zip(*l)]


X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
Y = ['B', 'D', 'C', 'A', 'B', 'A']
c, b = edit_dis(X, Y)

print(c[len(X)][len(Y)])
print("***** c *****")
for row in c:
    print(*row)
print("****** b *******")
for row in b[1:]:
    print(*[f"{item}" for item in row[1:]])

l = restore_sol_iter(X, b)
print(*l[0])
print(*l[1])
l = restore_sol_rec(X, b)
print(*l[0])
print(*l[1])
# ----------------------------------------
# [0 1 2 3 4 5 6]
# [1 1 2 3 3 4 5]
# [2 1 2 3 4 3 4]
# [3 2 2 2 3 4 4]
# [4 3 3 3 3 3 4]
# [5 4 3 4 4 4 4]
# [6 5 4 4 4 5 4]
# [7 6 5 5 5 4 5]
# ['↖' '↖' '↖' '↖' '←' '↖']
# ['↖' '↖' '↖' '↖' '↖' '←']
# ['↑' '↖' '↖' '←' '←' '↖']
# ['↖' '↖' '↖' '↖' '↖' '←']
# ['↑' '↖' '↖' '↖' '↖' '↖']
# ['↑' '↑' '↖' '↖' '↖' '↖']
# ['↖' '↑' '↖' '↖' '↖' '←']
# 5
# ['A', 'B', 'C', 'B', 'D', 'A', 'B', ' ']
# [' ', 'B', ' ', 'D', 'C', 'A', 'B', 'A']
