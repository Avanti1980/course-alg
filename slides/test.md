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

##### 另一改进思路

---

子数组$a[low, ..., high]$的最大子数组为下面三者中的最大者：

- $a[low, ..., mid]$的最大子数组
- $a[mid + 1, ..., high]$的最大子数组
- 跨越中点的最大子数组

其中跨越中点的最大子数组的起始索引$i$需要从$mid$向前遍历确定；结束索引$j$需要从$mid + 1$向后遍历确定，因此$f(n) = \Theta(n)$，从而

<p>
\begin{align}
    T(n) = 2 \cdot T (n/2) + f(n) \Longrightarrow T(n) = \Theta(n \lg n)
\end{align}
</p>

<div class="top2"></div>

根据主定理，要想改进$T(n)$，需优化$f(n)$

<!-- slide vertical=true data-notes="" -->

##### 另一改进思路

---

对任意子数组$a[l, ..., r]$

- 若维护以$l$为起始索引的最大子数组的和 (最大前缀和) 以及最大前缀的结束索引 (最大前缀终点)，则确定$j$只需$\Theta(1)$的时间 (将$mid+1$看作$l$)
- 若维护以$r$为结束索引的最大子数组的和 (最大后缀和) 以及最大后缀的起始索引 (最大后缀起点)，则确定$i$只需$\Theta(1)$的时间 (将$mid$看作$r$)

<div class="top2"></div>

对每个子数组，还需要维护最大前缀、最大后缀

- $a[l, ..., r]$的最大前缀要么等于$a[l, ..., m]$的最大前缀，要么等于$a[l, ..., m]$加上$a[m + 1, ..., r]$的最大前缀
- $a[l, ..., r]$的最大后缀要么等于$a[m+1, ..., r]$的最大后缀，要么等于$a[l, ..., m]$的最大后缀加上$a[m + 1, ..., r]$

<div class="top2"></div>

对每个子数组，还需要维护全部元素和

<!-- slide vertical=true data-notes="" -->

##### 另一改进思路

---

综上，对每个子数组，维护八元组

1. 子数组总和
2. 最大前缀和
3. 最大前缀的结束索引
4. 最大后缀和
5. 最大后缀的起始索引
6. 最大子数组的和
7. 最大子数组的起始索引
8. 最大子数组的结束索引

<div class="top2"></div>

由$a[low, ..., mid]$和$a[mid+1, ..., high]$的八元组得到$a[low, ..., high]$的八元组只需$\Theta(1)$的时间

<p>
\begin{align}
    T(n) = 2 \cdot T (n/2) + \Theta(1) \Longrightarrow T(n) = \Theta(n)
\end{align}
</p>

<!-- slide vertical=true data-notes="" -->

##### 另一改进思路 实现

---

@import "../codes/dc/max-subarray-dc.py" {line_begin=49 line_end=90 .line-numbers highlight=[]}
