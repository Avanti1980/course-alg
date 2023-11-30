def subset_sum(i, s, left, x):
    # i s left x = 待选数最小下标 已选数之和 剩余数之和 当前元组
    print(i, s, left)
    if i > n:
        return
    else:
        for j in range(i, n):  # 依次尝试选择 w_i, w_i+1, ..., w_n
            if s + w[j] == M:  # 若加上w[j]是一个解 输出
                x.append(j)
                print(x)
                x.pop()
            elif j < n-1:  # 否则 若选择w[j]可满足限界条件 递归
                if s + left >= M and s + w[j] + w[j + 1] <= M:
                    x.append(j)
                    left = 0
                    for k in range(j+1, n):
                        left += w[k]
                    subset_sum(j + 1, s + w[j], left, x)
                    x.pop()


w, M = [0, 5, 10, 12, 13, 15, 18], 30
n = len(w)
x = []
subset_sum(1, 0, sum(w), x)
# ---------------------------
# 1 0 73
# 2 5 68
# 3 15 58
# [1, 2, 5]
# 4 17 56
# [1, 3, 4]
# 3 10 63
# 4 12 61
# [3, 6]
# 5 13 60
