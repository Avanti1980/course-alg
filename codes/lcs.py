def restore_lcs(b, X, i, j):
    if i == -1 or j == -1:
        return
    if b[i][j] == '↖':
        restore_lcs(b, X, i-1, j-1)
        LCS.append(X[i])
    elif b[i][j] == '↑':
        restore_lcs(b, X, i-1, j)
    else:
        restore_lcs(b, X, i, j-1)


def lcs(X, Y):
    m, n = len(X), len(Y)
    b = [[0 for i in range(n)] for j in range(m)]
    c = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(1, m+1):
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
    return c, b


X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
Y = ['B', 'D', 'C', 'A', 'B', 'A']
c, b = lcs(X, Y)
LCS = []
restore_lcs(b, X, len(X)-1, len(Y)-1)
print(c)
print(b)
