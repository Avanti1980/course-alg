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

##### 一些术语

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
    \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \max & \quad 3 x_1 + 6 x_2 \\
    \st        & \quad x_1 + 3 x_2 + x_3 = 2 \\
               & \quad x_1 + x_4 = 1 \\
               & \quad x_2 + x_5 = 1 \\
               & \quad 0 \le x_1, x_2, x_3, x_4, x_5
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 单步改进

---

<div class="left4 righta top-2 bottom-2 row1-border-top-solid row4-border-top-dashed column1-border-right-solid column6-border-right-dashed">

| &ensp; | $x_1$ | $x_2$ | $x_3$ | $x_4$ | $x_5$ | &ensp; |
| :----: | :---: | :---: | :---: | ----- | ----- | ------ |
| $x_3$  |  $1$  |  $3$  |  $1$  | $0$   | $0$   | $2$    |
| $x_4$  |  $1$  |  $0$  |  $0$  | $1$   | $0$   | $1$    |
| $x_5$  |  $0$  |  $1$  |  $0$  | $0$   | $1$   | $1$    |
| &ensp; | $-3$  | $-6$  |  $0$  | $0$   | $0$   | $0$    |

</div>

$[0,0,2,1,1]$不是最优的，适当增大$x_1$或$x_2$可以增大目标函数值

$x_1$须满足$\begin{cases} x_1 + x_3 = 2, ~ x_3 \ge 0 \\ x_1 + x_4 = 1, ~ x_4 \ge 0 \end{cases} \Longrightarrow x_1 \le \min (2,1) = 1$

增大$x_1$至$1$得新基本可行解$[1,0,1,0,1]$，目标函数值为$3$

<!-- slide vertical=true data-notes="" -->

##### 单步改进

---

<div class="left4 righta top-2 bottom-2 row1-border-top-solid row4-border-top-dashed column1-border-right-solid column6-border-right-dashed">

| &ensp; | $x_1$ | $x_2$ | $x_3$ | $x_4$ | $x_5$ | &ensp; |
| :----: | :---: | :---: | :---: | ----- | ----- | ------ |
| $x_3$  |  $1$  |  $3$  |  $1$  | $0$   | $0$   | $2$    |
| $x_4$  |  $1$  |  $0$  |  $0$  | $1$   | $0$   | $1$    |
| $x_5$  |  $0$  |  $1$  |  $0$  | $0$   | $1$   | $1$    |
| &ensp; | $-3$  | $-6$  |  $0$  | $0$   | $0$   | $0$    |

</div>

$[0,0,2,1,1]$不是最优的，适当增大$x_1$或$x_2$可以增大目标函数值

$x_2$须满足$\begin{cases} 3 x_2 + x_3 = 2, ~ x_3 \ge 0 \\ x_2 + x_5 = 1, ~ x_5 \ge 0 \end{cases} \Longrightarrow x_2 \le \min (\frac{2}{3},1) = \frac{2}{3}$

增大$x_2$至$\frac{2}{3}$得新基本可行解$[0,\frac{2}{3},0,1,\frac{1}{3}]$，目标函数值为$4$

<!-- slide vertical=true data-notes="" -->

##### 单步改进

---

<div class="left4 righta top-2 bottom-2 row1-border-top-solid row4-border-top-dashed column1-border-right-solid column6-border-right-dashed">

| &ensp; | $x_1$ | $x_2$ | $x_3$ | $x_4$ | $x_5$ | &ensp; |
| :----: | :---: | :---: | :---: | ----- | ----- | ------ |
| $x_3$  |  $1$  |  $3$  |  $1$  | $0$   | $0$   | $2$    |
| $x_4$  |  $1$  |  $0$  |  $0$  | $1$   | $0$   | $1$    |
| $x_5$  |  $0$  |  $1$  |  $0$  | $0$   | $1$   | $1$    |
| &ensp; | $-3$  | $-6$  |  $0$  | $0$   | $0$   | $0$    |

</div>

$[0,0,2,1,1]$不是最优的，适当增大$x_1$或$x_2$可以增大目标函数值

目标行中的负元素指示着调整哪些变量：$-3 \rightarrow x_1$，$-6 \rightarrow x_2$

取目标行中{==绝对值最大的负元素==}指示的变量进行调整 ({==主元列==})

- $x_2$：{==输入变量==}，非基本变量 => 基本变量
- $x_3$：{==分离变量==}，基本变量 => 非基本变量

<!-- slide data-notes="" -->

##### 主元化

---

<div class="left4 righta top-2 bottom-2 row1-border-top-solid row4-border-top-dashed column1-border-right-solid column6-border-right-dashed">

| &ensp; | $x_1$ | $\class{blue}{x_2}$ | $x_3$ | $x_4$ | $x_5$ | &ensp; |
| :----: | :---: | :-----------------: | :---: | ----- | ----- | ------ |
| $x_3$  |  $1$  |         $3$         |  $1$  | $0$   | $0$   | $2$    |
| $x_4$  |  $1$  |         $0$         |  $0$  | $1$   | $0$   | $1$    |
| $x_5$  |  $0$  |         $1$         |  $0$  | $0$   | $1$   | $1$    |
| &ensp; | $-3$  | $\class{blue}{-6}$  |  $0$  | $0$   | $0$   | $0$    |

</div>

如何确定{==输入变量==}？目标行中{==绝对值最大的负元素==}指示的变量

如何确定{==分离变量==}？

1. 对主元列上每个正元素，计算$\theta$比值：$\theta_3 = 2/3$、$\theta_5 = 1/1$，$\theta_4$无需计算
2. $\theta_i$的物理意义：保证$x_i$非负的前提下，输入变量的最大变化量
3. 若$\theta_i$最小，则$x_i$为分离变量(瓶颈所在)，对应行为{==主元行==}，主元行和主元列的交叉元素为{==主元==}
4. 主元行的所有元素处以主元，将主元变成$1$

