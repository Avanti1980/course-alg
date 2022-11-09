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

##### 矩阵连乘问题

---

设$\Av \in \Rbb^{p \times q}$、$\Bv \in \Rbb^{q \times r}$，则$\Cv = \Av \Bv \in \Rbb^{p \times r}$

计算$c_{ij} = \sum_{1 \le k \le q} a_{ik} b_{kj}$需做$q$次标量乘法

计算$\Cv$需$pqr$次标量乘法

<div class="top4"></div>

设$\Av_1 \in \Rbb^{10 \times 100}$、$\Av_2 \in \Rbb^{100 \times 5}$、$\Av_3 \in \Rbb^{5 \times 50}$，根据结合律

- 共$(\Av_1 \Av_2) \Av_3 = 10 \times 100 \times 5 \times 5$次标量乘法
- 共$\Av_1 (\Av_2 \cdots \Av_3 =---------10 \times 100 \times 5 \times 5$次标量乘法
