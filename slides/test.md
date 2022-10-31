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

##### <span style="font-weight:900">Strassen</span>矩阵乘法

---

<div class="top2"></div>

$$
\begin{align*}
    \quad T(n) & = \begin{cases} 1 & n = 1 \\ \class{blue}{a} \cdot T(n/2) + \class{blue}{c n^2} & n > 1 \end{cases} = n^{\lg a} \cdot T(1) + \frac{4c}{a-4} (n^{\lg a} - n^2)
\end{align*}
$$

<div class="top-2"></div>

我的启示 即便$f(n) = \Theta(n^2)$，只要$a < 8$，就可以改进时间复杂度

Strassen 乘法：通过多做小矩阵的加法，少做小矩阵的乘法

- 多做小矩阵的加法会增大$c$，但不影响，依然有$f(n) = \Theta(n^2)$
- 少做小矩阵的乘法可以减小$a$，从而改进时间复杂度

<div class="top2"></div>

直观例子

1. $x^2 - y^2 = (x+y)(x-y)$，前者 2 乘 1 加，后者 1 乘 2 加
2. $(a + b \text{i})(c + d \text{i}) = ac - bd + (ad + bc) \text{i} = ac - bd + ((a+b)(c+d) - ac - bd) \text{i}$，前者 4 乘 2 加，后者 3 乘 5 加

<!-- slide vertical=true data-notes="" -->

##### <span style="font-weight:900">Strassen</span>矩阵乘法

---

<div class="top2"></div>

$$
\begin{align*}
    \quad \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix} \begin{bmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{bmatrix} = \begin{bmatrix} a_{11} b_{11} + a_{12} b_{21} & a_{11} b_{12} + a_{12} b_{22} \\ a_{21} b_{11} + a_{22} b_{21} & a_{21} b_{12} + a_{22} b_{22} \end{bmatrix}
\end{align*}
$$

<div class="top-3"></div>

下面说明$2 \times 2$的矩阵相乘可以通过{==只做$7$次==}乘法实现

$$
\begin{align*}
    \quad \begin{bmatrix}
        a_{11} b_{11} + a_{12} b_{21} \\
        a_{11} b_{12} + a_{12} b_{22} \\
        a_{21} b_{11} + a_{22} b_{21} \\
        a_{21} b_{12} + a_{22} b_{22}
    \end{bmatrix} & =
    \begin{bmatrix}
        a_{11} & 0   & a_{12} & 0   \\
        0   & a_{11} & 0   & a_{12} \\
        a_{21} & 0   & a_{22} & 0   \\
        0   & a_{21} & 0   & a_{22}
    \end{bmatrix}
    \begin{bmatrix}
        b_{11} \\ b_{12} \\ b_{21} \\ b_{22}
    \end{bmatrix} \\[4px]
    & \triangleq \widetilde{\Av}
    \begin{bmatrix}
        b_{11} \\ b_{12} \\ b_{21} \\ b_{22}
    \end{bmatrix}
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### <span style="font-weight:900">Strassen</span>矩阵乘法

---

<div class="top2"></div>

$$
\begin{align*}
    \quad \begin{bmatrix}
        a_{11} b_{11} + a_{12} b_{21} \\
        a_{11} b_{12} + a_{12} b_{22} \\
        a_{21} b_{11} + a_{22} b_{21} \\
        a_{21} b_{12} + a_{22} b_{22}
    \end{bmatrix} =
    \begin{bmatrix}
        a_{11} & 0   & a_{12} & 0   \\
        0   & a_{11} & 0   & a_{12} \\
        a_{21} & 0   & a_{22} & 0   \\
        0   & a_{21} & 0   & a_{22}
    \end{bmatrix}
    \begin{bmatrix}
        b_{11} \\ b_{12} \\ b_{21} \\ b_{22}
    \end{bmatrix} \triangleq \widetilde{\Av}
    \begin{bmatrix}
        b_{11} \\ b_{12} \\ b_{21} \\ b_{22}
    \end{bmatrix}
\end{align*}
$$

<div class="top-3"></div>

假设$\widetilde{\Av} \in \Rbb^{4 \times 4}$可以分解成$m$个秩$1$矩阵的和

$$
\begin{align*}
    \quad \widetilde{\Av} = \begin{bmatrix}
        a_{11} & 0   & a_{12} & 0   \\
        0   & a_{11} & 0   & a_{12} \\
        a_{21} & 0   & a_{22} & 0   \\
        0   & a_{21} & 0   & a_{22}
    \end{bmatrix} = \sum_{i \in [m]} r_i
    \begin{bmatrix}
        p_{i1} \\ p_{i2} \\ p_{i3} \\ p_{i4}
    \end{bmatrix}
    \begin{bmatrix}
        q_{i1} \\ q_{i2} \\ q_{i3} \\ q_{i4}
    \end{bmatrix}^\top
\end{align*}
$$

- $r_i$只由$a_{11}, a_{12}, a_{21}, a_{22}$进行加减运算得到
- $p_{i1}, \ldots,p_{i4}, q_{i1}, \ldots, q_{i4} \in \{ \pm 1, 0 \}$

<!-- slide vertical=true data-notes="" -->

##### <span style="font-weight:900">Strassen</span>矩阵乘法

---

<div class="top2"></div>

$$
\begin{align*}
    \quad \begin{bmatrix}
        a_{11} b_{11} + a_{12} b_{21} \\
        a_{11} b_{12} + a_{12} b_{22} \\
        a_{21} b_{11} + a_{22} b_{21} \\
        a_{21} b_{12} + a_{22} b_{22}
    \end{bmatrix} & = \widetilde{\Av}
    \begin{bmatrix}
        b_{11} \\ b_{12} \\ b_{21} \\ b_{22}
    \end{bmatrix} = \sum_{i \in [m]} r_i 
    \begin{bmatrix}
        p_{i1} \\ p_{i2} \\ p_{i3} \\ p_{i4}
    \end{bmatrix}
    \begin{bmatrix}
        q_{i1} \\ q_{i2} \\ q_{i3} \\ q_{i4}
    \end{bmatrix}^\top
    \begin{bmatrix}
        b_{11} \\ b_{12} \\ b_{21} \\ b_{22}
    \end{bmatrix} \\
    & = \sum_{i \in [m]} r_i 
    \begin{bmatrix}
        p_{i1} \\ p_{i2} \\ p_{i3} \\ p_{i4}
    \end{bmatrix} s_i = \sum_{i \in [m]} t_i
    \begin{bmatrix}
        p_{i1} \\ p_{i2} \\ p_{i3} \\ p_{i4}
    \end{bmatrix} 
\end{align*}
$$

- $r_i$只由$a_{11}, a_{12}, a_{21}, a_{22}$加减得到，$p_{i1}, \ldots,p_{i4}, q_{i1}, \ldots, q_{i4} \in \{ \pm 1, 0 \}$
- $s_i = q_{i1} b_{11} + q_{i2} b_{12} + q_{i3} b_{21} + q_{i4} b_{22}$只由$b_{11}, b_{12}, b_{21}, b_{22}$加减得到
- 计算全部$m$个$t_i = r_i s_i$需做$m$次乘法。又$p_{i1}, \ldots, p_{i4} \in \{ \pm \Iv, \zerov \}$

<!-- slide vertical=true data-notes="" -->

##### <span style="font-weight:900">Strassen</span>矩阵乘法

---

sss

