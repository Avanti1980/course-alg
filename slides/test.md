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

输入：$\{ 1,\ldots,n \}$的排列$X$

<div class="top-2"></div>

输出：$X$的最长递增子序列 (longest increasing subsequence, LIS)

记$d[i]$为以$X[i]$结尾的 LIS 的长度，显然所有$d[i]$的最小值是 1

$d[0] = 1$，以$X[0]$结尾的 LIS 就是$X[0]$

$d[1]$根据$X[1]$是否可以接在$X[0]$后面分两种情况：

- 若$X[0] < X[1]$，则$d[1] = 2$，此时 LIS 就是$X[0, 1]$
- 若$X[0] > X[1]$，则$d[1] = 1$，此时 LIS 就是$X[1]$

<!-- slide vertical=true data-notes="" -->

##### 最长递增子序列

---

输入：$\{ 1,\ldots,n \}$的排列$X$

<div class="top-2"></div>

输出：$X$的最长递增子序列 (longest increasing subsequence, LIS)

记$d[i]$为以$X[i]$结尾的 LIS 的长度，显然所有$d[i]$的最小值是 1

$X[i]$接在以$X[0], X[1], \ldots, X[i-1]$结尾的哪个 LIS 后面？

在所有可接的 LIS 后面，选一个最长的，因此有递推关系：

$$
\begin{align*}
    \quad d[i] = \begin{cases}
    1, & i=0 \\
    \max_{j < i} ~ \{ d[j] + 1 \}, & X[j] < X[i] \\
    \end{cases}
\end{align*}
$$
