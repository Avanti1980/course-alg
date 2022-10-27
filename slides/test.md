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

##### 限界函数的相互关系

---

<div class="threelines left8 righta">

|      | 等价关系 |   >   | 非严格偏序关系 |  >  | 严格偏序关系 |
| :--: | :------: | :---: | :------------: | :-: | :----------: |
| 函数 | $\Theta$ |  $O$  |    $\Omega$    | $o$ |   $\omega$   |
|  数  |   $=$    | $\le$ |     $\ge$      | $<$ |     $>$      |

</div>

基于此类比易知有

<div class="threelines left8 righta">

|          | 自反性 | 对称性 | 转置对称性 | 传递性 |
| :------: | :----: | :----: | :--------: | :----: |
| $\Theta$ |   ✓    |   ✓    |     ✗      |   ✓    |
|   $O$    |   ✓    |   ✗    |     ✓      |   ✓    |
| $\Omega$ |   ✓    |   ✗    |     ✓      |   ✓    |
|   $o$    |   ✗    |   ✗    |     ✓      |   ✓    |
| $\omega$ |   ✗    |   ✗    |     ✓      |   ✓    |

</div>

<!-- slide vertical=true data-notes="" -->

##### 自反性

---

求证：$f(n) = \Theta(f(n))$、$f(n) = O(f(n))$、$f(n) = \Omega(f(n))$

证明：$f(n)$渐进非负，设临界点为$n_f$，易知对$\forall n \ge n_f$有

$$
\begin{align*}
    \quad 0 \le 1 \cdot f(n) \le f(n) \le 1 \cdot f(n)
\end{align*}
$$

取$c_1 = c_2 = 1$、$n_0 = n_f$即有$f(n) = \Theta(f(n))$

由$f(n) = \Theta(f(n)) \Longleftrightarrow \begin{cases} f(n) = O(f(n)) \\ f(n) = \Omega(f(n)) \end{cases}$可知$O, \Omega$自反性成立

<!-- slide vertical=true data-notes="" -->

##### 对称性

---

求证：$f(n) = \Theta(g(n)) \Longleftrightarrow g(n) = \Theta(f(n))$

证明：

<div class="top-7"></div>

$$
\begin{align*}
    f(n) & = \Theta(g(n)) \\
    & \big \Updownarrow \\
    \qquad \exists c_1, c_2, n_0 > 0 ~ & \forall n \ge n_0 : 0 \le c_1 g(n) \le f(n) \le c_2 g(n) \\
    & \big \Updownarrow \\
    \exists c_1, c_2, n_0 > 0 ~ & \forall n \ge n_0 : 0 \le f(n) / c_2 \le g(n) \le f(n) / c_1 \\
    d_1 = 1 / c_1 ~ & \Biggl \Updownarrow ~  d_2 = 1 / c_2 \\
    \exists d_1, d_2, n_0 > 0 ~ & \forall n \ge n_0 : 0 \le d_1 f(n) \le g(n) \le d_2 f(n) \\
    & \big \Updownarrow \\
    g(n) & = \Theta(f(n))
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 转置对称性

---

求证：$f(n) = O(g(n)) \Longleftrightarrow g(n) = \Omega(f(n))$

证明：

<div class="top-7"></div>

$$
\begin{align*}
    f(n) & = O(g(n)) \\
    & \big \Updownarrow \\
    \qquad \exists c, n_0 > 0 ~ & \forall n \ge n_0 : 0 \le f(n) \le c g(n) \\
    & \big \Updownarrow \\
    \exists c, n_0 > 0 ~ & \forall n \ge n_0 : 0 \le f(n) / c \le g(n) \\
    & \Biggl \Updownarrow ~  d = 1 / c \\
    \exists d, n_0 > 0 ~ & \forall n \ge n_0 : 0 \le d f(n) \le g(n) \\
    & \big \Updownarrow \\
    g(n) & = \Omega(f(n))
\end{align*}
$$

<div class="top-2"></div>

同理可证$f(n) = o(g(n)) \Longleftrightarrow g(n) = \omega(f(n))$

<!-- slide vertical=true data-notes="" -->

##### 传递性

---

求证：$\begin{cases} f(n) = O(g(n)) \\ g(n) = O(h(n)) \end{cases} \Longrightarrow f(n) = O(h(n))$

