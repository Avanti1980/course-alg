---
presentation:
  margin: 0
  center: false
  transition: "convex"
  enableSpeakerNotes: true
  slideNumber: "c/t"
  navigationMode: "linear"
---

@import "../css/font-awesome-4.7.0/css/font-awesome.css"
@import "../css/theme/solarized.css"
@import "../css/logo.css"
@import "../css/font.css"
@import "../css/color.css"
@import "../css/margin.css"
@import "../css/table.css"
@import "../css/main.css"
@import "../plugin/zoom/zoom.js"
@import "../plugin/customcontrols/plugin.js"
@import "../plugin/customcontrols/style.css"
@import "../plugin/chalkboard/plugin.js"
@import "../plugin/chalkboard/style.css"
@import "../plugin/menu/menu.js"

<!-- slide data-notes="" -->

##### 最近点对

---

输入：$\Rbb^2$上的$n$个点$S = \{ (x_1, y_1), \ldots, (x_n, y_n) \}$

输出：最近点对的距离$d = \min_{i,j} \sqrt{(x_i - x_j)^2 + (y_i - y_j)^2}$

<div class="top2"></div>

暴力求解：二重 for 循环遍历所有点对，$T(n) = \Omega(n^2)$

<!-- slide vertical=true data-notes="" -->

##### 最近点对 分治

---

输入：$\Rbb^2$上的$n$个点$S = \{ (x_1, y_1), \ldots, (x_n, y_n) \}$

输出：最近点对的距离$d = \min_{i,j} \sqrt{(x_i - x_j)^2 + (y_i - y_j)^2}$

<div class="top2"></div>

分：设$x_1, \ldots, x_n$的中位数为$m$，在$m$处作垂线将$S$均分

1. 最近点对完全位于左半子集
2. 最近点对完全位于右半子集
3. 跨越了中线

<div class="top2"></div>

治：递归求左半子集和右半子集的最近点对

合：处理第 3 种情况，与前 2 种情况的最近点对比较取最小

<!-- slide vertical=true data-notes="" -->

##### 最近点对 跨越中线

---

设$d_l$、$d_r$分别是递归求解出的左半、右半子集的最近点对距离

只需考虑中线左右两侧宽度为$\delta = \min \{ d_l, d_r \}$的带状区域

- 如果跨越中线的一对点其中某个点不在区域内，则其距离$> \delta$
- 按纵坐标从小到大遍历带状区域中的点，每个点只需考虑 {==6==} 个点
- $f(n) = \Theta(n)$，从而递推式为$T(n) = 2 \cdot T(n/2) + \Theta(n) = \Theta(n \lg n)$

@import "../tikz/closest-pair.svg" {.center .width60 .top4}
