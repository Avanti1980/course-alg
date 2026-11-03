import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


ZhuZi = fm.FontEntry(
    fname="/home/avanti/Fonts/Founder/宋/方正FW筑紫古典L明朝 简.TTF", name="FZFW ZhuZi GuDianS LMC")
fm.fontManager.ttflist.insert(0, ZhuZi)
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

time_cost = np.load('time_cost.npy')

trial = 10
with plt.style.context('Solarize_Light2'):
    _, ax = plt.subplots(figsize=(8, 6))
    n = [2**(t + 4) for t in range(trial)]
    ax.loglog(n, time_cost[0, :], base=2,
              ls="solid", label="built-in")  # 对数坐标轴
    ax.loglog(n, time_cost[1, :], base=2, ls="dashed", label="grade school")
    ax.loglog(n, time_cost[2, :], base=2, ls="dashdot", label="Karatsuba")
    ax.loglog(n, time_cost[3, :], base=2, ls="dotted", label="Toom")
    ax.set_xlabel("位数")
    ax.set_ylabel("时间")
    ax.legend(framealpha=0.2, loc="best")
    ax.grid(color='#93a1a1', linestyle='-.', linewidth=0.7)
    plt.savefig(f"integer-multiplication-all-opt.svg")

    _, ax = plt.subplots(figsize=(8, 6))
    n = [2**(t + 4) for t in range(trial)]
    ax.loglog(n, time_cost[1, :], base=2,
              ls="dashed", label="grade school")  # 对数坐标轴
    ax.loglog(n, time_cost[2, :], base=2, ls="dashdot", label="Karatsuba")
    ax.set_xlabel("位数")
    ax.set_ylabel("时间")
    ax.legend(framealpha=0.2, loc="best")
    ax.grid(color='#93a1a1', linestyle='-.', linewidth=0.7)
    plt.savefig(f"integer-multiplication-karatsuba-opt.svg")
