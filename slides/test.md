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

##### 最长递增子序列

---

输入：元素各不相同的序列$X$

<div class="top-2"></div>

输出：$X$的最长递增子序列 (longest increasing subsequence, LIS)

最优子结构性：设以$X[i]$结尾的 LIS 为$X[i_1], \ldots, X[i_k], X[i]$

<div class="top-2"></div>

则$X[i_1], \ldots, X[i_k]$必然是以$X[i_k]$结尾的 LIS

记$d[i]$为以$X[i]$结尾的 LIS 的长度，显然所有$d[i]$的最小值是 1

<div class="top-2"></div>

$d[0] = 1$，以$X[0]$结尾的 LIS 就是$X[0]$

<div class="top-2"></div>

$d[1]$根据$X[1]$是否可以接在$X[0]$后面分两种情况：

- 若$X[0] < X[1]$，则$d[1] = 2$，此时 LIS 就是$X[0, 1]$
- 若$X[0] > X[1]$，则$d[1] = 1$，此时 LIS 就是$X[1]$

<!-- slide vertical=true data-notes="" -->

##### <span style="font-weight:900">LIS</span> 递推关系式

---

$X[i]$接在以$X[0], X[1], \ldots, X[i-1]$结尾的哪个 LIS 后面？

在所有可接的 LIS 后面选一个最长的，递推关系：

$$
\begin{align*}
    \quad d[i] = \begin{cases}
    1, & i=0 \\
    \max_{j < i} ~ \{ d[j] + 1 \}, & X[j] < X[i] \\
    \end{cases}
\end{align*}
$$

@import "../codes/lis.py" {line_begin=7 line_end=15 .left4 .line-numbers .top-3 .bottom0}

二重 for 循环时间复杂度$\Theta(n^2)$，一维表格空间复杂度$\Theta(n)$

<!-- slide vertical=true data-notes="" -->

##### <span style="font-weight:900">LIS</span> 例子

---

<div class="top2"></div>

$$
\begin{align*}
    \quad d[i] = \begin{cases}
    1, & i=0 \\
    \max_{j < i} ~ \{ d[j] + 1 \}, & X[j] < X[i] \\
    \end{cases}
\end{align*}
$$

<div class="threelines top-1">

| $i$ | <span class="yellow">0</span> |  1  | <span class="yellow">2</span> |  3  |  4  | <span class="yellow">5</span> |               6               |  7  |  8  |  9  |
| :-: | :---------------------------: | :-: | :---------------------------: | :-: | :-: | :---------------------------: | :---------------------------: | :-: | :-: | :-: |
| $X$ |            {==②==}            |  8  |            {==④==}            |  9  |  1  |            {==⑥==}            |            {==⑦==}            |  3  |  0  |  5  |
| $d$ |               1               |  2  |               2               |  3  |  1  |               3               |  <span class="red">4</span>   |  2  |  1  |  3  |
| $b$ |              -1               |  0  | <span class="yellow">0</span> |  1  | -1  | <span class="yellow">2</span> | <span class="yellow">5</span> |  0  | -1  |  2  |

</div>

@import "../codes/lis.py" {line_begin=17 line_end=22 .left4 .line-numbers .top0 .bottom0 highlight=[7-9]}
