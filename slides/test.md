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

##### 活动选择 贪心正确性

---

考虑一般情况，设上一轮$a_k$加入集合$\Acal$

$\Scal_k$表示$a_k$结束后开始的活动集合，它们都与$a_k$兼容

当前轮的问题为在$\Scal_k$中寻找最大兼容活动集合

- 设$a_m$在$\Scal_k$中结束时间最早，即当前轮的贪心选择
- 选择$a_m$后产生的子问题为在$\Scal_m$中寻找最大兼容活动集合$\Acal_m$

<div class="top4"></div>

下面证明{==贪心选择==}与{==子问题的最优解==}合并就是{==原问题的最优解==}

于是从最后一次的贪心选择和最后一个子问题的最优解开始反向合并，直到合并到第一次的贪心选择，即为原问题的最优解

<!-- slide vertical=true data-notes="" -->

##### 活动选择 贪心正确性

---

求证：$\{a_m\} \cup \Acal_m$就是$\Scal_k$的最大兼容活动集合

证明：设$\Acal_k$是$\Scal_k$的最大兼容活动集合，$a_j$在$\Acal_k$中结束最早 (不排除$a_j = a_m$的情况)，注意以下两个事实：

- $a_m$是贪心选择，其结束时间不晚于$a_j$
- $\Acal_k$中的活动都是不相交的，故$\Acal_k \setminus \{a_j\}$与$a_m$兼容

<div class="top1"></div>

若$\Acal_k \setminus \{a_j\}$是$\Scal_m$的最大兼容活动集合，令$\Acal_m = \Acal_k \setminus \{ a_j \}$，于是$\Acal'_k = \{a_m\} \cup \Acal_k \setminus \{ a_j \}$同时也是$\Scal_k$的最大兼容活动集合，命题得证

反设$\Scal_m$存在更大的兼容活动集合，于是$|\Acal_m| > |\Acal_k| - 1$，从而$|\Acal_m \cup \{a_m\}| > |\Acal_k|$，这与$\Acal_k$的最优性矛盾 (最优子结构性)

<!-- slide data-notes="" -->

##### 贪心法的一般步骤

---

<div class="top2"></div>

1. 确定问题的{==最优子结构==}
2. 将问题转化为一系列选择，每次选择后{==只产生一个子问题==}
3. 证明做出贪心选择后，剩余的子问题满足：{==其最优解与前面的贪心选择组合即可得到原问题的最优解==}，换言之，{==存在某个最优解包含贪心选择==}

<div class="top4"></div>

第三步证明思路：

1. 假设最优解不包含贪心选择
2. 对该最优解进行剪切-粘贴，将其一部分替换为贪心选择
3. 证明这样构造出的解也是最优解

<div class="top4"></div>

我的启示 {==最优子结构==}和{==可贪心选择==}是贪心法的两个关键

<!-- slide vertical=true data-notes="" -->

##### 活动选择 贪心正确性

---

根据贪心正确性知存在最大兼容活动集合$\Acal$包含贪心选择$a_1$

贪心选择$a_1$后产生子问题：$\Scal_1$的最大兼容活动集合

根据最优子结构性，$\Acal \setminus \{ a_1 \}$就是$\Scal_1$的最大兼容活动集合
