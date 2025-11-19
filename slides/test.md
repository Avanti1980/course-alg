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

##### 文件编码

---

压缩一个只包含$a$、$b$、$c$、$d$、$e$、$f$的$100$个字符的数据文件

<div class="threelines top-1 bottom1">

|   字符   |  $a$  |  $b$  |  $c$  |  $d$  |  $e$   |  $f$   |
| :------: | :---: | :---: | :---: | :---: | :----: | :----: |
|   频率   | $45$  | $13$  | $12$  | $16$  |  $9$   |  $5$   |
| 定长编码 | $000$ | $001$ | $010$ | $011$ | $100 $ | $101$  |
| 变长编码 |  $0$  | $101$ | $100$ | $111$ | $1101$ | $1100$ |

</div>

- 定长编码：$3 \cdot 100 = 300$个二进制位
- 变长编码：$1 \cdot 45 + 3 \cdot 13 + 3 \cdot 12 + 3 \cdot 16 + 4 \cdot 9 + 4 \cdot 5 = 224$个二进制位，节省$25.3\%$空间

<p class="fragment top4">问题：最优编码方案？</p>

<!-- slide vertical=true data-notes="" -->

##### 编码树

---

任何二进制编码都可以表示成一个二叉树，根节点到字符结点路径上遇到的$01$串就是其编码，以表示$a$、$b$、$c$、$d$四字符为例

- 左：$a:0$、$b:00$、$c:1$、$d:11$，$a$的编码是$b$的前缀，解码时有歧义
- 中：$a:00$、$b:01$、$c:10$、$d:11$，等长编码，解码时无歧义
- 右：$a:0$、$b:10$、$c:110$、$d:111$，变长编码，解码时无歧义

@import "../tikz/huffman/coding-tree-exam-4-char.svg" {.center .width60 .top5 .bottom-5}

解码：以右图方案为例，<span class="red">0</span><span class="green">10</span>{==110==} -> <span class="red">a</span><span class="green">b</span>{==c==}

<!-- slide vertical=true data-notes="" -->

##### 最优非前缀编码树

---

输入：长度$n \ge 2$的字符表$\Ccal$，每个字符$c$的频率$c.f$

输出：最优非前缀编码树

<p class="fragment" data-fragment-index="1">每个字符对应一个叶结点，否则不是非前缀码</p>

<p class="fragment" data-fragment-index="2">字符$c$的编码长度是其在编码树$\Tcal$中的深度$d_{\Tcal}(c)$</p>

<p class="fragment" data-fragment-index="3">所有字符的总编码长度$B(\Tcal) = \sum_{c \in \Ccal} c.f \cdot d_{\Tcal}(c)$</p>

<p class="fragment" data-fragment-index="4">最优编码树必然是满二叉树，每个内部结点有两个子结点</p>

<p class="fragment" data-fragment-index="5">输出：平均叶结点深度最小的满二叉树</p>

@import "../tikz/huffman/coding-tree-exam-not-full.svg" {.width15 .top-45 .lefta .right8 .bottom-5 .fragment data-fragment-index="4"}

<!-- slide data-notes="" -->

##### 霍夫曼算法

---

基本想法：维护一个森林，每次合并两棵树，合并会导致树中结点深度$+1$，总编码长度$B(\Tcal)$增量为两棵树中叶结点的频率和

霍夫曼算法的贪心选择：合并频率最低的两棵树

@import "../tikz/huffman/coding-tree-huffman.svg" {.center .width92 .top4 .bottom-5}

<p class="footnote book"> 霍夫曼算法来自他在 MIT 攻读博士学位时修读的信息论课程的学期报告：最有效的二进制编码，老师法诺曾提出自顶向下构建树的香农-范诺编码，霍夫曼使用自底向上构建树得到了更优的编码。</p>

<!-- slide vertical=true data-notes="" -->

##### 时间复杂度

---

简单实现：每次合并两棵树，共合并$\Theta(n)$次，每次合并需要查找频率最低的两棵树，线性查找$\Theta(n)$，因此总时间复杂度$\Theta(n^2)$

