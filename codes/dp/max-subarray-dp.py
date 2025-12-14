import numpy as np


def find_max_subarray_dp(A, n):
    dp = [0] * n                    # dp[i]为以A[i]作结尾的最大子数组的和
    s = [0] * n                     # s[i]为以A[i]作结尾的最大子数组的起始索引
    dp[0], s[0] = A[0], 0
    for i in range(1, n):
        if dp[i - 1] >= 0:
            dp[i] = dp[i - 1] + A[i]  # A[i]接在A[j,...,i-1]后面
            s[i] = s[i - 1]           # 继承其起始索引
        else:
            dp[i] = A[i]            # A[i]不接在A[j,...,i-1]后面 另起炉灶
            s[i] = i                # 起始索引就是当前位置
    max_index = np.argmax(dp)       # 遍历dp获取最大元的索引
    return s[max_index], max_index, dp[max_index]


A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
n = len(A)
print(find_max_subarray_dp(A, n))
# ----------------------------------
# (7, 10, 43)
