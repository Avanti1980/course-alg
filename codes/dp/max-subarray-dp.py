def find_max_subarray_dp(a: list) -> tuple[int, int, float]:
    n = len(a)
    d = [0] * n  # d[i]为以a[i]作结尾的最大子数组的和
    s = [0] * n  # s[i]为以a[i]作结尾的最大子数组的起始索引
    d[0], s[0] = a[0], 0
    for i in range(1, n):
        if d[i - 1] >= 0:
            d[i] = d[i - 1] + a[i]  # a[i]接在a[j,...,i-1]后面
            s[i] = s[i - 1]         # 继承其起始索引
        else:
            d[i] = a[i]          # a[i]不接在a[j,...,i-1]后面 另起炉灶
            s[i] = i             # 起始索引就是当前位置
    max_index = d.index(max(d))  # 遍历d获取最大元的索引
    return s[max_index], max_index, d[max_index]


a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print(find_max_subarray_dp(a))
# ----------------------------------
# (7, 10, 43)


def find_max_subarray_space_opt(a: list) -> tuple[int, int, float]:
    n = len(a)
    cur_sum = a[0]      # 以当前元素结尾的最大子数组和
    cur_start = 0       # 该段的起始下标
    best_sum = cur_sum  # 全局最优和
    best_start = 0      # 全局最优段起始
    best_end = 0        # 全局最优段结束
    for i in range(1, n):
        if cur_sum >= 0:
            cur_sum += a[i]  # a[i]接在a[j,...,i-1]后面
        else:
            cur_sum = a[i]   # a[i]不接在a[j,...,i-1]后面 另起炉灶
            cur_start = i    # 起始索引就是当前位置
        if cur_sum > best_sum:
            best_sum = cur_sum
            best_start = cur_start
            best_end = i
    return best_start, best_end, best_sum


print(find_max_subarray_space_opt(a))
# ----------------------------------
# (7, 10, 43)
