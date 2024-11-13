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

<!-- slide data-notes="" -->

##### 动态规划

---

动态规划是一种聪明的递归方式，不重复求解子问题

{==以空间换时间==}：时空权衡 (time-memory trade-off)

动态规划一般用来求解{==最优化==}问题：求问题的最大值、最小值

- {==最大==}收益的钢条切割方案
- {==最小==}开销的矩阵连乘方案
- {==最长==}公共子序列
- {==最长==}递增子序列
- {==最优==}二叉搜索树
- {==最大==}连续子数组

<!-- slide vertical=true data-notes="" -->

##### 动态规划 一般步骤

---

第一阶段：递归定义

1. 规约(specification)：用清晰的语言描述问题
2. 将问题的解用更小规模问题的解表示出来

<div class="top2"></div>

第二阶段：递推求解

1. 确定子问题，算法如何调用自己，初始参数？
2. 保存子问题结果的数据结构：数组、表格、……
3. 除边界条件外，子问题相互间的依赖关系(偏序)
4. 根据上一步的偏序确定子问题的求解顺序
5. 分析时空开销
6. 若除最优解的值外还需最优解本身，在第 2 步里维护一些额外信息
