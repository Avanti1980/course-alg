def activity_selector_rec(k, a):
    m = k + 1
    while m < n and s[m] < f[k]:  # 贪心选择寻找ak之后最早结束的活动
        m = m + 1
    if m < n:        # 若找到 将其加入集合 递归寻找下一个兼容活动
        a.append(m)  # 将am加入集合
        activity_selector_rec(m, a)


def activity_selector_greedy():
    a = [1]                # a1直接选择
    k = 1
    for m in range(1, n):  # 从前向后遍历a1之后的活动
        if s[m] > f[k]:    # 若找到ak之后最早结束的活动am
            a.append(m)    # 将am加入集合
            k = m          # 从am之后的活动中继续寻找
    return a


s = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]      # 开始时间
f = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]  # 结束时间 已排好序
n = len(s)

a = []
activity_selector_rec(0, a)
print(a)

print(activity_selector_greedy())
