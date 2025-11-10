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

##### 主方法 证明思路

---

设$n = b^t$(不等时需证明$T(\lfloor n/b \rfloor)$和$T(\lceil n/b \rceil)$不影响结果)，则

$$
\begin{align*}
    \quad & \spadesuit \qquad T(n/b^0) = a \cdot T(n/b^1) + f(n/b^0) \\
    & \heartsuit \qquad T(n/b^1) = a \cdot T(n/b^2) + f(n/b^1) \\
    & \qquad \qquad \vdots \\
    & \clubsuit \qquad T(n/b^{t-1}) = a \cdot T(n/b^t) + f(n/b^{t-1})
\end{align*}
$$

<div class="top-2"></div>

令$\spadesuit + \heartsuit \cdot a + \cdots + \clubsuit \cdot a^{t-1}$可得

$$
\begin{align*}
    \quad T(n) & = a^t \cdot T(1) + \sum_{i=0}^{t-1} a^i f(n/b^i) = \Theta(n^{\log_b a}) + \sum_{i=0}^{t-1} a^i f(n/b^i)
\end{align*}
$$

需要比较$n^{\log_b a}$和$g(n) = \sum_{i=0}^{t-1} a^i f(n/b^i)$

<!-- slide vertical=true data-notes="" -->

##### 主方法 证明思路

---

以$f(n) = n^d$为例

$$
\begin{align*}
    \quad g(n) = \sum_{i=0}^{t-1} a^i f \left( \frac{n}{b^i} \right) = \sum_{i=0}^{t-1} a^i \left( \frac{n}{b^i} \right)^d = n^d \sum_{i=0}^{t-1} \left( \frac{a}{b^d} \right)^i 
\end{align*}
$$

- 若$a > b^d$，则$\log_b a > d$，即情形1，等比数列公比$q>1$，和为最后一项$(a/b^d)^{t-1} = a^{t-1} b^d / n^d < a^t / n^d = a^{\log_b n}/ n^d = n^{\log_b a} / n^d$的常数倍，故$g(n) = \Theta(n^{\log_b a})$
- 若$a = b^d$，则$\log_b a = d$，即情形2，等比数列公比$q=1$，和为$t$，故$g(n) = \Theta(n^{\log_b a} \log_b n)$
- 若$a < b^d$，则$\log_b a < d$，即情形3，等比数列公比$q<1$，和为常数，故$g(n) = \Theta(n^d) = \Theta(f(n))$




