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

##### 磁带保存文件

---

磁带特点：读取文件时需将目标文件之前的文件顺序读一遍

<div class="top4">
    <img src="../img/tape.jpg" width=640px height=360px>
</div>

<!-- slide vertical=true data-notes="" -->

##### 磁带保存文件

---

设磁带上存储着$n$个文件，长度分别为$L[1, \ldots, n]$，读取第$k$个文件的开销为$c(k) = \sum_{i=1}^k L[i]$

<p class="fragment" data-fragment-index="1">随机读取一个文件的期望时间开销为$\Ebb[c] = \frac{1}{n} \sum_{k=1}^n \sum_{i=1}^k L[i]$</p>

<p class="fragment" data-fragment-index="2">设$\pi$是一个排列，$\pi(i)$表示文件$i$在磁带上的序号，随机读取一个文件的期望时间开销为</p>

<p class="fragment" data-fragment-index="2">
$$
\begin{align*}
    \quad \Ebb[c] = \frac{1}{n} \sum_{k=1}^n \sum_{i=1}^k L[\pi(i)]
\end{align*}
$$
</p>
