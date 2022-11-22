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


