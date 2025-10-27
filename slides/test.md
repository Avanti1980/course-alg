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

##### 整数乘法

---

输入：两个$n$位整数$x$和$y$

<div class="top-2"></div>

输出：$x \cdot y$

小学算法：$x$和$y$的每一位相乘再相加

@import "../img/multiplication.svg" {.right20 .lefta .width15 .top-20}

<!-- slide vertical=true data-notes="" -->

##### 小学算法 实现

---

@import "../codes/integer-multiplication.py" {line_begin=9 line_end=35 .left4 .line-numbers .top0 highlight=[4,7]}

<!-- slide vertical=true data-notes="" -->

##### 整数乘法 小学算法

---

$x$和$y$的每一位相乘再相加

- $x$和$y$的一位相乘最多需$n$次乘法、$n$次加法
- $y$有$n$位，最多需$n^2$次乘法、$n^2$次加法
- $n$个$2n$位数相加，最多需$2 n^2$次加法

<div class="top2"></div>

综上共需$n^2$次乘法、$3 n^2$次加法，对应代码中的二重 for 循环

<p class="fragment top2">若$n$翻倍，计算量翻$4$倍，更好的算法？</p>

<!-- slide data-notes="" -->

##### <span style="font-weight:900">Karatsuba</span>算法

---

将$x$和$y$的数位二等分，分别相乘

$$
\begin{align*}
    \quad x & = ab = a \cdot 10^{n/2} + b \\
    y & = cd = c \cdot 10^{n/2} + d
\end{align*}
$$

<div class="top-4"></div>

其中$a$、$b$、$c$、$d$均是$n/2$位数

$$
\begin{align*}
    \quad x \cdot y & = a \cdot c \cdot 10^n + (a \cdot d + b \cdot c) 10^{n/2} + b \cdot d \\
    & = a \cdot c \cdot 10^n + ((a+b) \cdot (c+d) - a \cdot c - b \cdot d) 10^{n/2} + b \cdot d
\end{align*}
$$

<p class="fragment">$n$位数相乘 => $3$个$n/2$位数相乘：$a \cdot c$、$b \cdot d$、$(a+b) \cdot (c+d)$</p>

<p class="fragment">原问题：$n$位数相乘 => $3$个$n/2$位数相乘的子问题，递归实现</p>

<!-- slide vertical=true data-notes="" -->

##### <span style="font-weight:900">Karatsuba</span>算法 实现

---

@import "../codes/integer-multiplication.py" {line_begin=37 .left4 .line-numbers .top0 highlight=[17-19,36]}

<!-- slide vertical=true data-notes="" -->

##### <span style="font-weight:900">Karatsuba</span>算法 时间

---

原问题：$n$位数相乘 => $3$个$n/2$位数相乘的子问题，递归实现

设$n$位数相乘的时间为$T(n)$，则有递推式

$$
\begin{align*}
    \quad T(n) = 3 \cdot T \left( \frac{n}{2} \right) + \underbrace{\Theta(n)}_{\text{加法}}
\end{align*}
$$

根据{==主方法==}可得$T(n) \in \Theta(n^{\log_2 3})$

<!-- slide vertical=true data-notes="" -->

##### 整数乘法 时间对比

---

@import "../codes/integer-multiplication.svg" {.center .width70 .top2 .bottom-4}
