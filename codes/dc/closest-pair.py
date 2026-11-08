import time
import math
import numpy as np
import numpy.typing as npt


def closest_pair(x: npt.NDArray, y: npt.NDArray, low: int, high: int, order_y: npt.NDArray) -> float:
    if high - low <= 2:  # 如果不超过3个点 不再递归 直接求最小距离
        closest = float("inf")
        for i in range(low, high + 1):
            for j in range(i + 1, high + 1):
                d = math.hypot(x[i] - x[j], y[i] - y[j])
                if d < closest:
                    closest = d
        return closest

    mid = (low + high) // 2
    xmid = (x[mid] + x[mid + 1]) / 2  # 中线位置

    delta_left = closest_pair(
        x, y, low, mid, order_y[(order_y >= low) & (order_y <= mid)])
    delta_right = closest_pair(
        x, y, mid + 1, high, order_y[(order_y >= mid + 1) & (order_y <= high)])

    delta = min(delta_left, delta_right)
    strip = order_y[np.abs(x[order_y] - xmid) <= delta]  # 中间带状区域中的点
    closest = delta
    l = len(strip)
    for i in range(l):  # 计算带状区域中的最近点对
        for j in range(i + 1, min(i + 8, l)):  # 最多考虑7个点
            d = math.hypot(x[strip[i]] - x[strip[j]],
                           y[strip[i]] - y[strip[j]])
            if d < closest:
                closest = d

    return min(closest, delta)


np.random.seed(0)

if __name__ == "__main__":

    trial = 8
    time_cost = np.empty([trial, 2])

    for t in range(trial):
        n = 2**(t + 6)
        x = np.random.rand(n)     # 随机生成 n 个点的横坐标
        y = np.random.rand(n)     # 随机生成 n 个点的纵坐标

        start = time.perf_counter()
        closest = float("inf")
        for i in range(n):
            for j in range(i + 1, n):
                closest = min(closest, math.hypot(
                    x[i] - x[j], y[i] - y[j]))  # 暴力穷举
        time_cost[t, 0] = time.perf_counter() - start

        start = time.perf_counter()
        order = x.argsort()    # x 升序的索引表
        x = x[order]           # x 升序
        y = y[order]           # 按 x 升序的 y
        order_y = y.argsort()  # y 升序的索引表
        closest = closest_pair(x, y, 0, n - 1, order_y)
        time_cost[t, 1] = time.perf_counter() - start

    print(time_cost)
    np.save('closest-pair-time-cost.npy', time_cost)