<!-- slide vertical=true data-notes="" -->

##### 主元化

---

<div class="left4 righta top-2 bottom-2 row1-border-top-solid row4-border-top-dashed column1-border-right-solid column6-border-right-dashed">

|       &ensp;       |     $x_1$     | $\class{blue}{x_2}$ |     $x_3$     | $x_4$ | $x_5$ | &ensp;        |
| :----------------: | :-----------: | :-----------------: | :-----------: | ----- | ----- | ------------- |
| $\class{red}{x_3}$ | $\frac{1}{3}$ |         $1$         | $\frac{1}{3}$ | $0$   | $0$   | $\frac{2}{3}$ |
|       $x_4$        |      $1$      |         $0$         |      $0$      | $1$   | $0$   | $1$           |
|       $x_5$        |      $0$      |         $1$         |      $0$      | $0$   | $1$   | $1$           |
|       &ensp;       |     $-3$      | $\class{blue}{-6}$  |      $0$      | $0$   | $0$   | $0$           |

</div>

做{==初等行变换==}：减去主元行的若干倍，把主元列都变成$0$

<div class="left4 righta top-2 bottom-2 row1-border-top-solid row4-border-top-dashed column1-border-right-solid column6-border-right-dashed">

| &ensp; |     $x_1$      | $x_2$ |     $x_3$      | $x_4$ | $x_5$ | &ensp;        |
| :----: | :------------: | :---: | :------------: | ----- | ----- | ------------- |
| $x_2$  | $\frac{1}{3}$  |  $1$  | $\frac{1}{3}$  | $0$   | $0$   | $\frac{2}{3}$ |
| $x_4$  |      $1$       |  $0$  |      $0$       | $1$   | $0$   | $1$           |
| $x_5$  | $-\frac{1}{3}$ |  $0$  | $-\frac{1}{3}$ | $0$   | $1$   | $\frac{1}{3}$ |
| &ensp; |      $-1$      |  $0$  |      $2$       | $0$   | $0$   | $4$           |

</div>

<div class="top-50per left52per righta fs18">

$\frac{2}{3} = \theta_3 < \theta_5 = 1$

$x_2$输入变量，$x_3$分离变量

</div>

<div class="top20per left52per righta fs18">

新基本可行解$[0,\frac{2}{3},0,1,\frac{1}{3}]$

对应目标函数值为$4$

$-1 \rightarrow x_1$将作为输入变量

</div>

<!-- slide vertical=true data-notes="" -->

##### 主元化

---

<div class="left4 righta top-2 bottom-2 row1-border-top-solid row4-border-top-dashed column1-border-right-solid column6-border-right-dashed">

|       &ensp;       | $\class{blue}{x_1}$ | $x_2$ |     $x_3$      | $x_4$ | $x_5$ | &ensp;        |
| :----------------: | :-----------------: | :---: | :------------: | ----- | ----- | ------------- |
|       $x_2$        |    $\frac{1}{3}$    |  $1$  | $\frac{1}{3}$  | $0$   | $0$   | $\frac{2}{3}$ |
| $\class{red}{x_4}$ |         $1$         |  $0$  |      $0$       | $1$   | $0$   | $1$           |
|       $x_5$        |   $-\frac{1}{3}$    |  $0$  | $-\frac{1}{3}$ | $0$   | $1$   | $\frac{1}{3}$ |
|       &ensp;       |        $-1$         |  $0$  |      $2$       | $0$   | $0$   | $4$           |

</div>

$\theta_2 = 2$、$\theta_4=1$，$x_4$为分离变量

<div class="left4 righta top-2 bottom-2 row1-border-top-solid row4-border-top-dashed column1-border-right-solid column6-border-right-dashed">

| &ensp; | $x_1$ | $x_2$ |     $x_3$      | $x_4$          | $x_5$ | &ensp;        |
| :----: | :---: | :---: | :------------: | -------------- | ----- | ------------- |
| $x_2$  |  $0$  |  $1$  | $\frac{1}{3}$  | $-\frac{1}{3}$ | $0$   | $\frac{1}{3}$ |
| $x_1$  |  $1$  |  $0$  |      $0$       | $1$            | $0$   | $1$           |
| $x_5$  |  $0$  |  $0$  | $-\frac{1}{3}$ | $\frac{1}{3}$  | $1$   | $\frac{2}{3}$ |
| &ensp; |  $0$  |  $0$  |      $2$       | $1$            | $0$   | $5$           |

</div>

<div class="top-20per left52per righta fs18">

新基本可行解$[1,\frac{1}{3},0,0,\frac{2}{3}]$

对应目标函数值为$5$

目标行无负元素，当前解即为最优解

</div>

<!-- slide data-notes="" -->

##### 分数背包问题 贪心

---

<div class="left6 righta top-2 threelines">

| &ensp; | 物品$1$ | 物品$2$ |
| :----: | :-----: | :-----: |
|  重量  |   $1$   |   $3$   |
|  价值  |   $3$   |   $6$   |

</div>

最优解：$x_1 = 1$、$x_2 = \frac{1}{3}$

我的启示 物品$1$单价大，优先装，装完后剩余重量全部用于装物品$2$

<div class="top-32per"></div>

$$
\begin{align*}
    \qquad \qquad \qquad \qquad \qquad \qquad \max & \quad 3 x_1 + 6 x_2 \\
    \st        & \quad x_1 + 3 x_2 \le 2 \\
               & \quad 0 \le x_1 \le 1 \\
               & \quad 0 \le x_2 \le 1
\end{align*}
$$