<p class="fragment" data-fragment-index="1">高级实现：利用堆或优先队列，查找的时间可以变为常数，但初始构建堆或优先队列需$\Theta(n \lg n)$、每次合并完维护堆或优先队列需$\Theta(\lg n)$，因此总时间复杂度$\Theta(n \lg n)$</p>

<!-- slide data-notes="" -->

##### 算法正确性

---

设$x$和$y$是$\Ccal$中频率最低的两个字符，则存在最优编码树，$x$和$y$是其中一对最深的兄弟叶子结点

证明：反设$\Tcal$是最优编码树，$x$和$y$不是一对兄弟叶子结点

将$x$和$y$与$\Tcal$中最深的一对兄弟叶子结点$a$和$b$交换会如何？

@import "../dot/huffman-proof1.dot" {.top4 .left8}

@import "../dot/huffman-proof2.dot" {.center .top-26per}

@import "../dot/huffman-proof3.dot" {.lefta .right8 .top-26per}

<!-- slide vertical=true data-notes="" -->

##### 算法正确性

---

设$a$、$x$交换后的新树为$\Tcal'$，$d_{\Tcal'}(a) = d_{\Tcal}(x)$、$d_{\Tcal'}(x) = d_{\Tcal}(a)$

<div class="top-2"></div>

不难证明$\Tcal'$也是最优编码树，同理再将$b$、$y$交换后依然还是

$$
\begin{align*}
    \quad \Delta B(\Tcal) & = a.f \times d_{\Tcal'}(a) + x.f \times d_{\Tcal'}(x) - a.f \times d_{\Tcal}(a) - x.f \times d_{\Tcal}(x) \\
    & = a.f \times d_{\Tcal}(x) + x.f \times d_{\Tcal}(a) - a.f \times d_{\Tcal}(a) - x.f \times d_{\Tcal}(x) \\
& = \underbrace{(a.f - x.f)}_{\ge ~ 0} \underbrace{(d_{\Tcal}(x) - d_{\Tcal}(a))}_{\le ~ 0} \le 0
\end{align*}
$$

@import "../dot/huffman-proof1.dot" {.top-1 .left8}

@import "../dot/huffman-proof2.dot" {.center .top-26per}

<div class="top0 bottom-32"></div>

$$
\begin{align*}
    \quad \qquad \quad \Tcal \qquad \qquad \qquad \qquad \quad \quad \Tcal'
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 算法正确性

---

设$\Ccal' = \Ccal \setminus \{ x,y \} \cup \{ z \}$，$z.f = x.f + y.f$，其它字符频率不变

设$\Tcal'$是$\Ccal'$的任一最优编码树，将$\Tcal'$中$z$对应的叶子结点替换为以$x$、$y$为子结点的内部结点，则得到的树$\Tcal$是$\Ccal$的一个最优编码树

@import "../dot/huffman-proof4.dot" {.top4 .left25}

@import "../dot/huffman-proof5.dot" {.top-20per .right30 .lefta .bottom-30}

<div class="top0 bottom0"></div>

$$
\begin{align*}
    \quad \qquad \qquad \qquad \qquad \Tcal' \qquad \qquad \qquad \qquad \quad ~ \Tcal
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 最优子结构

---

证明：反设$\Tcal$不是$\Ccal$的最优编码树

最优编码树为$\Tcal''$，于是$B(\Tcal'') < B(\Tcal)$

将$\Tcal''$中的$x$、$y$和它们的父节点整体替换成$z$，得到$\Tcal'''$

注意合并只会导致$x$、$y$的深度$-1$，因此总编码长度$B(\Tcal)$的变化量就是$x.f + y.f$

$B(\Tcal''') = B(\Tcal'') - x.f - y.f$、$B(\Tcal) = B(\Tcal') + x.f + y.f$

两式相加可得$B(\Tcal''') = B(\Tcal'') - B(\Tcal) + B(\Tcal') < B(\Tcal')$

故$\Tcal'$不可能是$\Ccal'$的最优编码树，矛盾！
