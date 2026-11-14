def fibo_rec(n: int) -> int:
    if n <= 1:
        return n
    
    # 递归求解两个子问题
    return fibo_rec(n - 1) + fibo_rec(n - 2)


def fibo_dp_memoized(n: int) -> int:
    memo: list[int | None] = [None] * (n + 1)
    memo[0:2] = [0, 1]

    def solve(k: int) -> int:
        if memo[k] is not None:
            return memo[k]

        memo[k] = solve(k - 1) + solve(k - 2)
        return memo[k]

    return solve(n)


def fibo_dp_iter(n: int) -> int:
    if n <= 1:
        return n

    F = [0] * (n + 1)
    F[1] = 1
    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F[n]


def fibo_dp_iter2(n: int) -> int:
    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(n - 1):
        prev, curr = curr, prev + curr
    return curr


def fibo_rec_faster(n: int) -> tuple[int, int]:

    def _fib_pair(m) -> tuple[int, int]:  # 返回 F(m), F(m+1)
        if m == 0:
            return 0, 1

        a, b = _fib_pair(m >> 1)  # a=F(k), b=F(k+1)
        c = a * (2 * b - a)       # F(2k)
        d = a * a + b * b         # F(2k+1)
        if m & 1:
            return d, c + d
        return c, d

    return _fib_pair(n)[0]


n = 21
print(fibo_rec(n))
print(fibo_dp_memoized(n))
print(fibo_dp_iter(n))
print(fibo_dp_iter2(n))
print(fibo_rec_faster(n))
