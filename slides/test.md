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

##### <span style="font-weight:900">0/1</span>背包问题

---

设背包承重量为 10，各物品价值如下，求可装包最大价值子集

<div class="left8 righta top-2 threelines">

|    &ensp;    | 物品 1 | 物品 2 | 物品 3 | 物品 4 |
| :----------: | :----: | :----: | :----: | :----: |
|     重量     |   4    |   7    |   5    |   3    |
|     价值     |   40   |   42   |   25   |   12   |
| 单位重量价值 |   10   |   6    |   5    |   4    |

</div>

解的形式：$(x_1, x_2, x_3, x_4)$，其中$x_i$表示是否选择该物品

显式条件：$x_i \in \{1,0\}$

隐式条件：$4 x_1 + 7 x_2 + 5 x_3 + 3 x_4 \le 10$

<!-- slide vertical=true data-notes="" -->

##### 背包问题

---

<div class="left8 righta top-2 threelines">

| &ensp; | 物品 1 | 物品 2 | 物品 3 | 物品 4 |
| :----: | :----: | :----: | :----: | :----: |
|  重量  |   4    |   7    |   5    |   3    |
|  价值  |   40   |   42   |   25   |   12   |
|  单价  |   10   |   6    |   5    |   4    |

</div>

这是最大化问题，考虑上界，对任意部分解，上界为：已选物品总价值 + 剩余承重量全部采用剩余物品中单位重量价值最大的物品的总价值

- 初始所有分量都未确定，价值上界 = 10 × 10 = 100
- 若选物品 1，价值上界 = 40 + 6 × 6 = 76，潜力更大
- 若不选物品 1，价值上界 = 6 × 10 = 60

<!-- slide vertical=true data-notes="" -->

##### 背包问题

---

<div class="left4 righta top-2 threelines">

| &ensp; | 物品 1 | 物品 2 | 物品 3 | 物品 4 |
| :----: | :----: | :----: | :----: | :----: |
|  重量  |   4    |   7    |   5    |   3    |
|  价值  |   40   |   42   |   25   |   12   |
|  单价  |   10   |   6    |   5    |   4    |

</div>

@import "../dot/bag.dot" {.center .top0 .bottom-10}
