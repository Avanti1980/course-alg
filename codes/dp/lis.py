def lis(X: list) -> tuple[list[int], list[int]]:
    n = len(X)
    d, b = [1] * n, [-1] * n
    for i in range(1, n):
        for j in range(i):
            if X[j] < X[i] and d[i] < d[j] + 1:  # X[i]可接在X[j]后面
                d[i] += 1
                b[i] = j  # 更新前一个元素的索引
    return d, b


def restore_lis_iter(X: list, b: list[int], idx: int) -> list:
    LIS: list[int] = []
    while idx != -1:
        LIS.append(idx)
        idx = b[idx]
    LIS.reverse()
    return [X[i] for i in LIS]


X = [2, 8, 4, 9, 1, 6, 7, 3, 0, 5]
d, b = lis(X)
idx = d.index(max(d))
print(restore_lis_iter(X, b, idx))
# ----------------------------------
# [2, 4, 6, 7]


def restore_lis_rec(X: list, b: list[int], idx: int) -> list:
    LIS: list[int] = []

    def _restore_lis_rec(idx: int) -> None:
        if idx == -1:
            return
        _restore_lis_rec(b[idx])
        LIS.append(idx)

    _restore_lis_rec(idx)
    return [X[i] for i in LIS]


print(restore_lis_rec(X, b, idx))
# ----------------------------------
# [2, 4, 6, 7]


def lis_plus(X: list) -> tuple[list[int], list[int], list[int]]:
    from bisect import bisect_left
    e: list[int] = []             # e[i]记录长度为i的递增子序列的末位元素最小值
    b: list[int] = [-1] * len(X)  # b[i]记录X[i]在LIS中的前驱索引
    idx: list[int] = []           # idx[i]记录e[i]在X中的索引
    for i, xi in enumerate(X):
        j = bisect_left(e, xi)  # 在e中对X[i]进行二分查找
        if j == len(e):  # X[i] > e[-1]
            if j > 0:
                b[i] = idx[-1]
            e.append(xi)  # 将其接在e后面表示找到了更长的递增子序列
            idx.append(i)
        else:  # e[j-1] < X[i] < e[j]
            if j > 0:
                b[i] = idx[j - 1]
            e[j] = xi  # 将e[j]改为X[i] 可以改进现有长度为j的递增子序列
            idx[j] = i
    return e, b, idx


e, b, idx = lis_plus(X)
print(restore_lis_iter(X, b, idx[-1]))
# ----------------------------------
# [2, 4, 6, 7]
