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

##### 编辑距离

---

将一个序列转换成另一个所需的最少的{==插入==}/{==删除==}/{==替换==}次数

$X = \langle A, B, C, B, D, A, B \rangle$、$Y = \langle B, D, C, A, B, A \rangle$

对$X$进行$3$次删除、$2$次插入可以得到$Y$

<div class="left4 twolines column1-border1-right-solid-head row1-column1-border1-right-solid column2-border1-right-solid-head row1-column2-border1-right-solid column4-border1-right-solid-head row1-column4-border1-right-solid column5-border1-right-solid-head row1-column5-border1-right-solid column6-border1-right-solid-head row1-column6-border1-right-solid column8-border1-right-solid-head row1-column8-border1-right-solid top-2">

|   A    |  B  |   C    |   B    |  D  | &nbsp; |  A  |  B  | &nbsp; |
| :----: | :-: | :----: | :----: | :-: | :----: | :-: | :-: | :----: |
| &nbsp; |  B  | &nbsp; | &nbsp; |  D  |   C    |  A  |  B  |   A    |

</div>

对$X$进行$2$次删除、$2$次替换、$1$次插入可以得到$Y$

<div class="left4 twolines column1-border1-right-solid-head row1-column1-border1-right-solid column2-border1-right-solid-head row1-column2-border1-right-solid column3-border1-right-solid-head row1-column3-border1-right-solid column7-border1-right-solid-head row1-column7-border1-right-solid column5-border1-right-solid-head row1-column5-border1-right-solid top-2">

|   A    |  B  |   C    |  B  |  D  |  A  |  B  | &nbsp; |
| :----: | :-: | :----: | :-: | :-: | :-: | :-: | :----: |
| &nbsp; |  B  | &nbsp; |  D  |  C  |  A  |  B  |   A    |

</div>

<!-- slide vertical=true data-notes="" -->

##### 编辑距离

---

$X$、$Y$各插入一些空格变成等长，然后以某种方式对齐，产生的最少的不相同的列数就是编辑距离

最优子结构性：将$X$、$Y$按编辑距离的方式对齐后，去掉最后一列，剩余列的对齐方式依然是前缀的编辑距离

记$c[i,j]$为$X_i$和$Y_j$的编辑距离

最后一列分 3 种情况：

- 删除：$x_m$对空格，$c[i,j] = c[i-1,j] + 1$
- 插入：空格对$y_n$，$c[i,j] = c[i,j-1] + 1$
- 替换：$x_m$对$y_n$，$c[i,j] = c[i-1,j-1] + \Ibb(x_m \neq y_n)$，其中$\Ibb(\cdot)$为指示函数

<div class="left52per twolines column1-border1-right-solid-head row1-column1-border1-right-solid column2-border1-right-solid-head row1-column2-border1-right-solid column3-border1-right-solid-head row1-column3-border1-right-solid column7-border1-right-solid-head row1-column7-border1-right-solid column5-border1-right-solid-head row1-column5-border1-right-solid top-32per">

|   A    |  B  |   C    |  B  |  D  |  A  |  B  | &nbsp; |
| :----: | :-: | :----: | :-: | :-: | :-: | :-: | :----: |
| &nbsp; |  B  | &nbsp; |  D  |  C  |  A  |  B  |   A    |

</div>

<!-- slide vertical=true data-notes="" -->

##### 编辑距离 递推关系

---

记$c[i,j]$为$X_i$和$Y_j$的编辑距离

最后一列分 3 种情况：

- 删除：$x_m$对空格，$c[i,j] = c[i-1,j] + 1$
- 插入：空格对$y_n$，$c[i,j] = c[i,j-1] + 1$
- 替换：$x_m$对$y_n$，$c[i,j] = c[i-1,j-1] + \Ibb(x_m \neq y_n)$，其中$\Ibb(\cdot)$为指示函数

<div class="top2"></div>

3 种情况取最小即为最优

$$
\begin{align*}
    \quad c[i,j] = \begin{cases} i, & j = 0 \\ j, & i = 0 \\ \min \left\{ c[i-1,j] + 1, \\ c[i,j-1] + 1, \\ \begin{array}{l} c[i-1,j-1] + \Ibb(x_m \neq y_n), \end{array} \right\} & \ow \end{cases}
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 编辑距离 实现

---

@import "../codes/edit-distance.py" {line_begin=3 line_end=74 .left4 .line-numbers .top-1}
