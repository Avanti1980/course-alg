import time
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.font_manager as fm

zhisong = fm.FontEntry(
    fname="/home/avanti/Fonts/Founder/宋/方正FW筑紫古典L明朝 简.TTF", name="FZFW ZhuZi GuDianS LMC")
fm.fontManager.ttflist.insert(0, zhisong)
plt.rcParams.update({
    "font.family": ["Ysabeau Office", "FZFW ZhuZi GuDianS LMC"],
    "axes.unicode_minus": True,
    "savefig.bbox": "tight",
    'legend.fontsize': 14,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    'savefig.transparent': True,
    'text.color': '#586e75',
})


def closest_pair(low, high, sort_y):
    if high - low <= 2:  # 如果不超过3个点 不再递归 直接求最小距离
        closest = float("inf")
        for i in range(low, high + 1):
            for j in range(i + 1, high + 1):
                d = math.hypot(v[i, 0] - v[j, 0], v[i, 1] - v[j, 1])
                if d < closest:
                    closest = d
        return closest

    mid = (low + high) // 2
    xmid = (v[mid, 0] + v[mid + 1, 0]) / 2  # 中线位置

    mask_left = (sort_y >= low) & (sort_y <= mid)  # 左半元素按y升序后的索引
    delta_left = closest_pair(low, mid, sort_y[mask_left])

    mask_right = (sort_y >= mid + 1) & (sort_y <= high)  # 右半元素按y升序后的索引
    delta_right = closest_pair(mid + 1, high, sort_y[mask_right])

    delta = min(delta_left, delta_right)

    strip = sort_y[(v[sort_y, 0] >= xmid - delta) &
                   (v[sort_y, 0] <= xmid + delta)]  # 中间带状区域中的点
    closest = delta
    l = len(strip)
    for i in range(l):  # 计算带状区域中的最近点对
        for j in range(i + 1, min(i + 8, l)):  # 最多考虑7个点
            d = math.hypot(v[strip[i], 0] - v[strip[j], 0],
                           v[strip[i], 1] - v[strip[j], 1])
            if d < closest:
                closest = d

    return min(closest, delta)


np.random.seed(0)

trial = 8
time_cost = np.zeros([2, trial])

for t in range(trial):
    n = 2**(t + 6)
    v = np.random.rand(n, 2)     # 随机生成n个点

    start = time.perf_counter()
    closest = float("inf")
    for i in range(n):
        for j in range(i + 1, n):
            closest = min(closest, math.hypot(
                v[i, 0] - v[j, 0], v[i, 1] - v[j, 1]))  # 暴力穷举
    time_cost[0, t] = time.perf_counter() - start

    start = time.perf_counter()
    v = v[v[:, 0].argsort()]    # 对v按x升序
    sort_y = v[:, 1].argsort()  # 对v按y升序 sort_y记录升序后元素在原来v中的索引
    closest = closest_pair(0, n - 1, sort_y)
    time_cost[1, t] = time.perf_counter() - start

with plt.style.context('Solarize_Light2'):
    n = [2**(t + 6) for t in range(trial)]
    plt.loglog(n, time_cost[0, :], base=2, label="BF")  # 对数坐标轴
    plt.loglog(n, time_cost[1, :], base=2, label="DC")  # 对数坐标轴
    plt.xlabel('点数')
    plt.ylabel('时间')
    plt.legend(framealpha=0.2)
    plt.grid(color='#93a1a1', linestyle='-.', linewidth=0.7)
    plt.savefig("closest-pair.svg")
