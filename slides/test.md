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

##### <span style="font-weight:900">0/1</span>背包问题

---

设背包承重量为 10，各物品价值如下，求可装包最大价值子集

<div class="left6 righta top-2 threelines">

| &ensp; | 物品 1 | 物品 2 | 物品 3 | 物品 4 |
| :----: | :----: | :----: | :----: | :----: |
|  重量  |   4    |   7    |   5    |   3    |
|  价值  |   40   |   42   |   25   |   12   |
|  单价  |   10   |   6    |   5    |   4    |

</div>

解的形式：$(x_1, x_2, x_3, x_4)$，其中$x_i$表示是否选择该物品

显式条件：$x_i \in \{1,0\}$

隐式条件：$4 x_1 + 7 x_2 + 5 x_3 + 3 x_4 \le 10$

<!-- slide vertical=true data-notes="" -->

##### <span style="font-weight:900">0/1</span>背包问题

---

<div class="left6 righta top-2 threelines">

| &ensp; | 物品 1 | 物品 2 | 物品 3 | 物品 4 |
| :----: | :----: | :----: | :----: | :----: |
|  重量  |   4    |   7    |   5    |   3    |
|  价值  |   40   |   42   |   25   |   12   |
|  单价  |   10   |   6    |   5    |   4    |

</div>

对任一确定了部分分量的解

- 上界：已选物品总价值 + 剩余承重量采用单价最大的物品的总价值
- 下界：已选物品总价值

<div class="top2"></div>

例如：若选了物品 1

- 价值上界 = 40 + 6 × 6 = 76
- 价值下界 = 40

<!-- slide vertical=true data-notes="" -->

##### <span style="font-weight:900">0/1</span>背包问题

---

<div class="left4 righta top-2 threelines">

| &ensp; | 物品 1 | 物品 2 | 物品 3 | 物品 4 |
| :----: | :----: | :----: | :----: | :----: |
|  重量  |   4    |   7    |   5    |   3    |
|  价值  |   40   |   42   |   25   |   12   |
|  单价  |   10   |   6    |   5    |   4    |

</div>

@import "../dot/bag.dot" {.right4 .lefta .top-28per}

<div class="top-4"></div>

部分解 (1, 0, 1, -) 下界 65，可剪枝上界为 60、64 的两个活结点


