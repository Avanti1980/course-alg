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

##### 最长递增子序列

---

求序列$X$、$Y$的最长公共子序列 (LCS)

若$Y$已升序排好，则 LCS 是$X$的最长递增子序列 (<span class="blue">l</span>ongest <span class="blue">i</span>ncreasing <span class="blue">s</span>ubsequence, LIS)

<div class="top4"></div>

<p class="fragment" data-fragment-index="1">输入：序列$X$</p>

<p class="fragment" data-fragment-index="1">输出：$X$的最长递增子序列</p>

<!-- slide vertical=true data-notes="" -->

##### 最优子结构

---

设以$X[i]$作结尾的 LIS 为$X[i_1], \ldots, X[i_k], X[i]$，则前缀$X[i_1], \ldots, X[i_k]$必然是以$X[i_k]$作结尾的 LIS

<p class="fragment" data-fragment-index="1">记$d[i]$为以$X[i]$结尾的 LIS 的长度，显然所有$d[i]$的最小值是 1</p>

<p class="fragment" data-fragment-index="2">$d[0] = 1$，以$X[0]$结尾的 LIS 就是$X[0]$</p>

<p class="fragment" data-fragment-index="3">$d[1]$根据$X[1]$是否可以接在$X[0]$后面分两种情况：</p>

<ul class="fragment" data-fragment-index="4">
    <li>若$X[0] < X[1]$，则$d[1] = 2$，此时 LIS 就是$X[0, 1]$</li>
    <li>若$X[0] > X[1]$，则$d[1] = 1$，此时 LIS 就是$X[1]$</li>
</ul>

<!-- slide vertical=true data-notes="" -->

##### 递推关系

---

$X[i]$接在以$X[0], X[1], \ldots, X[i-1]$结尾的哪个 LIS 后面？

在所有可接的 LIS 后面选一个最长的，若无则为$1$：

<p>
\begin{align}
    d[i] = \begin{cases}
    1, & i = 0 \\
    \max_{j < i, X[j] < X[i]} \{ 1, d[j] + 1 \}, & i > 0 \\
    \end{cases}
\end{align}
</p>

@import "../codes/dp/lis.py" {line_begin=0 line_end=9 .fragment .line-numbers highlight=[4-5]}

<p class="fragment">二重循环时间复杂度$\Theta(n^2)$，一维表格空间复杂度$\Theta(n)$</p>

<!-- slide vertical=true data-notes="" -->

##### 例子

---

<p>
\begin{align}
    d[i] = \begin{cases}
    1, & i = 0 \\
    \max_{j < i, X[j] < X[i]} \{ 1, d[j] + 1 \}, & i > 0 \\
    \end{cases}
\end{align}
</p>

<div class="threelines">

| $i$ | <span class="yellow">0</span> |  1  | <span class="yellow">2</span> |  3  |  4  | <span class="yellow">5</span> |               6               |  7  |  8  |  9  |
| :-: | :---------------------------: | :-: | :---------------------------: | :-: | :-: | :---------------------------: | :---------------------------: | :-: | :-: | :-: |
| $X$ |  <span class="blue">②</span>  |  8  |  <span class="blue">④</span>  |  9  |  1  |  <span class="blue">⑥</span>  |  <span class="blue">⑦</span>  |  3  |  0  |  5  |
| $d$ |               1               |  2  |               2               |  3  |  1  |               3               |  <span class="red">4</span>   |  2  |  1  |  3  |
| $b$ |              -1               |  0  | <span class="yellow">0</span> |  1  | -1  | <span class="yellow">2</span> | <span class="yellow">5</span> |  0  | -1  |  2  |

</div>

@import "../codes/dp/lis.py" {line_begin=11 line_end=18 .line-numbers highlight=[]}

<!-- slide data-notes="" -->

##### 改进

---

维护表$e[]$，初始为空

$e[j]$始终记录当前<span class="blue">长度为</span>$\class{blue}{j}$<span class="blue">的递增子序列的末位元素最小值</span>

<div class="top4"></div>

<p class="fragment" data-fragment-index="1">以$X = [2, 8, 4, 9, 1, 6, 7, 3, 0, 5]$为例，最终$e = [0, 3, 5, 7]$</p>

<p class="fragment" data-fragment-index="1">$e$的长度为 4 代表 LIS 的长度为$4$</p>

