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

##### <span style="font-weight:900">Prim</span> 算法

---

基于优先队列的实现，时间复杂度$O((|\Vcal| + |\Ecal|) \lg |\Vcal|)$

@import "../codes/mst-prim.py" {line_begin=3 .left4 .line-numbers .top1 .bottom-10}
