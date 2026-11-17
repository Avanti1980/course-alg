import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


def setup_matplotlib() -> None:  # 配置中文字体与样式
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
