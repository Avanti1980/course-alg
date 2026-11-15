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
@import "../plugin/notes/notes.js"
@import "../plugin/customcontrols/plugin.js"
@import "../plugin/customcontrols/style.css"
@import "../plugin/chalkboard/plugin.js"
@import "../plugin/chalkboard/style.css"
@import "../plugin/reveal.js-menu/menu.js"

<!-- slide vertical=true data-notes="" -->

##### 子问题图

---

自底向上处理子问题的顺序：

- 对任意子问题，先求解它指向的子问题
- 当它指向的所有子问题都求解完才会求解它

<div class="top2"></div>

<p class="fragment">算法运行时间等于所有子问题求解时间之和</p>

<p class="fragment">子问题的求解时间与对应顶点的<span class="blue">出度</span>成正比</p>

<p class="fragment">动态规划的运行时间一般与顶点和边的数量至少呈线性关系</p>

<img src="../dot/dp/subproblem.svg" class="top-40per lefta right14">
