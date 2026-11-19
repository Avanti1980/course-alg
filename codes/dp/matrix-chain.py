INF = float("inf")


def matrix_chain(p: list[int]) -> tuple[list[list[int]], list[list[int]]]:
    n = len(p) - 1  # 矩阵个数
    m: list[list[int]] = [[0] * n for _ in range(n)]
    s: list[list[int]] = [[0] * n for _ in range(n)]
    for l in range(2, n + 1):           # 子问题长度 l = 2 -> n
        for i in range(0, n - l + 1):   # 从第i个矩阵开始
            j = i + l - 1               # 到第j个矩阵结束
            m[i][j] = INF               # 初始化为无穷大
            for k in range(i, j):       # 遍历最优分开位置
                cost = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k + 1
    return m, s


p = [30, 35, 15, 5, 10, 20, 25]
m, s = matrix_chain(p)
print(m[0][len(p) - 2])
print("**************** m ****************")
for row in m:
    print(*[f"{item:>5}" for item in row])
print("*** s ***")
for row in s[:-1]:
    print(*[f"{item:>1}" for item in row[1:]])
# ------------------------------------------
# 15125
# **************** m ****************
#     0 15750  7875  9375 11875 15125
#     0     0  2625  4375  7125 10500
#     0     0     0   750  2500  5375
#     0     0     0     0  1000  3500
#     0     0     0     0     0  5000
#     0     0     0     0     0     0
# *** s ***
# 1 1 3 3 3
# 0 2 3 3 3
# 0 0 3 3 3
# 0 0 0 4 5
# 0 0 0 0 5


def restore_sol(s: list[list[int]]) -> str:
    sol: list[str] = []

    def _restore_sol(i: int, j: int) -> None:
        if i == j:
            sol.append(f"A{i + 1}")
        else:
            sol.append("(")
            _restore_sol(i, s[i][j] - 1)
            _restore_sol(s[i][j], j)
            sol.append(")")

    _restore_sol(0, len(s)-1)
    return "".join(sol)


print(restore_sol(s))
# ------------------------------------------
# ((A1(A2A3))((A4A5)A6))
