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

##### <span style="font-weight:900">Dijkstra</span> 算法 正确性

---

不变式：在外层 for 循环每次执行前，对$\forall u \in \Scal$有$u.d = \delta (s,u)$

- 根据算法，点$u$一旦加入$\Scal$，就不会再修正$u.d$
- 只需证明对$\forall u \in \Scal$，当其被加入到$\Scal$时有$u.d = \delta (s,u)$

<div class="top2"></div>

初始$\Scal = \emptyset$，之后源点$s$第一个加入$\Scal$，显然$s.d = \delta (s,s) = 0$

<div class="top-1"></div>

设$u$是{==第一个==}加入$\Scal$时$u.d \ne \delta (s,u)$的点，此时存在$s \rightsquigarrow u$的路径

否则$u.d = \delta (s,u) = \infty$，与假设矛盾

设$s$到$u$的最短路径为$p$



<!-- slide vertical=true data-notes="" -->

##### <span style="font-weight:900">Dijkstra</span> 算法 正确性

---

下面说明$u$是路径$p$上第一个不在$\Scal$中的点

<div class="top-1"></div>

否则设$u$前还有点$y$不在$\Scal$中，$s \overset{p_1}{\rightsquigarrow} y \overset{p_2}{\rightsquigarrow} u$

那么

设$y$是路径$p$上第一个不在$\Scal$中的点，$y$的前驱$x \in \Scal$

路径分为$s \rightsquigarrow x \rightarrow y \rightsquigarrow u$

