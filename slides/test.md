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

##### 最大子数组问题

---

某股票 17 天内的价格

<div class="threelines tighttable top-2">

|  天  |   0    |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10  | 11  | 12  | 13  | 14  | 15  | 16  |
| :--: | :----: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| 价格 |  100   | 113 | 110 | 85  | 105 | 102 | 86  | 63  | 81  | 101 | 94  | 106 | 101 | 79  | 94  | 90  | 97  |
| 变化 | &zwnj; | 13  | -3  | -25 | 20  | -3  | -16 | -23 | 18  | 20  | -7  | 12  | -5  | -22 | 15  | -4  |  7  |

</div>

问题：哪天买进、哪天卖出，收益最大？
