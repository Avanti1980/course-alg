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
@import "../css/font-song.css"
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

<!-- slide data-notes="" -->

##### 子集和数 定长元组

---

$n=6$，$(w_1, w_2, w_3, w_4, w_5, w_6) = (5, 10, 12, 13, 15, 18)$，$M = 30$

@import "../dot/subset-sum/subset-sum-example-fix-len.dot" {.center .top1}

<div class="top-54per left46per">

<span class="fs12">(待选数下标, 已选数之和, 剩余数之和)</span>

</div>

<!-- slide data-notes="" -->

##### 子集和数 变长元组

---

$n=6$，$(w_1, w_2, w_3, w_4, w_5, w_6) = (5, 10, 12, 13, 15, 18)$，$M = 30$

@import "../dot/subset-sum/subset-sum-example-var-len.dot" {.center .top1}

<div class="top-43per left22per">

<span class="fs12">(待选数最小下标, 已选数之和, 剩余数之和)</span>

</div>
