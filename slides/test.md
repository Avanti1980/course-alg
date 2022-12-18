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

##### 流的递增

---

设$\Vcal_1 = \{ v \mid (s,v) \in \Ecal \}$、$\Vcal_2 = \{ v \mid (v,s) \in \Ecal \}$，注意$\Vcal_1 \cap \Vcal_2 = \emptyset$

<div class="top2"></div>

$$
\begin{align*}
    |f & \uparrow f'| = \sum_{v \in \Vcal_1} (f \uparrow f')(s,v) - \sum_{v \in \Vcal_2} (f \uparrow f')(v,s) \\
    & = \sum_{v \in \Vcal_1} (f(s,v) + f'(s,v) - f'(v,s)) - \sum_{v \in \Vcal_2} (f(v,s) + f'(v,s) - f'(s,v)) \\
    & = \sum_{v \in \Vcal_1} f(s,v) - \sum_{v \in \Vcal_2} f(v,s) + \sum_{v \in \Vcal_1 \cup \Vcal_2} f'(s,v) - \sum_{v \in \Vcal_1 \cup \Vcal_2} f'(v,s) \\
    & = |f| + |f'|
\end{align*}
$$

如何在残存网络$\Gcal_f$中找流$f'$？
