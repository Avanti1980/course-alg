import numpy as np
import matplotlib.pyplot as plt
from utils4plot import setup_matplotlib


time_cost = np.load('closest-pair-time-cost.npy')
print(time_cost)
trial = time_cost.shape[0]

setup_matplotlib()
with plt.style.context('Solarize_Light2'):
    n = [2**(t + 6) for t in range(trial)]
    plt.loglog(n, time_cost[:, 0], base=2,
               marker='o', label="蛮力法")  # 对数坐标轴
    plt.loglog(n, time_cost[:, 1], base=2,
               marker='s', label="分治法")  # 对数坐标轴
    plt.xlabel('点数')
    plt.ylabel('时间 (秒)')
    plt.grid(color='#93a1a1', linestyle='-.', linewidth=0.7)
    plt.legend()
    plt.savefig("closest-pair.svg")
