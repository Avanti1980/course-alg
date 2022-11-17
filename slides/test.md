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

##### 文件编码

---

压缩一个有 10w 个字符的数据文件，只包含 a、b、c、d、e、f

<div class="threelines top0 bottom0">

|   字符   |  a  |  b  |  c  |  d  |  e   |  f   |
| :------: | :-: | :-: | :-: | :-: | :--: | :--: |
|   频率   | 45  | 13  | 12  | 16  |  9   |  5   |
| 定长编码 | 000 | 001 | 010 | 011 | 100  | 101  |
| 变长编码 |  0  | 101 | 100 | 111 | 1101 | 1100 |

</div>

采用二进制字符编码

- 定长编码：3 \* 10w = 30w 个二进制位
- 变长编码：约 22.4w 个二进制位，节约 25%空间

<!-- slide vertical=true data-notes="" -->

##### 最优编码方案

---

变长编码必然是{==前缀码==} (prefix code)

码字{==互不为前缀==}，可以保证解码时无歧义

<div class="threelines top0 bottom0">

| 字符 |  a  |  b  |  c  |  d  |  e   |  f   |
| :--: | :-: | :-: | :-: | :-: | :--: | :--: |
| 频率 | 45  | 13  | 12  | 16  |  9   |  5   |
| 编码 |  0  | 101 | 100 | 111 | 1101 | 1100 |

</div>

文件编码：0101100

文件解码：<span class="red">0</span><span class="green">101</span>{==100==} -> <span class="red">a</span><span class="green">b</span>{==c==}

<!-- slide data-notes="" -->

##### 编码树

---

<div class="top2"></div>

- 每个字符对应一个叶子结点
- 字符的码字由根结点到该字符叶子结点的路径表示

@import "../dot/coding-tree1.dot"

@import "../dot/coding-tree2.dot" {.top-32per .left50per}

<div class="top-10"></div>

左：定长编码树，右：变长编码树

最优编码树必然是满二叉树(右)，每个内部结点有两个子结点

<!-- slide vertical=true data-notes="" -->

##### 最优编码

---

设$C$为字符表，对$\forall c \in C$，令$c.f$为$c$在文件中出现的频率

设$T$为任意前缀编码树，令$d_T(c)$表示字符$c$对应的叶子结点在$T$中的深度，也是$c$的码字的长度

采用编码方案$T$时，文件的编码长度

<div class="top2"></div>

$$
\begin{align*}
    \quad B(T) = \sum_{c \in C} c.f \times d_T(c)
\end{align*}
$$

使得$B(T)$最小的编码称为{==最优编码==}

霍夫曼编码是一种最优编码

<!-- slide data-notes="" -->

##### 霍夫曼编码

---

<div class="threelines left6 righta top-1 bottom0">

| 字符 |  a  |  b  |  c  |  d  |  e  |  f  |
| :--: | :-: | :-: | :-: | :-: | :-: | :-: |
| 频率 | 45  | 13  | 12  | 16  |  9  |  5  |

</div>

@import "../dot/huffman-tree-build1.dot"

@import "../dot/huffman-tree-build2.dot" {.top0}

@import "../dot/huffman-tree-build3.dot" {.top0}

@import "../dot/huffman-tree-build4.dot" {.top-57per .left58per}

@import "../dot/huffman-tree-build5.dot" {.top0 .bottom-4 .left58per}

<!-- slide vertical=true data-notes="" -->

##### 霍夫曼编码

---

最终霍夫曼编码树为

<div class="threelines left20per top-10 bottom-10">

| 字符 |  a  |  b  |  c  |  d  |  e  |  f  |
| :--: | :-: | :-: | :-: | :-: | :-: | :-: |
| 频率 | 45  | 13  | 12  | 16  |  9  |  5  |

</div>

@import "../dot/huffman-tree.dot" {.left-15 .top4}

<!-- slide vertical=true data-notes="" -->

##### 霍夫曼编码

---


最优前缀码对应的树是满二叉树，故必有

- $|C|$个叶子结点
- $|C|-1$个内部结点

<div class="top2"></div>

前缀编码树$T$对文件产生的编码长度$B(T) = \sum_{c \in C} c.freq \cdot d_T(c)$


⑤⑥⑦⑧⑨⑩

