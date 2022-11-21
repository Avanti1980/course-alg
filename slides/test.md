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

##### 最短路径 贪心加速？

---

从$s$出发只有$t$和$y$能一步直达，其它点至少需经过其中某个点

注意$w(s,t) = 6 < 7 = w(s,y)$，若做贪心选择，应该先选择$t$

至少从$s$到$t$的最短路径应该是$s \rightarrow t$，但实际也是从$y$中转

从$y$出发后续有负权重的边可以再减少路径长度

若想贪心，不能有负权重的边

@import "../tikz/sp-bellman-ford-final.svg" {.lefta .right4 .width35 .top-10}

<!-- slide vertical=true data-notes="" -->

##### 最短路径 贪心

---

假设图中没有负权重的边，引入已确定最短路径的顶点集合$S$

初始化$S = \{ s \}$，之后不断将其它点加入$S$

从$s$到$y$的最短路径就是$s \rightarrow y$

此时从$t$中转不会再有负权重的边来减少路径长度

$S = \{ s, y \}$

@import "../tikz/sp-2.svg" {.lefta .right4 .width35 .top-6}

<!-- slide vertical=true data-notes="" -->

##### 最短路径 贪心

---

已确定最短路径的顶点集合$S = \{ s, y \}$

@import "../tikz/sp-2.svg" {.lefta .right4 .width35 .top-6}


<!-- slide vertical=true data-notes="" -->

##### 最短路径 贪心

---

@import "../tikz/sp-dijkstra.svg" {.center .width90 .top6}
