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

##### 增广路径

---

给定流网络$\Gcal = (\Vcal, \Ecal)$和流$f$，增广路径$p$是其残存网络$\Gcal_f$中一条从源点$s$到汇点$t$的简单路径

增广路径的残存容量是所有边上残存容量的最小值

$$
\begin{align*}
    \quad c_f (p) = \min \{ c_f (u,v): (u,v) \in p \}
\end{align*}
$$

下图蓝色路径就是一条增广路径，$c_f (p) = \min \{ 5,4,5 \} = 4$

@import "../tikz/max-flow-aug2.svg" {.center .top4 .width90}

<!-- slide vertical=true data-notes="" -->

##### 增广路径

---

根据增广路径的残存容量立刻可以得到残存网络中的一个流$f_p$

$$
\begin{align*}
    \quad f_p (u,v) = \begin{cases} c_f(p), & (u,v) \in p \\ 0, & \text{其它} \end{cases}
\end{align*}
$$

$f \uparrow f_p$是原流网络$\Gcal$中的一个流，流值$|f \uparrow f_p| = |f| + |f_p| > |f|$

<div class="top2"></div>

Ford-Fulkerson 方法：利用残存网络和增广路径迭代改进流

如何寻找增广路径？深度优先搜索或广度优先搜索
