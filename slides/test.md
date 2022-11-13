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

##### 最优二叉搜索树

---

场景：语言翻译，从英语到法语，对给定的单词，在单词表里找到该词

等等


方法：创建一棵二叉搜索树，以英语单词作为关键字构建树

目标：尽快地找到英语单词，使“总”的搜索时间尽量少

思路：频繁使用的单词，如the，应尽可能靠近根；而不经常出现的单词可以离根远一些

思考：如果反之会怎样？


