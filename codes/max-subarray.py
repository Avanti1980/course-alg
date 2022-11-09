def find_max_subarray(A, low, high):  # 返回最大子数组的起始索引、结束索引、和

    if low == high:
        return low, high, A[low]

    mid = int((low+high)/2)

    # 递归求解左半数组
    l_low, l_high, l_sum = find_max_subarray(A, low, mid)

    # 递归求解右半数组
    r_low, r_high, r_sum = find_max_subarray(A, mid+1, high)

    # 处理跨越中点的情况
    c_low, c_high, c_sum = find_max_cross_subarray(A, low, mid, high)

    # 比较三种情况：
    if l_sum > r_sum and l_sum > c_sum:
        return l_low, l_high, l_sum
    elif l_sum < c_sum and r_sum < c_sum:
        return c_low, c_high, c_sum
    else:
        return r_low, r_high, r_sum


def find_max_cross_subarray(A, low, mid, high):
    l_sum = r_sum = -65536

    sum = 0  # 找左边的最大子数组
    for i in range(mid, low-1, -1):
        sum += A[i]
        if sum > l_sum:
            l_sum, l_index = sum, i

    sum = 0  # 找右边的最大子数组
    for i in range(mid+1, high+1):
        sum += A[i]
        if sum > r_sum:
            r_sum, r_index = sum, i

    return l_index, r_index, l_sum + r_sum


def find_max_subarray_dp(A):
    dp = [0] * len(A)  # dp[i]为以A[i]作结尾的最大子数组的和
    dp[0] = A[0]
    for i in range(1, len(A)):
        if dp[i-1] >= 0:
            dp[i] = dp[i-1] + A[i]
        else:
            dp[i] = A[i]
    return max(dp)


def find_max_subarray_dp2(A):
    dp = [0] * len(A)  # dp[i]为以A[i]作结尾的最大子数组的和
    s = [0] * len(A)   # s[i]为以A[i]作结尾的最大子数组的起始索引
    dp[0], s[0] = A[0], 0
    for i in range(1, len(A)):
        if dp[i-1] >= 0:
            dp[i] = dp[i-1] + A[i]
            s[i] = s[i-1]
        else:
            dp[i] = A[i]
            s[i] = i
    max_value = max(dp)
    max_index = dp.index(max_value)
    return s[max_index], max_index, max_value


A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

print(find_max_subarray(A, 0, len(A)-1))
print(find_max_subarray_dp(A))
print(find_max_subarray_dp2(A))
