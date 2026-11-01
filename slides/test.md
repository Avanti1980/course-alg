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
@import "../plugin/notes/notes.js"
@import "../plugin/customcontrols/plugin.js"
@import "../plugin/customcontrols/style.css"
@import "../plugin/chalkboard/plugin.js"
@import "../plugin/chalkboard/style.css"
@import "../plugin/reveal.js-menu/menu.js"

<!-- slide vertical=true data-notes="" -->

##### 一些例题 证明

---

求证：$\lg ( \Theta(n)) = \Theta(\lg n)$

<details>
  
<summary>证明</summary>

<p>证明：左边的渐进界表示任意，等号表示属于$\in$，即</p>

<p>
\begin{align}
    \forall f(n) \in \Theta(n) : \lg (f(n)) \in \Theta(\lg n)
\end{align}
</p>

<p>根据定义$\exists c_1, c_2, n_0 > 0$使得对$\forall n \ge n_0$有$0 \le c_1 n \le f(n) \le c_2 n$，故</p>

<p>
\begin{align}
    \lg c_1 + \lg n \le \lg (f(n)) \le \lg c_2 + \lg n
\end{align}
</p>

<p>最后只需将上下界再放成$\lg n$的常数倍</p>

<ul>
  <li>$\lg c_2 \le \lg n$，这只需$n \ge c_2$</li>
  <li>$\lg c_1$是常数，$\lg n$上无界，因此只能是$\lg c_1 \ge - \frac{1}{2} \lg n$，这只需$n \ge 1/c_1^2$</li>
</ul>

<div class="top-2"></div>

<p>综上，对$\forall n \ge \max \{ n_0, 1/c_1^2, c_2 \}$有$\frac{1}{2} \lg n \le \lg (f(n)) \le 2 \lg n$</p>

</details>

<!-- slide vertical=true data-notes="" -->

##### 一些例题 证明

---

求证：$k \lg k = \Theta(n) \Longrightarrow k = \Theta (n / \lg n)$

<details>
  
<summary>证明</summary>

<p>证明：$\exists c_1, c_2, k_0 > 0~\forall k \ge k_0: 0 \le c_1 n \le k \lg k \le c_2 n$</p>

<p>如果还有$\lg k$的上下界均是$\lg n$的常数倍，两式相除即得证</p>

<p>取对数$\lg c_1 + \lg n \le \lg k + \lg (\lg k) \le \lg c_2 + \lg n$</p>

<ul>
  <li>上界：若$\lg (\lg k) \ge \lg c_2$则有$\lg k \le \lg n$，这需要$k \ge \exp(c_2)$</li>
  <li>下界：若$\lg (\lg k) - \lg c_1 \le \lg k^2 = 2 \lg k$则有$\frac{1}{3} \lg n \le \lg k$，这需要$\lg k \le c_1 k^2$，即$k \le \exp (c_1 k^2)$，注意$\exp (c_1 k^2) \ge 1 + c_1 k^2 > c_1 k^2$，因此有$c_1 k \ge 1$即可</li>
</ul>

<div class="top-2"></div>

<p>综上，对$\forall k \ge \max \{\exp(c_2), 1/ c_1 \}$有$\frac{1}{3} \lg n \le \lg k \le \lg n$</p>

<p>$\exists c_1, c_2, k_0 > 0 ~ \forall k \ge \max \{k_0, \exp(c_2), 1/ c_1 \}: c_1 \frac{n}{\lg n} \le k \le 3 c_2 \frac{n}{\lg n}$</p>

</details>