<p class="fragment" data-fragment-index="1">$e[-1] = 7$代表 LIS 末位元素为$7$，$[2, 4, 6, 7]$是一个 LIS</p>

<p class="fragment" data-fragment-index="2"> $e$的元素是单调递增的，这是提升速度的关键</p>

<!-- slide vertical=true data-notes="" -->

##### 改进

---

$e[j]$记录<span class="blue">长度为</span>$\class{blue}{j}$<span class="blue">的递增子序列的末位元素最小值</span>，初始为空

<div class="threelines top-2 bottom0">

| $X$ |             $e$              |   $\len(\lis)=1$    |     $\len(\lis)=2$     |      $\len(\lis)=3$       |        $\len(\lis)=4$        |
| :-: | :--------------------------: | :-----------------: | :--------------------: | :-----------------------: | :--------------------------: |
| $2$ |            $[2]$             |        $[2]$        |         &zwnj;         |          &zwnj;           |            &zwnj;            |
| $8$ |    $[2, \class{blue}{8}]$    |        $[2]$        | $[2, \class{blue}{8}]$ |          &zwnj;           |            &zwnj;            |
| $4$ |    $[2, \class{blue}{4}]$    |        $[2]$        | $[2, \class{blue}{4}]$ |          &zwnj;           |            &zwnj;            |
| $9$ |  $[2, 4, \class{blue}{9}]$   |        $[2]$        |        $[2, 4]$        | $[2, 4, \class{blue}{9}]$ |            &zwnj;            |
| $1$ |  $[\class{blue}{1}, 4, 9]$   | $[\class{blue}{1}]$ |        $[2, 4]$        |        $[2, 4, 9]$        |            &zwnj;            |
| $6$ |  $[1, 4, \class{blue}{6}]$   |        $[1]$        |        $[2, 4]$        | $[2, 4, \class{blue}{6}]$ |            &zwnj;            |
| $7$ | $[1, 4, 6, \class{blue}{7}]$ |        $[1]$        |        $[2, 4]$        |        $[2, 4, 6]$        | $[2, 4, 6, \class{blue}{7}]$ |
| $3$ | $[1, \class{blue}{3}, 6, 7]$ |        $[1]$        | $[2, \class{blue}{3}]$ |        $[2, 4, 6]$        |        $[2, 4, 6, 7]$        |
| $0$ | $[\class{blue}{0}, 3, 6, 7]$ | $[\class{blue}{0}]$ |        $[2, 3]$        |        $[2, 4, 6]$        |        $[2, 4, 6, 7]$        |
| $5$ | $[0, 3, \class{blue}{5}, 7]$ |        $[0]$        |        $[2, 3]$        | $[2, 4, \class{blue}{5}]$ |        $[2, 4, 6, 7]$        |

</div>

<!-- slide vertical=true data-notes="" -->

##### 改进

---

<span class="blue">在任意时刻</span>$\class{blue}{e}$<span class="blue">都是严格单调递增的</span>，若$i<j$且$e[i] > e[j]$，则有

<p>
\begin{align}
    \lis_i:~ \underbrace{\square ~ \square ~ \cdots ~ \square ~ e[i]}_{\len~=~i}, \quad \lis_j:~ \underbrace{\square ~ \square ~ \square ~ \square ~ \cdots ~ \square ~ \square ~ e[j]}_{\len~=~j}
\end{align}
</p>

去掉$\lis_j$前$j-i$个元素可得长度$i$、末位元素$< e[i]$的递增序列

<div class="top2"></div>

<p class="fragment" data-fragment-index="1">在遍历$X$时，对于$X[i]$</p>

<ul>
  <li class="fragment" data-fragment-index="2">若$X[i] > e[-1]$，其可接在当前 LIS 后产生更长的 LIS，$e = [e, [X[i]]$</li>
  <li class="fragment" data-fragment-index="3">若$e[j-1] < X[i] < e[j]$，其可接在长度为$j-1$的递增子序列后产生长度为$j$末位元素更小的递增子序列，$e[j] = X[i]$，确定$j$可用二分查找</li>
</ul>

<div class="top2"></div>

<p class="fragment" data-fragment-index="4">二分查找时间复杂度$O(\lg n)$，总时间复杂度$O(n \lg n)$</p>

<!-- slide vertical=true data-notes="" -->

##### 改进

---

@import "../codes/dp/lis.py" {line_begin=46 line_end=70 .line-numbers}
