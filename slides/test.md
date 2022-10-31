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

##### 矩阵加法

---

设$\Av = (a_{ij})_{n \times n}$、$\Bv = (b_{ij})_{n \times n}$为$n$阶方阵

设$\Cv  = (c_{ij})_{n \times n} = \Av + \Bv$，则$c_{ij} = a_{ij} + b_{ij}$

计算$\Cv = \Av + \Bv$的代码如下

@import "../codes/matrix-multiply.py" {line_begin=3 line_end=8 .left4 .line-numbers .top1 .bottom1}

因为二重 for 循环的存在，时间复杂度为$\Theta(n^2)$


<!-- slide data-notes="" -->

##### 矩阵乘法

---

设$\Av = (a_{ij})_{n \times n}$、$\Bv = (b_{ij})_{n \times n}$为$n$阶方阵

设$\Cv  = (c_{ij})_{n \times n} = \Av \Bv$，则$c_{ij} = \sum_{k=1}^n a_{ik} b_{kj}$

计算$\Cv = \Cv + \Av \Bv$的代码如下

@import "../codes/matrix-multiply.py" {line_begin=3 line_end=8 .left4 .line-numbers .top1 .bottom1}

因为三重 for 循环的存在，时间复杂度为$\Theta(n^3)$

<!-- slide data-notes="" -->

##### 矩阵乘法 递归版

---

将$\Av$、$\Bv$、$\Cv$分成$4$个分块矩阵，每块$n/2 \times n/2$

$$
\begin{align*}
    \quad \Av = \begin{bmatrix} \Av_{11} & \Av_{12} \\ \Av_{21} & \Av_{22} \end{bmatrix}, \quad \Bv = \begin{bmatrix} \Bv_{11} & \Bv_{12} \\ \Bv_{21} & \Bv_{22} \end{bmatrix}, \quad \Cv = \begin{bmatrix} \Cv_{11} & \Cv_{12} \\ \Cv_{21} & \Cv_{22} \end{bmatrix}
\end{align*}
$$

<div class="top-2"></div>

根据分块矩阵的运算法则

$$
\begin{align*}
    \quad \begin{bmatrix} \Cv_{11} & \Cv_{12} \\ \Cv_{21} & \Cv_{22} \end{bmatrix} & = \begin{bmatrix} \Av_{11} & \Av_{12} \\ \Av_{21} & \Av_{22} \end{bmatrix} \begin{bmatrix} \Bv_{11} & \Bv_{12} \\ \Bv_{21} & \Bv_{22} \end{bmatrix} \\[2px]
    & = \begin{bmatrix} \Av_{11} \Bv_{11} + \Av_{12} \Bv_{21} & \Av_{11} \Bv_{12} + \Av_{12} \Bv_{22} \\ \Av_{21} \Bv_{11} + \Av_{22} \Bv_{21} & \Av_{21} \Bv_{12} + \Av_{22} \Bv_{22} \end{bmatrix} \\[2px]
    \Longrightarrow & ~ \begin{cases} \Cv_{11} = \Av_{11} \Bv_{11} + \Av_{12} \Bv_{21} \\
    \Cv_{12} = \Av_{11} \Bv_{12} + \Av_{12} \Bv_{22} \\
    \Cv_{21} = \Av_{21} \Bv_{11} + \Av_{22} \Bv_{21} \\
    \Cv_{22} = \Av_{21} \Bv_{12} + \Av_{22} \Bv_{22} \end{cases}
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 矩阵乘法 递归版

---

@import "../codes/matrix-multiply.py" {line_begin=11 line_end=42 .left4 .line-numbers .top1 .bottom1}

<!-- slide data-notes="" -->

##### <span style="font-weight:900">Strassen</span>矩阵乘法

---
