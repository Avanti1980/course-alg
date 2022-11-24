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

##### 问题描述

---

输入：带权无向图$\Gcal = (\Vcal, \Ecal, w)$，其中$\Vcal$为边集、$\Ecal$为点集，边上的权重由权重函数$w: \Ecal \mapsto \Rbb$给出

输出：最小权重生成树$\Tcal$

@import "../tikz/span-tree.svg" {.center .width60 .top5}

<!-- slide vertical=true data-notes="" -->

##### 思路

---

初始化边集$\Acal = \emptyset$，之后每轮选择一条边$(u,v)$加入$\Acal$

在此过程中保证$\Acal$始终是某棵最小生成树的子集

<div class="top2"></div>

问题：如何选择边$(u,v)$？

<!-- slide data-notes="" -->

##### 基本概念

---

切割：无向图$\Gcal = (\Vcal, \Ecal, w)$的切割$(\Scal, \Vcal \setminus \Scal)$是$\Vcal$的一个划分

<div class="top-1"></div>

横跨切割边：边的两个端点分属于$\Scal$和$\Vcal \setminus \Scal$，例如$(a,h)$

<div class="top-1"></div>

尊重：如果集合$\Acal$中没有横跨切割的边，称该切割尊重$\Acal$

<div class="top-1"></div>

轻量边：横跨切割边中权重最小的边，例如$(c,d)$

@import "../tikz/span-tree-cut.svg" {.center .width70 .top2}

<!-- slide vertical=true data-notes="" -->

##### 如何选择边

---

贪心：每轮对任意{==尊重==}当前$\Acal$的切割，选择{==轻量边==}$(u,v)$加入

正确性证明：设$\Tcal$是任一包含$\Acal$的最小生成树，但$(u,v) \not \in \Tcal$

<div class="top-1"></div>

不妨设$\Tcal$中$u$到$v$的路径$p = \class{yellow}{u \rightsquigarrow w \rightsquigarrow x} \rightsquigarrow \class{blue}{b \rightsquigarrow a \rightsquigarrow v}$

<div class="top-1"></div>

$(u,v)$横跨切割，$p$中也必有一边横跨切割，不妨设为$(x,b)$

<div class="top-1"></div>

当前切割尊重$\Acal$，故$(x,b) \not \in \Acal$

<div class="top-1"></div>

记$\Tcal' = \Tcal \setminus \{ (x,b) \} \cup \{ (u,v) \}$

<div class="top-1"></div>

$w(u,v) \le w(x,b)$，$\Tcal'$也是最小生成树

<div class="top-1"></div>

$\Acal \cup \{ (u,v) \} \subseteq \Tcal'$

@import "../dot/span-tree-proof.dot" {.lefta .right8 .top-28per}

<!-- slide data-notes="" -->

##### 最小生成树 算法

---

Kruskal 算法：$\Acal$始终是一个森林

- 初始时$\Acal$是所有单结点树构成的森林
- 每次加入连接$\Acal$中两棵树的权重最小的边

<div class="top2"></div>

Prim 算法：$\Acal$始终是一个树

- 初始时$\Acal$是某个单结点树
- 每次加入连接$\Acal$和$\Acal$之外结点的权重最小的边

<!-- slide vertical=true data-notes="" -->

##### <span style="font-weight:900">Kruskal</span> 算法

---

@import "../tikz/kruskal.svg" {.center .width60 .top2}

