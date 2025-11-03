---
presentation:
  margin: 0
  center: false
  transition: "none"
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

##### 逆序对计数

---

输入：长度为$n$的数组$A$

<div class="top-2"></div>

输出：$A$中逆序对数目

推荐系统中的协同过滤：甲在电影网站上列出了自己最喜爱电影 Top 10，网站如何根据其他用户的电影喜爱列表向甲推荐好友？

构造数组$A[i]$：甲最喜欢的第$i$部电影在乙的列表中的位置

- 若出现$i < j$、$A[i] > A[j]$，则甲、乙在这两部电影的喜好上有分歧
- 逆序对越多，说明甲、乙的电影审美差异越大，不宜推荐

<div class="top2"></div>

暴力求解：二重 for 循环遍历$(i,j)$，$T(n) = \Omega(n^2)$

<!-- slide vertical=true data-notes="" -->

##### 逆序对计数 分治

---

设当前要统计子数组$A[low, \ldots, high]$的逆序对数目

分：$A[low, \ldots, high] = A[low, \ldots, mid] + A[mid+1, \ldots, high]$

治：递归求$A[low, \ldots, mid]$和$A[mid+1, \ldots, high]$的逆序对数目

合：跨越中点的逆序对$low \le i \le mid < j \le high$且$A[i] > A[j]$，与两个递归问题的返回值相加求和

<div class="top2"></div>

<p class="fragment">问题：跨越中点的逆序对可能有$\Theta(n^2)$个，若一个个数，复杂度就是$\Omega(n^2)$，如何加速？</p>

<!-- slide vertical=true data-notes="" -->

##### 跨越中点

---

合并已经排好序的子数组可以自然地发现逆序对

@import "../codes/count-inverse-pair.py" {line_begin=12 line_end=56 .left4 .line-numbers .top0 .bottom1 highlight=[11,20,33,39-42,44]}

<!-- slide vertical=true data-notes="" -->

##### 时间分析

---

处理跨越中点的情况只需一重循环，$f(n) = \Theta(n)$

$$
\begin{align*}
    \quad T(n) = \begin{cases} 1, & n = 1 \\ 2 \cdot T (n/2) + \Theta(n), & n > 1 \end{cases} = \Theta(n \lg n)
\end{align*}
$$

