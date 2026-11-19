def subset_sum_dp(w: list[int], M: int) -> list[list[bool]]:
    n = len(w)
    ss: list[list[bool]] = [[False] * (M + 1) for _ in range(n)]
    for i in range(n):
        ss[i][0] = True  # 第0列全为真
    if w[-1] <= M:
        ss[-1][w[-1]] = True  # 填最后一行
    for i in range(n - 2, 0, -1):  # 倒数第二行 -> 第一行
        for m in range(1, M + 1):  # 每行 左 -> 右
            if m < w[i]:  # 如果目标和小于w[i] 只产生一个子问题
                ss[i][m] = ss[i + 1][m]
            else:
                ss[i][m] = ss[i + 1][m] or ss[i + 1][m - w[i]]
    return ss


w, M = [0, 5, 10, 12, 13, 15, 18], 30
ss = subset_sum_dp(w, M)
print(ss[1][M])
# ------------------------------------------
# True


def restore_sol_stack(ss: list[list[bool]], w: list[int], M: int) -> list[list[int]]:
    n = len(w)
    sol: list[list[int]] = []
    stack = [(1, M, [])]
    while stack:
        i, m, subset = stack.pop()
        if m == w[i]:  # 如果当前目标和等于w[i] 则找到一个解
            sol.append(subset + [i])
            continue
        if i == n-1:
            continue
        if ss[i+1][m]:  # 不选w[i]
            stack.append((i+1, m, subset))
        if ss[i+1][m - w[i]]:  # 选w[i]
            stack.append((i+1, m - w[i], subset + [i]))
    return sol


sol = restore_sol_stack(ss, w, M)
for subset in sol:
    print(" + ".join([str(w[i]) for i in subset]) + f" = {M}")
# ------------------------------------------
# 5 + 10 + 15 = 30
# 5 + 12 + 13 = 30
# 12 + 18 = 30


def restore_sol_rec(ss: list[list[bool]], w: list[int], M: int) -> list[list[int]]:
    sol: list[list[int]] = []

    def _restore_subsets_rec(i: int, m: int, subset: list[int]) -> None:
        if w[i] == m:  # 如果当前目标和等于w[i] 则找到一个解
            sol.append(subset + [i])
        else:
            if ss[i + 1][m - w[i]]:  # 选w[i]
                subset.append(i)     # 入栈
                _restore_subsets_rec(i + 1, m - w[i], subset)
                subset.pop()  # 出栈
            if ss[i + 1][m]:  # 不选w[i]
                _restore_subsets_rec(i + 1, m, subset)

    _restore_subsets_rec(1, M, [])
    return sol


sol = restore_sol_rec(ss, w, M)
for subset in sol:
    print(" + ".join([str(w[i]) for i in subset]) + f" = {M}")
# ------------------------------------------
# 5 + 10 + 15 = 30
# 5 + 12 + 13 = 30
# 12 + 18 = 30
