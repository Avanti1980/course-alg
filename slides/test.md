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

##### 最优二叉搜索树

---

语言翻译，英译汉，对每个单词，在单词表里找到该词

<div class="top-2"></div>

有的词能找到对应的汉语词汇，有的找不到

<div class="twolines row2-border-top-solid fs16 top-2 bottom-2">

| When | you | play | the | game  | of  | thrones |   ,    |  you   | win |
| :--: | :-: | :--: | :-: | :---: | :-: | :-----: | :----: | :----: | :-: |
|  当  | 你  |  玩  |  >  | 游戏  | 的  |  权力   |   ,    |   你   | 赢  |
|  or  | you | die  |  .  | There | is  |   no    | middle | ground |  .  |
|  或  | 你  |  死  |  ,  |   >   | 有  |   没    |  中间  |  地带  |  .  |

</div>

{==Daenerys Stormborn==} of House {==Targaryen==}, the First of Her Name, Queen of the {==Andals==}, the {==Rhoynar==} and the {==First Men==}, Queen of {==Meereen==}, Protector of the Realm, Lady Regnant of the Seven Kingdoms, Mother of Dragons, {==Khaleesi==} of the Great Grass Sea, the Unburnt, Breaker of Chains.

<!-- slide vertical=true data-notes="" -->

##### 最优二叉搜索树

---

方法：以英语单词作为关键字构建二叉搜索树

<div class="top-2"></div>

目标：尽快找到英语单词，使{==期望==}搜索时间最少

<div class="top-2"></div>

特点：

- 第$i$层的关键字需比较$i$次才能找到
- 左子树的所有元素比根结点小
- 右子树的所有元素比根结点大
- 左、右子树也是二叉搜索树

@import "../dot/binary-search-tree.dot" {.left30per .top-12}

<!-- slide vertical=true data-notes="" -->

##### 最优二叉搜索树

---

频繁使用的单词应尽可能靠近根，减少比较次数

<div class="top-2"></div>

不在词典中的情况也要纳入考虑，引入伪关键字$d_i = (k_i, k_{i+1})$

<div class="top-2"></div>

输入：

- $n$个排好序的关键字$k_1 < k_2 < \ldots < k_n$，$\Pbb [x = k_i] = p_i$
- $n+1$个伪关键字$d_0, d_1, \ldots, d_n$，$\Pbb [x \in d_i] = q_i$

<div class="top2"></div>

输出：以$k_1, k_2, \ldots k_n$为内部结点，以$d_0, d_1, \ldots, d_n$为叶子结点的最优二叉搜索树$T$，使得如下的期望搜索时间最少

$$
\begin{align*}
    \quad \Ebb[\text{search time in } T] & = \sum_{i=1}^n (\dep (k_i) + 1) \cdot p_i + \sum_{i=0}^n (\dep (d_i) + 1) \cdot q_i \\
    & = 1 + \sum_{i=1}^n \dep (k_i) \cdot p_i + \sum_{i=0}^n \dep (d_i) \cdot q_i
\end{align*}
$$

<!-- slide data-notes="" -->

##### 最优二叉搜索树 例子

---

设有$n = 5$个关键字，$6$个伪关键字，$\sum_{i=1}^n p_i + \sum_{i=0}^n q_i = 1$

<div class="threelines top-2 bottom-2">

|  $i$  |   0    |  1   |  2   |  3   |  4   |  5   |
| :---: | :----: | :--: | :--: | :--: | :--: | :--: |
| $p_i$ | &zwnj; | 0.15 | 0.10 | 0.05 | 0.10 | 0.20 |
| $q_i$ |  0.05  | 0.10 | 0.05 | 0.05 | 0.05 | 0.10 |

</div>

@import "../dot/binary-search-tree-example.dot" {.center .top1 .bottom-4}
