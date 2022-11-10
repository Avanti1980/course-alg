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

1. 分析最优解的结构特征
2. 递归定义最优解的值
3. 根据递推关系{==自底向上==}，依次计算最优解的值
4. 若除最优解的值外还需最优解本身，在第 3 步里维护一些额外信息

<div class="top4"></div>

第 1 步就是判断{==最优子结构性==}是否成立

- 以$A[i]$作结尾的最大子数组依赖以$A[i-1]$作结尾的最大子数组
- 长度为$n$的钢条的最优切割方案依赖所有长度小于$n$的切割方案
- 长度为$n$的矩阵序列的加括号方案依赖所有长度小于$n$的加括号方案

<div class="top4"></div>

第 2 步就是给出{==递推关系式==}，也称{==状态转移方程==}

<!-- slide vertical=true data-notes="" -->

##### 最优子结构性成立

---

有向图上的无权最短路径具有最优子结构性

设$u \ne v$，$u$到$v$的最短路径为$p$，记为$u \overset{p}{\rightsquigarrow} v$

路径$p$上的中间结点$w$将$p$分为$p_1$、$p_2$两部分，$u \overset{p_1}{\rightsquigarrow} w \overset{p_2}{\rightsquigarrow} v$，则

- $p_1$是从$u$到$w$的最短路径，否则设$p'_1$更短，则$u \overset{p'_1}{\rightsquigarrow} w \overset{p_2}{\rightsquigarrow} v$也更短
- $p_2$是从$w$到$v$的最短路径，否则设$p'_2$更短，则$u \overset{p_1}{\rightsquigarrow} w \overset{p'_2}{\rightsquigarrow} v$也更短

<div class="top2"></div>

最优子结构性均可用上述反证法来证，书上称{==剪切-粘贴==}技术

1. 假设子问题的解不是其自身的最优解，最优解另有其解
2. 将该解{==剪掉==}，并将最优解{==粘进来==}，从而得到原问题的一个更优解
3. 这与最初的解是原问题的最优解矛盾

<!-- slide vertical=true data-notes="" -->

##### 最优子结构性不成立

---

有向图上的无权最长{==简单==}(无环)路径不具有最优子结构性

- ①->②->③ 是 ① 到 ③ 的一条最长路径
- ①->② 不是 ① 到 ② 的最长路径 (①->④->③->②)
- ②->③ 不是 ② 到 ③ 的最长路径 (②->①->④->③)
- ①->② 的最长路径连上 ②->③ 的最长路径不是简单路径

@import "../dot/longest-path.dot" {.left82per .top-18 .bottom2}

{==子问题无关性==}：同一个原问题的子问题之间相互独立

最短路径的两个子问题相互独立，$p_1$、$p_2$除$w$外没有公共点，否则设公共点为$x$，则$u \rightsquigarrow x \rightsquigarrow w \rightsquigarrow x \rightsquigarrow v$可优化为$u \rightsquigarrow x \rightsquigarrow v$

最长路径的两个子问题不独立，子问题 ① 到 ② 的最长路径经过的点，在子问题 ① 到 ③ 的最长路径中不能再经过
