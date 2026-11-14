def find_max_subarray(a: list, low: int, high: int) -> tuple[int, int, int]:
    # 返回最大子数组的起始索引、结束索引、和
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
        key=lambda x: x[2],
    )


def find_max_cross_subarray(a: list, low: int, mid: int, high: int) -> tuple[int, int, int]:
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
