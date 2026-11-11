import numpy as np


def setup_matplotlib():
    """配置中文字体与样式"""
    import matplotlib.font_manager as fm
    import matplotlib.pyplot as plt

    font_path = '/home/avanti/Fonts/Founder/宋/方正FW筑紫古典L明朝 简.TTF'
    fm.fontManager.addfont(font_path)
    plt.rcParams.update({
        'font.family': ['Ysabeau Office', fm.FontProperties(fname=font_path).get_name()],
        'axes.unicode_minus': True,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'legend.fontsize': 12,
        'legend.framealpha': 0.4,
        'legend.loc': 'best',
        'savefig.bbox': 'tight',
        'savefig.transparent': True,
        'text.color': '#586e75',
    })
    return plt


if __name__ == "__main__":
    time_cost = np.load('matrix-multiply-time-cost.npy')
    trial = time_cost.shape[0]

    plt = setup_matplotlib()
    with plt.style.context('Solarize_Light2'):
        n = [2**(t + 5) for t in range(trial)]
        plt.loglog(n, time_cost[:, 1], base=2, marker='o', label="三重循环")
        plt.loglog(n, time_cost[:, 2], base=2, marker='s', label="朴素分治")
        plt.loglog(n, time_cost[:, 3], base=2, marker='x', label="Strassen")
        plt.xlabel("矩阵阶数")
        plt.ylabel("时间 (秒)")
        plt.grid(color='#93a1a1', linestyle='-.', linewidth=0.7)
        plt.legend()
        plt.savefig(f"matrix-multiply.svg")
