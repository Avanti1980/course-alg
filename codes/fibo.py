def fibo_rec(n):
    if n <= 1:
        return n
    else:  # 递归求解两个子问题
        return fibo_rec(n - 1) + fibo_rec(n - 2)


def fibo_dp_memoized(n):
    F = [-float("inf")] * (n + 1)  # 备忘录初始化为负无穷
    return fibo_dp_memoized_aux(n, F)


def fibo_dp_memoized_aux(n, F):
    if n <= 1:
        return n
    else:
        if F[n] >= 0:
            return F[n]
        else:
            F[n] = fibo_dp_memoized_aux(n - 1, F) + fibo_dp_memoized_aux(n - 2, F)
            return F[n]


def fibo_dp_iter(n):
    F = [0] * (n + 1)
    F[1] = 1
    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F[n]


def fibo_dp_iter2(n):
    prev, curr = 0, 1
    for i in range(n - 1):
        next = prev + curr
        prev, curr = curr, next
    return curr


def fibo_rec_faster(n):
    if n == 1:
        return 0, 1
    m = int(n / 2)
    prev_, curr_ = fibo_rec_faster(m)
    prev = prev_**2 + curr_**2
    curr = curr_ * (2 * prev_ + curr_)
    next = prev + curr
    if n & 1:
        return curr, next
    else:
        return prev, curr


n = 32
print(fibo_rec(n))
print(fibo_dp_memoized(n))
print(fibo_dp_iter(n))
print(fibo_dp_iter2(n))
print(fibo_rec_faster(n))
