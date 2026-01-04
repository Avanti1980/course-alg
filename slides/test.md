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

<!-- slide vertical=true data-notes="" -->

##### Toom 算法

---

方程组涉及$5$个乘法子问题：

$$
\begin{align*}
    \begin{array}{l}
    s_4 \triangleq ad \\
    s_3 \triangleq (4a+2b+c)(4d+2e+f) \\
    s_2 \triangleq (a-b+c)(d-e+f) \\
    s_1 \triangleq (a+b+c)(d+e+f) \\
    s_0 \triangleq cf
    \end{array} \Longrightarrow
    \begin{array}{l}
    w_4 = s_4                                                           \\
    w_3 = (-12 s_4 + s_3 - s_2 - 3 s_1 + 3 s_0) / 6  \\
    w_2 = (-2 s_4 + s_2 + s_1 - 2 s_0) / 2                   \\
    w_1 = (12 s_4 - s_3 - 2 s_2 + 6 s_1 - 3 s_0) / 6 \\
    w_0 = s_0
    \end{array}
\end{align*}
$$

<p class="fragment">由此可得$T(n) = 5 \cdot T (n/3) + \Theta(n) \Longrightarrow T(n) = \Theta(n^{\log_3 5})$</p>

<p class="fragment">更一般的将$x$作$k$等分，此时$w(t)$是$2k-2$次多项式，共有$2k-1$个系数，线性方程组需包含$2k-1$个方程，由此产生$2k-1$个子问题，时间复杂度$\Theta(n^{\log_k (2k-1)})$</p>