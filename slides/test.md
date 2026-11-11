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

##### 递归树 非平衡子问题

---

例：$T(n) = T(n/3) + T(2n/3) + c n$，猜测$T(n) = \Theta(n \lg n)$

欲证$T(n) \le d n \lg n$，只需取$d$满足

<p>
\begin{align}
    T(n) & = T \left( \frac{n}{3} \right) + T \left( \frac{2n}{3} \right) + cn \\
    & \le d \frac{n}{3} \lg \frac{n}{3} + d \frac{2 n}{3} \lg \frac{2n}{3} + cn \\
    & = d n \lg n - \left( \lg 3 - \frac{2}{3} \right) d n + cn \\
    & \le d n \lg n
\end{align}
</p>

<p class="fragment" data-fragment-index="1">同理欲证$T(n) \ge d n \lg n$，只需取$d$满足</p>

<p class="fragment" data-fragment-index="1">
\begin{align}
    T(n) \ge d n \lg n - \left( \lg 3 - \frac{2}{3} \right) d n + cn \ge d n \lg n
\end{align}
</p>

<!-- slide vertical=true data-notes="" -->

##### 递归树 非平衡子问题

---

欲证$T(n) \le d n \lg n$，只需取$d_1$、$d$满足

<p>
\begin{align}
    T(n) & = T \left( \frac{n}{3} \right) + T \left( \frac{2n}{3} \right) + cn \le d n \lg n - \left( \lg 3 - \frac{2}{3} \right) d n + cn \le d n \lg n \\
    T(n) & \ge d_1 n \lg n - \left( \lg 3 - \frac{2}{3} \right) d_1 n + cn \ge d_1 n \lg n
\end{align}
</p>
