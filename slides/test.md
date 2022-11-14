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

##### <span style="font-weight:900">OBST</span> 最优子结构性

---

如果$T$是关于关键字$k_1, \ldots, k_n$和伪关键字$d_0, \ldots, d_n$的 OBST，则$T$中仅包含$k_i, \ldots, k_j$和$d_{i-1}, \ldots, d_j$的子树$T'$必然也是 OBST

<div class="top-1"></div>

{==剪切-粘贴==}，若$T'$不是最优，则存在更优的$T''$，将$T$中的$T'$替换成$T''$可以得到比$T$更优的 OBST

<div class="top2"></div>

子问题：仅包含$k_i, \ldots, k_j$和$d_{i-1}, \ldots, d_j$的 OBST

- 设$e[i,j]$是期望搜索代价，$w(i,j) = \sum_{l=i}^j p_l + \sum_{l=i-1}^j q_l$是结点概率和
- 最优根结点是$k_r$
- 左子树是仅包含$k_i, \ldots, k_{r-1}$的 OBST
- 右子树是仅包含$k_{r+1}, \ldots, k_j$的 OBST

@import "../dot/binary-search-tree-proof.dot" {.left58per .top-10}

<!-- slide vertical=true data-notes="" -->

##### <span style="font-weight:900">OBST</span> 递推关系式

---

当一棵树成为另一个结点的子树时，所有结点{==深度加 1==}

设$k_r$是最优根结点，递推关系

$$
\begin{align*}
    \quad e[i,j] & = \overbrace{p_r}^{\text{根}} + \overbrace{e[i,r-1] + w (i,r-1)}^{\text{左子树}} + \overbrace{e[r+1,j] + w (r+1,j)}^{\text{右子树}} \\
    & = e[i,r-1] + e[r+1,j] + w(i,j) \\[5px]
    \Longrightarrow & ~ e[i,j] = \begin{cases} q_{i-1}, & j = i - 1 \\ \min_{i \le r \le j} ~ \{ e[i,r-1] + e[r+1,j] + w(i,j) \}, & i \le j \end{cases}
\end{align*}
$$

设$root[i,j]$是仅包含$k_i, \ldots, k_j$和$d_{i-1}, \ldots, d_j$的 OBST 的根节点

<!-- slide vertical=true data-notes="" -->

##### <span style="font-weight:900">OBST</span> 实现

---

<div class="top2"></div>

$$
\begin{align*}
    \quad e[i,j] = \begin{cases} q_{i-1}, & j = i - 1 \\ \min_{i \le r \le j} ~ \{ e[i,r-1] + e[r+1,j] + w(i,j) \}, & i \le j \end{cases}
\end{align*}
$$

<div class="top-1"></div>

@import "../codes/optimal-bst.py" {line_begin=0 line_end=16 .left4 .line-numbers .top-1 .bottom-4 highlight=[12]}

<!-- slide data-notes="" -->

##### <span style="font-weight:900">OBST</span> 例子

---

@import "../tikz/obst.svg" {.center .width90}

<!-- slide vertical=true data-notes="" -->

##### <span style="font-weight:900">OBST</span> 例子

---

<div class="threelines left4 righta top-1 bottom0">

| $p_1$ | $p_2$ | $p_3$ | $p_4$ | $p_5$ | $q_0$ | $q_1$ | $q_2$ | $q_3$ | $q_4$ | $q_5$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0.15  | 0.10  | 0.05  | 0.10  | 0.20  | 0.05  | 0.10  | 0.05  | 0.05  | 0.05  | 0.10  |

</div>

$$
\begin{align*}
    w(i,j) & = \sum_{l=i}^j p_l + \sum_{l=i-1}^j q_l \\
    w(1,0) & = q_0 = 0.05, ~ w(2,1) = q_1 = 0.10, ~ w(3,2) = q_3 = 0.05 \\
    w(4,3) & = q_4 = 0.05, ~ w(5,4) = q_5 = 0.05, ~ w(6,5) = q_6 = 0.10 \\[2px]
    w(1,1) & = q_0 + p_1 + q_1 = 0.05 + 0.15 + 0.10 = 0.30 \\
    w(2,2) & = q_1 + p_2 + q_2 = 0.10 + 0.10 + 0.05 = 0.25 \\
    w(3,3) & = q_1 + p_2 + q_2 = 0.10 + 0.10 + 0.05 = 0.25 \\
    w(4,4) & = q_1 + p_2 + q_2 = 0.10 + 0.10 + 0.05 = 0.25 \\
    w(5,5) & = q_1 + p_2 + q_2 = 0.10 + 0.10 + 0.05 = 0.25 \\
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### <span style="font-weight:900">OBST</span> 例子

---

<div class="threelines left4 righta top-1 bottom0">

| $p_1$ | $p_2$ | $p_3$ | $p_4$ | $p_5$ | $q_0$ | $q_1$ | $q_2$ | $q_3$ | $q_4$ | $q_5$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0.15  | 0.10  | 0.05  | 0.10  | 0.20  | 0.05  | 0.10  | 0.05  | 0.05  | 0.05  | 0.10  |

</div>

$$
\begin{align*}
    e[i,j] & = \begin{cases} q_{i-1}, & j = i - 1 \\ \min_{i \le r \le j} ~ \{ e[i,r-1] + e[r+1,j] + w(i,j) \}, & i \le j \end{cases} \\[5px]
    e[1,0] & = q_0 = 0.05, ~ e[2,1] = q_1 = 0.1, ~ e[3,2] = q_3 = 0.05 \\
    e[4,3] & = q_4 = 0.05, ~ e[5,4] = q_5 = 0.05, ~ e[6,5] = q_6 = 0.1 \\[5px]
    e[1,1] & = e[1,0] + e[2,1] + w(1,1) = 0.05 + 0.1 + 0.3 = 0.45 \\
    e[2,2] & = 0.4, ~ e[3,3] = 0.25, ~ e[4,4] = 0.3, ~ e[5,5] = 0.5 \\[5px]
    e[1,2] & = \min \{ e[1,0] + e[2,2], ~ e[1,1] + e[3,2]\} + w(1,2) \\
    & = \min \{ \class{blue}{0.05 + 0.4}, ~ 0.45 + 0.05 \} + 0.45 \\
    & = 0.9, \quad root[1,2] = 1
\end{align*}
$$
