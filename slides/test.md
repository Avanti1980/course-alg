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

##### 差分约束系统

---

假设一个生产工序有$n$个步骤，在时刻$x_i$进行第$i$个步骤

步骤的执行时间会有一些约束

在时刻$x_i$使用一种需要$2$个小时才能风干的粘贴剂材料

下一个步骤需要$2$小时后等粘贴剂干了才能在时刻$x_{i+1}$安装

这样就有约束条件$x_i - x_{i+1} \le -2$

<!-- slide vertical=true data-notes="" -->

##### 差分约束系统

---

把所有的约束条件写到一下就是差分约束系统

$$
\begin{align*}
    \quad \begin{cases}
        x_1 - x_2 \le 0 \\
        x_1 - x_5 \le -1 \\
        x_2 - x_5 \le 1 \\
        x_3 - x_1 \le 5 \\
        x_4 - x_1 \le 4 \\
        x_4 - x_3 \le -1 \\
        x_5 - x_3 \le -3 \\
        x_5 - x_4 \le -3
    \end{cases} \quad \Longleftrightarrow \quad
    \underbrace{\begin{bmatrix}
        1 & -1 & 0 & 0 & 0 \\
        1 & 0 & 0 & 0 & -1 \\
        0 & 1 & 0 & 0 & -1 \\
        -1 & 0 & 1 & 0 & 0 \\
        -1 & 0 & 0 & 1 & 0 \\
        0 & 0 & -1 & 1 & 0 \\
        0 & 0 & -1 & 0 & 1 \\
        0 & 0 & 0 & -1 & 1
    \end{bmatrix}}_{\Av ~ \in ~ \{ \pm 1, 0 \}^{m \times n}} \underbrace{\begin{bmatrix}
        x_1 \\ x_2 \\ x_3 \\ x_4 \\ x_5
    \end{bmatrix}}_{\xv ~ \in ~ \Rbb^n} \le \underbrace{\begin{bmatrix}
        0 \\ -1 \\ 1 \\ 5 \\ 4 \\ -1 \\ -3 \\ -3
    \end{bmatrix}}_{\bv ~ \in ~ \Rbb^m}
\end{align*}
$$

<div class="top-3"></div>

满足$\Av \xv \le \bv$的$\xv$称为差分约束系统的解

<div class="top-1"></div>

差分约束系统的解{==不唯一==}，若$\xv$是解，则$\xv + c \onev$也是解

<!-- slide data-notes="" -->

##### 约束图

---

给定差分约束系统$\Av \xv \le \bv$，其约束图是带权有向图$\Gcal = (\Vcal, \Ecal)$

- $\Vcal = \{ v_0, v_1, \ldots, v_n \}$，每个$x_i$对应一个$v_i$，此外引入一个额外的$v_0$
- $\Ecal = \{ (v_i, v_j) \mid x_j -x_i \le b_k \} \cup \{ (v_0, v_1), (v_0,v_2), \ldots, (v_0, v_n) \}$，每个约束对应一条边，边的权重就是$b_k$


