NEG_INF = float("-inf")


def cut_rod_rec2(n: int, p: list[float]) -> float:
    if n <= 1:
        return p[n]

    best = p[n] if n < len(p) else NEG_INF
    for i in range(1, n // 2 + 1):  # i = 1, 2, ..., n//2
        best = max(best, cut_rod_rec2(i, p) + cut_rod_rec2(n - i, p))
    return best


def cut_rod_rec(n: int, p: list[float]) -> float:
    if n <= 1:
        return p[n]

    best = p[n] if n < len(p) else NEG_INF
    for i in range(1, min(n+1, len(p))):  # i = 1, 2, ...
        best = max(best, p[i] + cut_rod_rec(n - i, p))
    return best


def cut_rod_dp_memoized(n: int, p: list[float]) -> float:
    memo: list[float | None] = [None] * (n + 1)
    memo[0:2] = p[0:2]

    def solve(k: int) -> float:
        if memo[k] is not None:
            return memo[k]
        best = NEG_INF
        for i in range(1, min(k+1, len(p))):  # i = 1, 2, ...
            best = max(best, p[i] + solve(k - i))
        memo[k] = best
        return best

    return solve(n)


def cut_rod_dp_bottom_up(n: int, p: list[float]) -> float:
    r = [0] * (n+1)
    for j in range(1, n+1):  # 依次求解 r[1], r[2], ...
        best = NEG_INF
        for i in range(1, min(j+1, len(p))):  # 求解 r[j] 时遍历 i = 1, 2, ...
            best = max(best, p[i] + r[j-i])  # 此时 r[j-1], r[j-2], ... 均已求好
        r[j] = best
    return r[n]


def cut_rod_dp_with_solution(n: int, p: list[float]) -> tuple[float, list[int]]:
    r = [0] * (n + 1)
    s = [0] * (n + 1)  # s[i]是长度为i的钢条的第一刀最优切割位置
    for j in range(1, n + 1):
        best, best_i = NEG_INF, 0
        for i in range(1, min(j+1, len(p))):
            val = p[i] + r[j - i]
            if val > best:
                best, best_i = val, i
        r[j] = best
        s[j] = best_i

    solution, k = [], n
    while k > 0:  # 重构最优切割方案
        solution.append(s[k])
        k -= s[k]
    return r[n], solution


p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]   # 价格表
for n in range(20):
    print("***********", n, "***********")
    print(cut_rod_rec2(n, p))
    print(cut_rod_rec(n, p))
    print(cut_rod_dp_memoized(n, p))
    print(cut_rod_dp_bottom_up(n, p))
    print(cut_rod_dp_with_solution(n, p))
