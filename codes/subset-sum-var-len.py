def subset_sum(i, s, left, x):
    print(i, s, left)
    if i > n:
        return
    else:
        for j in range(i, n):
            if s + w[j] == M:  # 找到一个解 输出 返回 不再递归
                x.append(j)
                print(x)
                x.pop()
            elif j < n-1:
                if s + left >= M and s + w[j] + w[j + 1] <= M:  # 选择w[j]满足限界条件
                    x.append(j)
                    subset_sum(j + 1, s + w[j], left - w[j], x)
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