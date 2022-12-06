def subset_sum(i, s, left, x):
    print(i, s, left)
    if i > n:
        return
    else:
        if s + w[i] == M:  # 找到一个解 输出 返回 不再递归
            x.append(1)
            print(x)
            x.pop()
            return
        if s + left >= M and s + w[i] + w[i + 1] <= M:  # 选择w[i]满足限界条件
            x.append(1)
            subset_sum(i + 1, s + w[i], left - w[i], x)
            x.pop()
        if s - w[i] + left >= M and s + w[i + 1] <= M:  # 不选择w[i]满足限界条件
            x.append(0)
            subset_sum(i + 1, s, left - w[i], x)
            x.pop()


w, M = [0, 5, 10, 12, 13, 15, 18], 30
n = len(w)
x = []
subset_sum(1, 0, sum(w), x)
# ---------------------------
# 1 0 73
# 2 5 68
# 3 15 58
# 4 15 46
# 5 15 33
# [1, 1, 0, 0, 1]
# 3 5 58
# 4 17 46
# [1, 0, 1, 1]
# 4 5 46
# 5 5 33
# 2 0 68
# 3 10 58
# 4 10 46
# 5 10 33
# 3 0 58
# 4 12 46
# 5 12 33
# 6 12 18
# [0, 0, 1, 0, 0, 1]
# 4 0 46
# 5 13 33
# 5 0 33
