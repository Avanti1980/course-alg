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

##### 有向无环图 <span style="font-weight:900">DFS</span>

---

松弛

$$
\begin{align*}
    \quad d_v = \begin{cases} 0, & v = s \\ \min_u \{ d_u + w(u,v) \}, & \text{其它} \end{cases}
\end{align*}
$$

Ford 算法框架实现：

- 若图上有边$(u,v)$，则$d_v$依赖$d_u$
- 利用后序 (posrorder) 形式的深度优先搜索得到结点的拓扑序
- 根据拓扑序依次松弛每个点的入边

<div class="top4"></div>

时间复杂度为$O(|\Vcal| + |\Ecal|)$

<!-- slide vertical=true data-notes="" -->

##### 无权图 <span style="font-weight:900">BFS</span>

---

@import "../codes/sssp/dfs-sssp.py" {.left4 .line-numbers highlight=[6] .top1 .bottom-10}


