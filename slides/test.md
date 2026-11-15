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

<!-- slide data-notes="" -->

##### 构造最优解

---

$s[i,j]$表示$\Av_i \cdots \Av_j$的最优分开位置

- $s[1,6]=3$，故$\Av_1 \cdots \Av_6$在$\Av_3$后分开
- $s[1,3]=1$，故$\Av_1 \cdots \Av_3$在$\Av_1$后分开
- $s[4,6]=5$，故$\Av_4 \cdots \Av_6$在$\Av_5$后分开

<div class="top2"></div>

最优方案：$(\Av_1 (\Av_2 \Av_3)) ((\Av_4 \Av_5) \Av_6)$

@import "../codes/dp/matrix-chain.py" {line_begin=18 line_end=26 .left2 .line-numbers .top0 .bottom0}

<img src="../tikz/matrix-chain/matrix-chain-s.svg" class="width35 lefta right6 top-50per">
