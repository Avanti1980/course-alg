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
@import "../plugin/notes/notes.js"
@import "../plugin/customcontrols/plugin.js"
@import "../plugin/customcontrols/style.css"
@import "../plugin/chalkboard/plugin.js"
@import "../plugin/chalkboard/style.css"
@import "../plugin/reveal.js-menu/menu.js"

<!-- slide data-notes="" -->

##### 子集和数

---

输入：$n$个正整数的集合$W = \{ w_1, w_2, \ldots, w_n \}$和正整数$M$

<div class="top-2"></div>

输出：$W$中的和数等于$M$的所有子集

例 1：

- $n=4$，$(w_1, w_2, w_3, w_4) = (7, 11, 13, 24)$，$M = 31$
- 子集：$(7, 11, 13)$、$(7, 24)$

<div class="top2"></div>

例 2：

- $n=6$，$(w_1, w_2, w_3, w_4, w_5, w_6) = (5, 10, 12, 13, 15, 18)$，$M = 30$
- 子集：$(5, 10, 15)$、$(5, 12, 13)$、$(12,18)$

<!-- slide vertical=true data-notes="" -->

##### 子集和数 分治

---

子问题：$\{ w_i, w_{i+1}, \ldots, w_n \}$的子集和为$m$

<p class="fragment">令$ss[i, m]$表示子问题是否有解，$ss[1, M]$即为所求目标</p>

<ul>
    <li class="fragment">若$w[i]$不是和为$m$的加数之一，则$ss[i, m] = ss[i+1, m]$</li>
    <li class="fragment">若$w[i]$是和为$m$的加数之一，则$ss[i, m] = ss[i+1, m-w[i]]$</li>
</ul>

<div class="top2"></div>

<p class="fragment">综上，$ss[i, m] = ss[i+1, m] \vee ss[i+1, m-w[i]]$</p>

<p class="fragment">$i$从$1$开始每增大$1$，产生两个新的子问题，子问题总数为$2^n$</p>

<!-- slide data-notes="" -->

##### 子集和数 动态规划

---

子问题：$\{ w_i, w_{i+1}, \ldots, w_n \}$的子集和为$m$

令$ss[i, m]$表示子问题是否有解，$ss[1, M]$即为所求目标

$ss[i, m] = ss[i+1, m] \vee ss[i+1, m-w[i]]$

<p class="fragment">边界：</p>

<ul>
    <li class="fragment">若$m = 0$，$ss[i, m]$恒为真</li>
    <li class="fragment">若$m < 0$或$i>n$，$ss[i, m]$恒为假</li>
</ul>

<div class="top2"></div>

<p class="fragment">优化 (减少一个子问题)：</p>

<ul>
    <li class="fragment">若$m < w[i]$，则$w[i]$必然不是加数之一，$ss[i, m] = ss[i+1, m]$</li>
</ul>

<!-- slide vertical=true data-notes="" -->

##### 子集和数 动态规划

---

子问题：$\{ w_i, w_{i+1}, \ldots, w_n \}$的子集和为$m$

令$ss[i, m]$表示子问题是否有解，$ss[1, M]$即为所求目标

<p>
\begin{align}
    ss[i, m] = \begin{cases} \true, & m = 0 \\ \false, & m < 0 ~ 或 ~ i > n \\ ss[i+1, m], & m < w_i \\ ss[i+1, m] \vee ss[i+1, m-w_i], & 其它 \end{cases}
\end{align}
</p>

<div class="top2"></div>

- 表$ss$的大小为$n \times (M+1)$，元素为布尔值
- 表第$0$列全部为真
- 第$i$行依赖第$i+1$行的元素，填表时从最后一行往前填

<!-- slide data-notes="" -->

##### 子集和数 实现

---

令$ss[i, m]$表示子问题是否有解

<p>
\begin{align}
    ss[i, m] = \begin{cases} \true, & m = 0 \\ \false, & m < 0 ~ 或 ~ i > n \\ ss[i+1, m], & m < w_i \\ ss[i+1, m] \vee ss[i+1, m-w_i], & 其它 \end{cases}
\end{align}
</p>

@import "../codes/dp/subset-sum-dp.py" {line_begin=3 line_end=16 .left2 .line-numbers .top0 .bottom0}

<!-- slide vertical=true data-notes="" -->

##### 子集和数 重构解

---

@import "../codes/dp/subset-sum-dp.py" {line_begin=18 line_end=41 .left2 .line-numbers .top1 .bottom0}

<!-- slide data-notes="" -->

##### 子集和数 效率

---

@import "../codes/dp/subset-sum-dp.py" {line_begin=3 line_end=16 .left2 .line-numbers .top1 .bottom0 highlight=[7-8]}

二重 for 循环，复杂度$O(nM)$

<ul>
    <li class="fragment">若$M \ll 2^n$，动态规划可以带来显著收益</li>
    <li class="fragment">若$M \ge 2^n$，动态规划不如分治，计算了大量分治不会考虑的子问题</li>
</ul>

<p class="conclusion fragment top4"> 不要无脑动态规划，它并不是总能有提升的</p>
