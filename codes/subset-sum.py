def subset_sum(i, s, left, x):
    print(i, s, left)
    if i == n:
        return
    else:
        if s + w[i] == M:  # 找到一个解 输出 返回 不再递归
            x.append(1)
            print([i for i in x if i != None])
            x.pop()
            return
        if s + left >= M and s + w[i] + w[i + 1] <= M:  # 选择w[i]
            x.append(1)
            subset_sum(i + 1, s + w[i], left - w[i], x)
            x.pop()
        if s - w[i] + left >= M and s + w[i + 1] <= M:  # 不选择w[i]
            x.append(0)
            subset_sum(i + 1, s, left - w[i], x)
            x.pop()


w = [5, 10, 12, 13, 15, 18]   # 集合
n = len(w)
x = []                        # 解
M = 30                        # 目标和
subset_sum(0, 0, sum(w), x)
---------------------------
0 0 73
1 5 68
2 15 58
3 15 46
4 15 33
[1, 1, 0, 0, 1]
2 5 58
3 17 46
[1, 0, 1, 1]
3 5 46
4 5 33
1 0 68
2 10 58
3 10 46
4 10 33
2 0 58
3 12 46
4 12 33
5 12 18
[0, 0, 1, 0, 0, 1]
3 0 46
4 13 33
4 0 33
