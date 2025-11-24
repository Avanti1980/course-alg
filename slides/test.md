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

##### 活动安排

---

现有$n$个活动，编号分别为$1, \ldots, n$，时长分别为$L[1], \ldots, L[n]$，最后期限为$D[1], \ldots, D[n]$

在安排方案$\pi$中，活动$k$的结束时间为$c_{\pi} (k) = \sum_{i=1}^k L[\pi(i)]$，记延迟$\lambda_{\pi} (k) = \max \{ 0, c_{\pi} (k) - D[k] \}$

问题：求最优排列$\pi^\star$使最大延迟$\max_{k} \lambda_{\pi} (k)$最小</p>

<p class="fragment" data-fragment-index="1">贪心选择：</p>

<ul>
  <li class="fragment" data-fragment-index="2">按照时长$L[k]$的升序，优先安排不太耗时的活动</li>
  <li class="fragment" data-fragment-index="3">按照最后期限$D[k]$的升序，优先安排时间紧的活动</li>
  <li class="fragment" data-fragment-index="4">按照$L[k] \cdot D[k]$的升序安排活动</li>
</ul>

<!-- slide vertical=true data-notes="" -->

##### 活动安排

---

假设有两个活动：

- 活动$1$：$L[1] = 10$、$D[1] = 50$
- 活动$2$：$L[2] = 100$、$D[2] = 20$

<div class="top2"></div>

三种贪心选择：

- 按$L[k]$升序：$\pi(1) = 1$、$\pi(2) = 2$，$\lambda_{\pi} (1) = 0$、$\lambda_{\pi} (2) = 90$
- 按$D[k]$升序：$\pi(1) = 2$、$\pi(2) = 1$，$\lambda_{\pi} (1) = 80$、$\lambda_{\pi} (2) = 60$
- 按$L[k] \cdot D[k]$升序：同按$L[k]$升序

<p class="fragment top4" data-fragment-index="1">对最小化最大延迟问题：按照时长$L[k]$升序和按$L[k] \cdot D[k]$升序都不是正确的贪心选择</p>

<!-- slide vertical=true data-notes="" -->

##### 活动安排 正确性证明

---

按最后期限$D[k]$升序是正确的贪心选择，对任意排列$\pi$，若存在$i$使得$D[\pi(i)] \ge D[\pi(i+1)]$，交换活动$\pi(i)$、$\pi(i+1)$后得到的新排列为$\pi'$

其余$n-2$个活动的延迟情况不变，记$M = \sum_{j=1}^{i-1} L[\pi(j)]$

- $\lambda_\pi (i) = \max \{0, M + L[\pi(i)] - D[\pi(i)]\}$
- $\lambda_\pi (i+1) = \max \{0, M + L[\pi(i)] + L[\pi(i+1)] - D[\pi(i+1)]\}$
- $\lambda_{\pi'} (i) = \max \{0, M + L[\pi(i+1)] - D[\pi(i+1)]\}$
- $\lambda_{\pi'} (i+1) = \max \{0, M + L[\pi(i)] + L[\pi(i+1)] - D[\pi(i)]\}$

<div class="top2"></div>

显然$\lambda_{\pi'} (i) \le \lambda_\pi (i+1)$、$\lambda_{\pi'} (i+1) \le \lambda_\pi (i+1)$，故

$$
\begin{align*}
    \quad \max \{ \lambda_{\pi'} (i), \lambda_{\pi'} (i+1) \} \le \lambda_\pi (i+1) \le \max \{ \lambda_\pi (i), \lambda_\pi (i+1) \}
\end{align*}
$$



