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

##### 最短路径 最优子结构

---

设路径$p = \langle v_0, v_1, \ldots, v_k \rangle$是从$v_0$到$v_k$的一条最短路径，则其任意子路径$\langle v_i, v_{i+1}, \ldots, v_j \rangle$是从$v_i$到$v_j$的最短路径

此时路径$p$分为三部分，$v_0 \overset{p_1}{\rightsquigarrow} v_i \overset{p_2}{\rightsquigarrow} v_j \overset{p_3}{\rightsquigarrow} v_k$

若$p_2$不是最短路径，设$p'_2$更短，则$v_0 \overset{p_1}{\rightsquigarrow} v_i \overset{p'_2}{\rightsquigarrow} v_j \overset{p_3}{\rightsquigarrow} v_k$也更短

<div class="bottom4"></div>

---

<div class="bottom2"></div>

源点到不同点的最短路径显然存在公共的子路径

最优化问题 + 最优子结构 + 公共子问题 ？

<!-- slide data-notes="" -->

##### 最短路径 动态规划

---

如何定义子问题并确定其递推关系？若采用自底向上，何为底？

以源点到其它点的最短路径作为子问题？难以确定递推关系

<div class="top4"></div>

我的启示 最短路径的边数有上界，不超过$|\Vcal|-1$

<div class="top6"></div>

$$
\begin{align*}
    \qquad \qquad \begin{matrix}
    \text{经过不超过 }|\Vcal|-1\text{ 条边的最短路径的长度} \\
    \vdots \\
    \text{经过不超过 }2\text{ 条边的最短路径的长度} \\
    \text{经过不超过 }1\text{ 条边的最短路径的长度} \\
    \end{matrix}
    \qquad \quad \Bigg \Uparrow
\end{align*}
$$

