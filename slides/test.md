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

##### 小结

---

动态规划一般步骤：

1. 分析最优解的结构特征 -> {==最优子结构性==}
2. 递归定义最优解的值 -> {==递推关系式==}，也称{==状态转移方程==}
3. 安排求解顺序，一般{==自底向上==}，依次计算最优解的值
4. 若除最优解的值外还需最优解本身，在第 3 步里维护一些额外信息

<div class="top2"></div>

子问题无关性：同一个原问题的子问题之间相互独立

最长简单路径问题

```dot
ss
```
