def find_max_subarray(a, low, high):  # 返回最大子数组的起始索引、结束索引、和

    if low == high:
        return low, high, a[low]

    mid = int((low + high) / 2)

    # 递归求解左半数组
    l_low, l_high, l_sum = find_max_subarray(a, low, mid)

    # 递归求解右半数组
    r_low, r_high, r_sum = find_max_subarray(a, mid + 1, high)

    # 处理跨越中点的情况
    c_low, c_high, c_sum = find_max_cross_subarray(a, low, mid, high)

    # 比较三种情况：
    if l_sum > r_sum and l_sum > c_sum:
        return l_low, l_high, l_sum
    elif l_sum < c_sum and r_sum < c_sum:
        return c_low, c_high, c_sum
    else:
        return r_low, r_high, r_sum


def find_max_cross_subarray(a, low, mid, high):
    l_sum = r_sum = -float("inf")

    sum = 0  # 找结束于mid的最大子数组的起始索引
    for i in range(mid, low - 1, -1):  # 遍历 mid -> low
        sum += a[i]
        if sum > l_sum:
            l_sum, l_index = sum, i

    sum = 0  # 找开始于mid+1的最大子数组的结束索引
    for i in range(mid + 1, high + 1):  # 遍历 mid+1 -> high
        sum += a[i]
        if sum > r_sum:
            r_sum, r_index = sum, i

    return l_index, r_index, l_sum + r_sum


a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
n = len(a)
print(find_max_subarray(a, 0, n - 1))
# --------------------------------------
# (7, 10, 43)