证明：

<div class="top-7"></div>

$$
\begin{align*}
    & \qquad \qquad \begin{cases}
    f(n) = O(g(n)) : \exists c_1, n_1 > 0 ~ \forall n \ge n_1 : 0 \le f(n) \le c_1 g(n) \\
    g(n) = O(h(n)) : \exists c_2, n_2 > 0 ~ \forall n \ge n_2 : 0 \le g(n) \le c_2 h(n)
    \end{cases} \\
    & \qquad \qquad \qquad \qquad \qquad \big \Downarrow \\
    & \qquad \qquad \exists c_1, c_2, n_1, n_2 > 0 ~ \forall n \ge \max \{n_1, n_2\} : 0 \le f(n) \le c_1 c_2 h(n) \\
    & \qquad \qquad \qquad \qquad \qquad \Biggl \Downarrow ~  c = c_1 c_2, ~ n_0 = \max \{n_1, n_2\}  \\
    & \qquad \qquad \exists c, n_0 > 0 ~ \forall n \ge n_0 : 0 \le f(n) \le c h(n) \\
    & \qquad \qquad \qquad \qquad \qquad \big \Downarrow \\
    & \qquad \qquad \qquad \quad ~ f(n) = O(h(n))
\end{align*}
$$

<div class="top-2"></div>

同理可证$\begin{cases} f(n) = \Omega(g(n)) \\ g(n) = \Omega(h(n)) \end{cases} \Longrightarrow f(n) = \Omega(h(n))$

<!-- slide vertical=true data-notes="" -->

##### 传递性

---

求证：$\begin{cases} f(n) = \Theta(g(n)) \\ g(n) = \Theta(h(n)) \end{cases} \Longrightarrow f(n) = \Theta(h(n))$

证明：

<div class="top-7"></div>

$$
\begin{align*}
    \qquad \qquad \begin{cases} f(n) = \Theta(g(n)) \Longrightarrow \begin{cases} f(n) = O(g(n)) \\ f(n) = \Omega(g(n)) \end{cases} \\ g(n) = \Theta(h(n)) \Longrightarrow \begin{cases} g(n) = O(h(n)) \\ g(n) = \Omega(h(n)) \end{cases} \end{cases}
\end{align*}
$$

根据$O$、$\Omega$的传递性有$\begin{cases} f(n) = O(h(n)) \\ f(n) = \Omega(h(n)) \end{cases} \Longrightarrow f(n) = \Theta(h(n))$

<!-- slide vertical=true data-notes="" -->

##### 传递性

---

求证：$\begin{cases} f(n) = o(g(n)) \\ g(n) = o(h(n)) \end{cases} \Longrightarrow f(n) = o(h(n))$

证明：

<div class="top-7"></div>

$$
\begin{align*}
    & \qquad \qquad \begin{cases}
    f(n) = O(g(n)) : \exists c_1, n_1 > 0 ~ \forall n \ge n_1 : 0 \le f(n) \le c_1 g(n) \\
    g(n) = O(h(n)) : \exists c_2, n_2 > 0 ~ \forall n \ge n_2 : 0 \le g(n) \le c_2 h(n)
    \end{cases} \\
    & \qquad \qquad \qquad \qquad \qquad \big \Downarrow \\
    & \qquad \qquad \exists c_1, c_2, n_1, n_2 > 0 ~ \forall n \ge \max \{n_1, n_2\} : 0 \le f(n) \le c_1 c_2 h(n) \\
    & \qquad \qquad \qquad \qquad \qquad \Biggl \Downarrow ~  c = c_1 c_2, ~ n_0 = \max \{n_1, n_2\}  \\
    & \qquad \qquad \exists c, n_0 > 0 ~ \forall n \ge n_0 : 0 \le f(n) \le c h(n) \\
    & \qquad \qquad \qquad \qquad \qquad \big \Downarrow \\
    & \qquad \qquad \qquad \quad ~ f(n) = O(h(n))
\end{align*}
$$

<div class="top-2"></div>

同理可证$\begin{cases} f(n) = \omega(g(n)) \\ g(n) = \omega(h(n)) \end{cases} \Longrightarrow f(n) = \omega(h(n))$
