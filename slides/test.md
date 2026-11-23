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

##### 各问题复杂度一览

---

<div class="threelines tighttable">

| 问题                  |   子问题数    | 子问题时间复杂度 |    时间复杂度     |  空间复杂度   |
| :-------------------- | :-----------: | :--------------: | :---------------: | :-----------: |
| 费波拿契数            |  $\Theta(n)$  |   $\Theta(n)$    |   $\Theta(n^2)$   |  $\Theta(n)$  |
| 钢条切割              |  $\Theta(n)$  |   $\Theta(n)$    |   $\Theta(n^2)$   |  $\Theta(n)$  |
| 矩阵连乘              | $\Theta(n^2)$ |   $\Theta(n)$    |   $\Theta(n^3)$   | $\Theta(n^2)$ |
| 最优二叉搜索树        | $\Theta(n^2)$ |   $\Theta(n)$    |   $\Theta(n^3)$   | $\Theta(n^2)$ |
| 最长公共子序列        | $\Theta(mn)$  |   $\Theta(1)$    |   $\Theta(mn)$    | $\Theta(mn)$  |
| 编辑距离              | $\Theta(mn)$  |   $\Theta(1)$    |   $\Theta(mn)$    | $\Theta(mn)$  |
| 最长递增子序列        |  $\Theta(n)$  |   $\Theta(n)$    |   $\Theta(n^2)$   |  $\Theta(n)$  |
| 最长递增子序列 (改进) |  $\Theta(n)$  | $\Theta(\lg n)$  | $\Theta(n \lg n)$ |  $\Theta(n)$  |
| 最大子数组 (分治)     |  $\Theta(n)$  |   $\Theta(1)$    |    $\Theta(n)$    |  $\Theta(1)$  |
| 最大子数组 (动态规划) |  $\Theta(n)$  |   $\Theta(1)$    |    $\Theta(n)$    |  $\Theta(1)$  |
| 子集和数 (分治)       | $\Theta(2^n)$ |   $\Theta(1)$    |   $\Theta(2^n)$   |  $\Theta(1)$  |
| 子集和数 (动态规划)   | $\Theta(nM)$  |   $\Theta(1)$    |   $\Theta(nM)$    | $\Theta(nM)$  |

</div>
