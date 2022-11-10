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

##### 最长公共子序列

---

DNA 由 A、C、G、T 四种碱基组成，现有两个有机体的 DNA

- S1 = ACCG{==GTCG==}AG{==T==}G{==CG==}C{==G==}G{==AAGCCGGCCGAA==}
- S2 = {==GTCGT==}T{==CGGAA==}T{==GCCG==}TT{==GC==}T{==C==}T{==G==}T{==AA==}A

<div class="top2"></div>

两个有机体有多“相似”，基因序列比对

1. 将其中一个转换成另一个所需改变的工作量，编辑距离 (edit distance)
2. 找{==最长==}的 S3，其中的基以同样的顺序出现在 S1 和 S2 中，但不一定连续

<div class="top2"></div>

S3 = GTCGTCGGAAGCCGGCCGAA

两个字符串的最长公共非连续子串称为最长公共子序列 (longest common subsequence, LCS)

<!-- slide data-notes="" -->

##### <span style="font-weight:900">LCS</span> 最优子结构性

---

序列$X = \langle x_1, x_2, \ldots, x_m \rangle$，序列$Y = \langle y_1, y_2, \ldots, y_m \rangle$

<div class="top-2"></div>

记$X$的前$i$个元素构成的{==前缀==}子序列为$X_i = \langle x_1, x_2, \ldots, x_i \rangle$

<div class="top-2"></div>

设序列$Z = \langle z_1, z_2, \ldots, z_k \rangle$是$X$和$Y$的任意 LCS

<div class="top2"></div>

① 若$x_m = y_n$，则$z_k = x_m = y_n$且$Z_{k-1}$是$X_{m-1}$和$Y_{n-1}$的 LCS

反设$z_k \ne x_m = y_n$，将$x_m$接到$Z$的末尾可以得到一个长为$k+1$的公共子序列，这与$Z$的最优性矛盾

已证$z_k = x_m = y_n$，因此$Z_{k-1}$是$X_{m-1}$和$Y_{n-1}$的公共子序列，若其不是最长，则另有一个长度大于$k-1$的子序列，将$x_m$接到该子序列末尾可以得到$X$和$Y$的一个长度大于$k$的子序列，矛盾

<!-- slide vertical=true data-notes="" -->

##### <span style="font-weight:900">LCS</span> 最优子结构性

---

序列$X = \langle x_1, x_2, \ldots, x_m \rangle$，序列$Y = \langle y_1, y_2, \ldots, y_m \rangle$

<div class="top-2"></div>

记$X$的前$i$个元素构成的{==前缀==}子序列为$X_i = \langle x_1, x_2, \ldots, x_i \rangle$

<div class="top-2"></div>

设序列$Z = \langle z_1, z_2, \ldots, z_k \rangle$是$X$和$Y$的任意 LCS

<div class="top2"></div>

② 若$x_m \ne y_n$，则$z_k \ne x_m$蕴含$Z$是$X_{m-1}$和$Y$的一个 LCS

若$z_k \ne x_m$，$Z$显然是$X_{m-1}$和$Y$的公共子序列，若其不是最长，则另有一个长度大于$k$的子序列，该子序列也是$X$和$Y$的子序列，这与$Z$的最优性矛盾

<div class="top2"></div>

③ 若$x_m \ne y_n$，则$z_k \ne y_n$蕴含$Z$是$X$和$Y_{n-1}$的一个 LCS

<!-- slide vertical=true data-notes="" -->

##### <span style="font-weight:900">LCS</span> 最优子结构性

---

序列$X = \langle x_1, x_2, \ldots, x_m \rangle$，序列$Y = \langle y_1, y_2, \ldots, y_m \rangle$

<div class="top-2"></div>

记$X$的前$i$个元素构成的{==前缀==}子序列为$X_i = \langle x_1, x_2, \ldots, x_i \rangle$

<div class="top-2"></div>

设序列$Z = \langle z_1, z_2, \ldots, z_k \rangle$是$X$和$Y$的任意 LCS

- 若$x_m = y_n$，则$z_k = x_m = y_n$且$Z_{k-1}$是$X_{m-1}$和$Y_{n-1}$的 LCS
- 若$x_m \ne y_n$，则$z_k \ne x_m$蕴含$Z$是$X_{m-1}$和$Y$的一个 LCS
- 若$x_m \ne y_n$，则$z_k \ne y_n$蕴含$Z$是$X$和$Y_{n-1}$的一个 LCS

<div class="top2"></div>

我的启示 两个序列的 LCS 的前缀子序列也是其各自前缀子序列的 LCS

记$c[i,j]$为$X_i$和$Y_j$的 LCS 的长度

$$
\begin{align*}
    \quad c[i,j] = \begin{cases} 0, & i = 0 \vee j = 0 \quad \text{其中一个为空} \\ c[i-1,j-1]+1, & i,j > 0 \wedge x_i = y_j \\ \max \{ c[i,j-1], c[i-1,j] \}, & i,j > 0 \wedge x_i \ne y_j \end{cases}
\end{align*}
$$
