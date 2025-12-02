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

<!-- slide vertical=true data-notes="" -->

##### 问题描述

---

给定带权有向图$\Gcal = (\Vcal, \Ecal, w)$

- 点集$\Vcal$对应城市
- 边集$\Ecal$对应直接连接两城市的道路
- 边上的权重由函数$w: \Ecal \mapsto \Rbb$给出，对应距离、时间、路费等

<div class="top4"></div>

路径$p = \langle v_0, v_1, \ldots, v_k \rangle$的长度$l(p) = \sum_{i=1}^k w(v_{i-1}, v_i)$是路径上所有边的权重之和

问题目标：寻找源点$s$到目的点$t$的最短路径：

$$
\begin{align*}
    \quad \delta(s,t) = \begin{cases} \min_p \{ l(p) : s \overset{p}{\rightsquigarrow} t \}, & \text{如果存在 } s \text { 到 } t \text{ 的路径} \\ \infty, & \text{其它} \end{cases}
\end{align*}
$$

<p class="footnote comments"> 权重函数$w: \Ecal \mapsto \Rbb$的值域为$\Rbb$表示边上权重可以为负，对应于走该边可以挣一些钱</p>
