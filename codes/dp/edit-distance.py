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
            diag = c[i-1][j-1] + (0 if X[i-1] == Y[j-1] else 1)
            left = c[i][j-1] + 1
            up = c[i-1][j] + 1
            if diag <= left and diag <= up:
                c[i][j] = diag
                b[i][j] = '↖'
            elif left <= up:
                c[i][j] = left
                b[i][j] = '←'
            else:
                c[i][j] = up
                b[i][j] = '↑'
    return c, b


def restore_sol(i: int, j: int, b: list[list[str]], l: list[list[str]]):
    if i == 0:
        for _ in range(j):
            l.append([' ', Y[j-1]])
        return
    if j == 0:
        for _ in range(i):
            l.append([X[i-1], ' '])
        return
    if b[i][j] == '↖':
        restore_sol(i-1, j-1, b, l)
        l.append([X[i-1], Y[j-1]])
    elif b[i][j] == '↑':
        restore_sol(i-1, j, b, l)
        l.append([X[i-1], ' '])
    else:
        restore_sol(i, j-1, b, l)
        l.append([' ', Y[j-1]])


X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
Y = ['B', 'D', 'C', 'A', 'B', 'A']
c, b = edit_dis(X, Y)
l = []
restore_sol(len(X), len(Y), b, l)
l = [list(row) for row in zip(*l)]

print("***** c *****")
for row in c:
    print(*row)
print([row[1:] for row in b[1:]])
print(c[len(X)][len(Y)])
print(l[0])
print(l[1])
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
