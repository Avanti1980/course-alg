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

##### <span style="font-weight:900">n</span>-皇后问题 分支限界

---

分支限界每步对下一个 E-结点的选择过于死板

结点 22 明明离答案结点 31 一步之遥，却又向右兜了个大圈子

问题一：聪明地选择 E-结点？

@import "../dot/four-queen-bb-solve11.dot" {.center .top0 .bottom-10}

<!-- slide data-notes="" -->

##### <span style="font-weight:900">n</span>-皇后问题 分支限界

---

目前看，回溯和分支限界的区别就是{==状态空间树的生长策略==}

问题二：对 n-皇后问题，分支是分支了，限界在哪里？

<div class="top4"></div>

n-皇后问题不是最优化问题，没体现出“限界”的意味

对于最优化问题

- 维护当前已知最优结点对应的目标函数值
- 对确定了部分分量的解，若能{==估计==}其在目标函数上的{==边界==}，与当前已知的最优目标函数值比较，可剪枝铁定没希望成为最优解的结点

<!-- slide data-notes="" -->

##### 分派问题

---

$4$个任务分派给$4$个人，每个任务恰只分派给一个人

每个任务分派给每个人的成本见下表，求成本最小的分派方案

<div class="left8 righta top-2 tighttable row1-4-column2-5-fullborder">

|    &ensp;     | 任务 1 | 任务 2 | 任务 3 | 任务 4 |
| :-----------: | :----: | :----: | :----: | :----: |
| 人员 1 &zwnj; |   9    |   2    |   7    |   8    |
| 人员 2 &zwnj; |   6    |   4    |   3    |   7    |
| 人员 3 &zwnj; |   5    |   8    |   1    |   8    |
| 人员 4 &zwnj; |   7    |   6    |   9    |   4    |

</div>

解的形式：$(x_1, x_2, x_3, x_4)$，其中$x_i$表示第$i$个人被分派的任务

显式条件：$x_i \in \{1,2,3,4\}$，隐式条件：解是$\{1,2,3,4\}$的置换

<!-- slide vertical=true data-notes="" -->

##### 分派问题

---

<div class="left8 righta top-2 tighttable row1-4-column2-5-fullborder">

|    &ensp;     | 任务 1 | 任务 2 | 任务 3 | 任务 4 |
| :-----------: | :----: | :----: | :----: | :----: |
| 人员 1 &zwnj; |   9    |   2    |   7    |   8    |
| 人员 2 &zwnj; |   6    |   4    |   3    |   7    |
| 人员 3 &zwnj; |   5    |   8    |   1    |   8    |
| 人员 4 &zwnj; |   7    |   6    |   9    |   4    |

</div>

这是最小化问题，我们考虑下界，对任一确定了部分分量的解，其下界为：已分派任务的成本和 + 剩余每行的最小值

- 初始所有分量都未确定，成本下界 = 2 + 3 + 1 + 4 = 10
- 若第一个人分派任务 1，成本下界 = 9 + 3 + 1 + 4 = 17
- 若第一个人分派任务 2，成本下界 = 2 + 3 + 1 + 4 = 10
- 若第一个人分派任务 3，成本下界 = 7 + 4 + 5 + 4 = 20
- 若第一个人分派任务 4，成本下界 = 8 + 3 + 1 + 6 = 18

<!-- slide vertical=true data-notes="" -->

##### 分派问题

---

<div class="left8 righta top-2 tighttable row1-4-column2-5-fullborder">

|    &ensp;     | 任务 1 | 任务 2 | 任务 3 | 任务 4 |
| :-----------: | :----: | :----: | :----: | :----: |
| 人员 1 &zwnj; |   9    |   2    |   7    |   8    |
| 人员 2 &zwnj; |   6    |   4    |   3    |   7    |
| 人员 3 &zwnj; |   5    |   8    |   1    |   8    |
| 人员 4 &zwnj; |   7    |   6    |   9    |   4    |

</div>

@import "../dot/job-distribution.dot"

在得到左下角的 13 后，其它活结点可以全部杀死
