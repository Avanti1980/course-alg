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

##### 磁带存储

---

磁带特点：读取文件时需将目标文件之前的文件顺序读一遍

<div class="top4">
    <img src="../img/tape.jpg" width=640px height=360px>
</div>

<!-- slide vertical=true data-notes="" -->

##### 磁带存储

---

设磁带上存储着$n$个文件，长度分别为$L[1, \ldots, n]$，读取第$k$个文件的开销为$c(k) = \sum_{i=1}^k L[i]$

<div class="top2"></div>

<p class="fragment" data-fragment-index="1">随机读取一个文件的期望开销为$\Ebb[c] = \frac{1}{n} \sum_{k=1}^n \sum_{i=1}^k L[i]$</p>

<div class="top2"></div>

<p class="fragment" data-fragment-index="2">设$\pi$是一个排列，$\pi(i)$表示磁带上第$i$个文件的实际文件编号，随机读取一个文件的期望开销为$\Ebb[c(\pi)] = \frac{1}{n} \sum_{k=1}^n \sum_{i=1}^k L[\pi(i)]$</p>

<div class="top2"></div>

<p class="fragment" data-fragment-index="3">问题：文件如何排列可使期望开销最低？</p>

<!-- slide vertical=true data-notes="" -->

##### 磁带存储

---

暴力穷举：$\Omega(2^n)$

动态规划？

<p class="fragment">最优子结构性：设$\pi(1), \ldots, \pi(n)$是$\{ \text{文件}1,\ldots, \text{文件}n \}$的最优存储顺序，则$\pi(2), \ldots, \pi(n)$是$\{ \text{文件}1,\ldots, \text{文件}n \}\setminus \{\text{文件}\pi(1)\}$的最优存储顺序</p>

<!-- slide data-notes="" -->

##### 磁带存储 贪心

---

引理：使$\Ebb[c(\pi)]$最小的排列就是$L[1, \ldots, n]$的增序

<p class="fragment">证明：假设存在$i$使得$L[\pi(i)] \ge L[\pi(i+1)]$</p>

<p class="fragment">记$a = \pi(i)$、$b = \pi(i+1)$，交换$a$、$b$得到新的排列$\pi'$</p>

<ul class="fragment">
  <li>其它$n-2$个文件的读取不受影响</li>
  <li>读取文件$a$的开销增加$L[b]$</li>
  <li>读取文件$b$的开销减少$L[a]$</li>
  <li>由于$L[a] \ge L[b]$，因此$\Ebb[c(\pi')] \le \Ebb[c(\pi)]$</li>
</ul>

<div class="top2"></div>

<p class="fragment">算法的正确性：假设最优排列$\pi^\star$与增序不同，则其必然存在逆序，交换可得新的排列$\pi'$，由引理$\Ebb[c(\pi')] \le \Ebb[c(\pi^\star)]$</p>

<!-- slide vertical data-notes="" -->

##### 磁带存储 贪心

---

假设除长度外，还有频率$F[1, \ldots, n]$

随机读取一个文件的期望开销为

$$
\begin{align*}
    \quad \Ebb[c(\pi)] = \frac{1}{n} \sum_{k=1}^n \sum_{i=1}^k L[\pi(i)] F[\pi(i)]
\end{align*}
$$

<!-- slide vertical data-notes="" -->

##### 磁带存储 贪心

---

引理：使$\Ebb[c(\pi)]$最小的排列就是$L[\pi(i)]/F[\pi(i)]$的增序

<p class="fragment">证明：假设存在$i$使得$L[\pi(i)]/F[\pi(i)] \ge L[\pi(i+1)]/F[\pi(i+1)]$</p>

<p class="fragment">记$a = \pi(i)$、$b = \pi(i+1)$，交换$a$、$b$得到新的排列$\pi'$</p>

<ul class="fragment">
  <li>其它$n-2$个文件的读取不受影响</li>
  <li>读取文件$a$的开销增加$L[b] F[a]$</li>
  <li>读取文件$b$的开销减少$L[a] F[b]$</li>
</ul>

<div class="top4"></div>

<p class="fragment">
$$
\begin{align*}
    \quad \frac{L[a]}{F[a]} \ge \frac{L[b]}{F[b]} \Longleftrightarrow L[a] F[b] \ge L[b] F[a]
\end{align*}
$$
</p>

