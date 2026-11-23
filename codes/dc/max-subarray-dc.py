def find_max_subarray(a: list, low: int, high: int) -> tuple[int, int, float]:
    # 返回最大子数组的 起始索引、结束索引、和
    if low == high:
        return low, high, a[low]

    mid = (low + high) // 2

    # 递归求解左半数组
    l_low, l_high, l_sum = find_max_subarray(a, low, mid)

    # 递归求解右半数组
    r_low, r_high, r_sum = find_max_subarray(a, mid + 1, high)

    # 处理跨越中点的情况
    c_low, c_high, c_sum = find_max_cross_subarray(a, low, mid, high)

    # 三种情况取最大
    return max(
        (l_low, l_high, l_sum),
        (r_low, r_high, r_sum),
        (c_low, c_high, c_sum),
        key=lambda x: x[2])


def find_max_cross_subarray(a: list, low: int, mid: int, high: int) -> tuple[int, int, float]:
    l_sum = r_sum = float("-inf")

    s = 0  # 找结束于 mid 的最大子数组的起始索引
    for i in range(mid, low-1, -1):  # 遍历 mid -> low
        s += a[i]
        if s > l_sum:
            l_sum, l_index = s, i

    s = 0  # 找开始于 mid+1 的最大子数组的结束索引
    for i in range(mid+1, high+1):  # 遍历 mid+1 -> high
        s += a[i]
        if s > r_sum:
            r_sum, r_index = s, i

    return l_index, r_index, l_sum + r_sum


a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
n = len(a)
print(find_max_subarray(a, 0, n - 1))
# --------------------------------------
# (7, 10, 43)


def find_max_subarray_dc_linear(a: list, low: int, high: int) -> tuple[float, float, int, float, int, float, int, int]:
    # 返回8项：子数组总和
    # 最大前缀和 最大前缀的结束索引
    # 最大后缀和 最大后缀的起始索引
    # 最大子数组的和 最大子数组的起始索引 最大子数组的结束索引
    if low == high:
        return a[low], a[low], low, a[low], low, a[low], low, high

    mid = (low + high) // 2

    # 递归求解左半
    l_total, l_pre_sum, l_pre_end, l_suf_sum, l_suf_start, l_best, l_low, l_high = find_max_subarray_dc_linear(
        a, low, mid)

    # 递归求解右半
    r_total, r_pre_sum, r_pre_end, r_suf_sum, r_suf_start, r_best, r_low, r_high = find_max_subarray_dc_linear(
        a, mid + 1, high)

    # 子数组总和 = 左半总和 + 右半总和
    total = l_total + r_total

    # 最大前缀和 = max{左半最大前缀和, 左半总和 + 右半最大前缀和}
    pre_sum, pre_end = max(
        (l_pre_sum, l_pre_end),
        (l_total + r_pre_sum, r_pre_end),
        key=lambda x: x[0])

    # 最大后缀和 = max{右半最大后缀和, 右半总和 + 左半最大后缀和}
    suf_sum, suf_start = max(
        (r_suf_sum, r_suf_start),
        (r_total + l_suf_sum, l_suf_start),
        key=lambda x: x[0])

    # 最大子数组的和 = max{左/右半最大子数组的和, 左半最大后缀和 + 右半最大前缀和}
    best_sum, best_low, best_high = max(
        (l_best, l_low, l_high),
        (r_best, r_low, r_high),
        (l_suf_sum + r_pre_sum, l_suf_start, r_pre_end),
        key=lambda x: x[0])

    return total, pre_sum, pre_end, suf_sum, suf_start, best_sum, best_low, best_high


_, _, _, _, _, best, low, high = find_max_subarray_dc_linear(a, 0, n - 1)
print((low, high, best))
# --------------------------------------
# (7, 10, 43)
