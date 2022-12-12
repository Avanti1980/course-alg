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

##### 算法停止条件

---

当残存网络中不再有增广路径时，确实找到了最大流吗？

最大流最小切割定理：设$f$为流网络$\Gcal = (\Vcal, \Ecal)$中的一个流，该流网络源点为$s$、汇点为$t$，则下面的条件是等价的：

1. $f$是$\Gcal$的一个最大流
2. 残存网络$\Gcal_f$不包括任何增广路径
3. $|f| = c(S,T)$，其中$(S,T)$是流网络$\Gcal$的某个切割

<div class="top2"></div>

三点说明

1. 定理表明算法停止条件可以设为残存网络$\Gcal_f$不包括任何增广路径
2. 残存网络$\Gcal_f$中没有残存容量为零的边，没有增广路径就是没有$s$到$t$的路径
3. 由 1 证 2 是显然的，难的是由 2 证 1，因此需要引入最小切割过渡

<!-- slide vertical=true data-notes="" -->

##### 流网络的切割

---

给定流网络            ，源结点为s，汇点为t。
       定义一个切割(S,T)，将结点集合V分成两部分S和T=V-S，使得                 。
       若f是G上的一个流，定义横跨切割(S,T)的净流量f(S,T)为：



       定义切割(S,T)的容量为:

最小切割：一个网络的最小切割是网络中容量最小的切割。
