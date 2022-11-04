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

##### 递归树

---

递归树可用来生成好的猜测

<div class="top-2"></div>

$T(n) = 3 \cdot T(n/4) + c n^2$的递归树如下

@import "../tikz/tree2.svg" {.center .width90 .top3}


<!-- slide vertical=true data-notes="" -->

##### 递归树

---

$$
\begin{align*}
    \qquad \quad \scriptsize T(n) = 3 \cdot T(n/4) + c n^2
\end{align*}
$$

@import "../tikz/tree2.svg" {.center .width90 .top-7 .bottom4}

- 每个结点表示某个单一子问题的时间复杂度
- 第$i$层共有$3^i$个结点，对应第$i$层递归调用，总层数为$\log_4 n + 1$
- 叶节点为递归调用的边界情况，共有$3^{\log_4 n} = n^{\log_4 3}$个
- 所有结点上的值的和即为$T(n)$

<!-- slide vertical=true data-notes="" -->

##### 递归树

---

$$
\begin{align*}
    \qquad \quad \scriptsize T(n) = 3 \cdot T(n/4) + c n^2
\end{align*}
$$

@import "../tikz/tree2.svg" {.center .width90 .top-7 .bottom4}

$$
\begin{align*}
    \quad T(n) & = cn^2 + \frac{3}{16} cn^2 + \cdots + \left( \frac{3}{16} \right)^{\log_4 n - 1} cn^2 + n^{\log_4 3} \Theta(1) \\
    & < \sum_{i=0}^\infty \left( \frac{3}{16} \right)^i cn^2 + \Theta(n^{\log_4 3}) = O(n^2)
\end{align*}
$$



