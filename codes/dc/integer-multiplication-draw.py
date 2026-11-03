import time
import numpy as np
import matplotlib.pyplot as plt
import random
import string
import sys
import matplotlib.font_manager as fm

sys.set_int_max_str_digits(100000)

np.random.seed(0)

ysabeau = fm.FontEntry(fname="/home/avanti/Slides/Courses/Alg/fonts/YsabeauOffice/YsabeauOffice-Medium.otf", name="Ysabeau-Regular")
fm.fontManager.ttflist.insert(0, ysabeau)
plt.rcParams.update({
    "font.family": [ysabeau.name],
    "font.size": 16,
})

time_cost = np.load('time_cost.npy')

trial = 10
with plt.style.context('Solarize_Light2'):
    _, ax = plt.subplots(figsize=(8, 6))
    x = [v + 4 for v in range(trial)]
    ax.plot(x, np.log2(time_cost[0, :]), ls="solid", label="built-in")  # 对数坐标轴
    ax.plot(x, np.log2(time_cost[1, :]), ls="dashed", label="grade school")
    ax.plot(x, np.log2(time_cost[2, :]), ls="dashdot", label="Karatsuba")
    ax.plot(x, np.log2(time_cost[3, :]), ls="dotted", label="Toom")
    ax.set_xlabel("n: power of 2", fontsize=18)
    ax.set_ylabel("time: power of 2", fontsize=18)
    ax.legend(loc="best")
    ax.xaxis.set_major_locator(plt.MultipleLocator(1))
    ax.yaxis.set_major_locator(plt.MultipleLocator(2))
    ax.grid(color='#93a1a1', linestyle='-.', linewidth=0.7)
    plt.savefig(f"integer-multiplication-all.svg", transparent=True, bbox_inches="tight")

    _, ax = plt.subplots(figsize=(8, 6))
    x = [v + 4 for v in range(trial)]
    ax.plot(x, np.log2(time_cost[1, :]), ls="dashed", label="grade school")  # 对数坐标轴
    ax.plot(x, np.log2(time_cost[2, :]), ls="dashdot", label="Karatsuba")
    ax.set_xlabel("n: power of 2", fontsize=18)
    ax.set_ylabel("time: power of 2", fontsize=18)
    ax.legend(loc="best")
    ax.xaxis.set_major_locator(plt.MultipleLocator(1))
    ax.yaxis.set_major_locator(plt.MultipleLocator(2))
    ax.grid(color='#93a1a1', linestyle='-.', linewidth=0.7)
    plt.savefig(f"integer-multiplication-karatsuba.svg", transparent=True, bbox_inches="tight")
