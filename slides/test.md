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

在安排方案$\pi$中，活动$k$的结束时间为$c_{\pi} (k) = \sum_{i=1}^k L[\pi(i)]$，记延迟$\lambda_{\pi} (k) = \max \{ 0, c_{\pi} (k) \}$

问题：求最优排列$\pi^\star$使最大延迟$\max_{k} \lambda_{\pi} (k)$最小</p>

贪心选择：

- 按照时长$L[k]$的升序安排活动
- 按照最后期限$D[k]$的升序安排活动
- 按照$L[k] \cdot D[k]$的升序安排活动

<!-- slide vertical=true data-notes="" -->

##### 活动安排

---

假设有两个活动：

- 活动$1$：$L[1] = 10$、$D[1] = 50$
- 活动$2$：$L[2] = 100$、$D[2] = 20$

<div class="top2"></div>

按照时长：
