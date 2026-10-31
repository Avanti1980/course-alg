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

<!-- slide data-notes="" -->

##### 归并排序 _vs_ 快速排序

---

<div class="threelines top-2 left8 righta">

|          |        CPU         |   算法   |     时间复杂度     |
| :------: | :----------------: | :------: | :----------------: |
| 计算机 A | $10^{10}$条指令/秒 | 插入排序 |   $2 \cdot n^2$    |
| 计算机 B |  $10^7$条指令/秒   | 归并排序 | $50 \cdot n \lg n$ |

</div>

1. 插入排序时间复杂度中的常数因子仅为归并排序的$2/50 = 1/25$
2. 插入排序所在的计算机 A 的硬件比归并排序的快$10^{10} / 10^7 = 1000$倍

<div class="top2"></div>

现对长度一千万的数组进行排序，$n = 10^7$

<p class="bottom6">
\begin{align}
    \frac{2 \cdot (10^7)^2 \class{base01}{\text{指令}}}{10^{10} \class{base01}{\text{指令/秒}}} > 5.5 \class{base01}{\text{小时}}, \quad \frac{50 \cdot 10^7 \lg 10^7 \class{base01}{\text{指令}}}{10^7 \class{base01}{\text{指令/秒}}} < 20 \class{base01}{\text{分钟}}
\end{align}
</p>

- 问题规模$n$达到一定程度时，时间复杂度中关于$n$的部分会成为算法最终性能表现的决定性因素
- 我们感兴趣的恰是大规模问题 (小问题上不同算法的体感表现拉不开差距)
