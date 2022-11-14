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

##### <span style="font-weight:900">OBST</span> 实现

---

<div class="top2"></div>

$$
\begin{align*}
    \quad e[i,j] = \begin{cases} q_{i-1}, & j = i - 1 \\ \min_{i \le r \le j} ~ \{ e[i,r-1] + e[r+1,j] + w(i,j) \}, & i \le j \end{cases}
\end{align*}
$$

<div class="top-3"></div>

设$root[i,j]$是仅包含$k_i, \ldots, k_j$的 OBST 的根节点

@import "../codes/optimal-bst.py" {line_begin=0 line_end=16 .left4 .line-numbers .top-1 .bottom-4}

<!-- slide vertical=true data-notes="" -->

##### <span style="font-weight:900">OBST</span> 例子

---

<div class="threelines left4 righta top-1 bottom0">

| $k_1$ | $k_2$ | $k_3$ | $k_4$ | $k_5$ | $d_0$ | $d_1$ | $d_2$ | $d_3$ | $d_4$ | $d_5$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0.15  | 0.10  | 0.05  | 0.10  | 0.20  | 0.05  | 0.10  | 0.05  | 0.05  | 0.05  | 0.10  |

</div>

$$
\begin{align*}
    e[i,j] & = \begin{cases} q_{i-1}, & j = i - 1 \\ \min_{i \le r \le j} ~ \{ e[i,r-1] + e[r+1,j] + w(i,j) \}, & i \le j \end{cases} \\[4px]
    e[1,0] & = 0.05, ~ e[2,1] = 0.1, ~ e[3,2] = e[4,3] = e[5,4] = 0.05, ~ e[6,5] = 0.1 \\[4px]
    e[1,1] & = e[1,0] + e[2,1] + w(1,1) = 0.05 + 0.1 + 0.3 = 0.45 \\
    e[2,2] & = 0.4, ~ e[3,3] = 0.25, ~ e[4,4] = 0.3, ~ e[5,5] = 0.5 \\[4px]
    e[1,2] & = \min \{ \}
\end{align*}
$$

@import "../tikz/obst-w.svg" {.left65per .width30 .bottom4}

<!-- slide vertical=true data-notes="" -->

##### <span style="font-weight:900">OBST</span> 例子

---

@import "../tikz/obst.svg" {.center .width90}
