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

<!-- slide data-notes="哈密顿回路的数目与给定初始点是无关的" -->

##### 哈密顿回路

---

输入：无向图，初始点

<div class="top-2"></div>

输出：从给定初始点出发，恰好经过每个顶点一次的回路

@import "../dot/hamilton1.dot" {.left65per}

<div class="top-26per"></div>

例 1：从点 a 出发的 2 条哈密顿回路

- a -> b -> c -> e -> d -> a
- a -> d -> e -> c -> b -> a

<!-- slide vertical=true data-notes="" -->

##### 哈密顿回路

---

输入：无向图，初始点

<div class="top-2"></div>

输出：从给定初始点出发，恰好经过每个顶点一次的回路

@import "../dot/hamilton2.dot" {.left65per}

<div class="top-26per"></div>

例 2：从点 c 出发的 6 条哈密顿回路

- c -> a -> b -> f -> e -> d -> c
- c -> a -> d -> e -> f -> b -> c
- c -> b -> f -> e -> d -> a -> c
- c -> d -> a -> b -> f -> e -> c
- c -> d -> e -> f -> b -> a -> c
- c -> e -> f -> b -> a -> d -> c

<!-- slide vertical=true data-notes="" -->

##### 状态空间树

---

@import "../dot/hamilton1.dot" {.left75per}

<div class="top-26per"></div>

@import "../dot/hamilton1-solution-space.dot" {.left8}

<div class="top0"></div>

- a -> b -> c -> e -> d -> a
- a -> d -> e -> c -> b -> a

<!-- slide vertical=true data-notes="" -->

##### 哈密顿回路 回溯实现

---

@import "../codes/hamilton.py" {line_begin=0 line_end=48 .left4 .line-numbers .top0}
