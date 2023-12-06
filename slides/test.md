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

##### 分数背包问题

---

设背包承重量为$2$，允许物品按比例取走部分，求最大装包方案

<div class="left6 righta top-2 threelines">

| &ensp; | 物品$1$ | 物品$2$ |
| :----: | :-----: | :-----: |
|  重量  |   $1$   |   $3$   |
|  价值  |   $3$   |   $6$   |

</div>

设物品$1$和物品$2$取走的比例分别为$x_1$和$x_2$

$$
\begin{align*}
    \quad \max & \quad 3 x_1 + 6 x_2 \\
    \st        & \quad x_1 + 3 x_2 \le 2 \\
               & \quad 0 \le x_1 \le 1 \\
               & \quad 0 \le x_2 \le 1
\end{align*}
$$

这是一个线性规划问题

<!-- slide vertical=true data-notes="" -->

##### 线性规划标准形式

---

所有线性规划问题都可等价变形成标准形式

- 目标必须是最大化一个线性函数
- 所有约束都是等式约束
- 所有变量非负

<div class="top2"></div>

引入非负变量$x_3,x_4,x_5$

$$
\begin{align*}
    \quad \max & \quad 3 x_1 + 6 x_2 \\
    \st        & \quad x_1 + 3 x_2 + x_3 = 2 \\
               & \quad x_1 + x_4 = 1 \\
               & \quad x_2 + x_5 = 1 \\
               & \quad 0 \le x_1, x_2, x_3, x_4, x_5
\end{align*}
$$

<!-- slide data-notes="" -->

##### 单纯形法

---

根据问题画出{==单纯形表==} (simplex tableau)

<div class="left4 righta top-2 row1-border-top-solid row4-border-top-dashed column1-border-right-solid column6-border-right-dashed">

| &ensp; | $x_1$ | $x_2$ | $x_3$ | $x_4$ | $x_5$ | &ensp; |
| :----: | :---: | :---: | :---: | ----- | ----- | ------ |
| $x_3$  |  $1$  |  $3$  |  $1$  | $0$   | $0$   | $2$    |
| $x_4$  |  $1$  |  $0$  |  $0$  | $1$   | $0$   | $1$    |
| $x_5$  |  $0$  |  $1$  |  $0$  | $0$   | $1$   | $1$    |
| &ensp; | $-3$  | $-6$  |  $0$  | $0$   | $0$   | $0$    |

</div>

- $5$个变量，$3$个等式约束，有$2$个变量是自由的，称为{==非基本变量==}
- 对{==非基本变量==}赋值，剩下的{==基本变量==}(单纯形表最左列)有唯一解
- 令$x_{\{1,2\}} = 0$，求解$x_{\{3,4,5\}}$得{==基本可行解==}$[0,0,2,1,1]$
- 单纯形表最后一行称为{==目标行==}，初始为目标函数的系数，符号取反，最后一格为当前{==基本可行解==}$[0,0,2,1,1]$对应的目标函数值$0$

<div class="top-42per"></div>

$$
\begin{align*}
    \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \max & \quad 3 x_1 + 6 x_2 \\
    \st        & \quad x_1 + 3 x_2 + x_3 = 2 \\
               & \quad x_1 + x_4 = 1 \\
               & \quad x_2 + x_5 = 1 \\
               & \quad 0 \le x_1, x_2, x_3, x_4, x_5
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 迭代改进

---

根据问题画出{==单纯形表==} (simplex tableau)

<div class="left4 righta top-2 row1-border-top-solid row4-border-top-dashed column1-border-right-solid column6-border-right-dashed">

| &ensp; | $x_1$ | $x_2$ | $x_3$ | $x_4$ | $x_5$ | &ensp; |
| :----: | :---: | :---: | :---: | ----- | ----- | ------ |
| $x_3$  |  $1$  |  $3$  |  $1$  | $0$   | $0$   | $2$    |
| $x_4$  |  $1$  |  $0$  |  $0$  | $1$   | $0$   | $1$    |
| $x_5$  |  $0$  |  $1$  |  $0$  | $0$   | $1$   | $1$    |
| &ensp; | $-3$  | $-6$  |  $0$  | $0$   | $0$   | $0$    |

</div>

基本可行解$[0,0,2,1,1]$不是最优的，适当增加$x_1$可以增大目标函数值
