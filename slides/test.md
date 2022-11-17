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

```dot
digraph g {
    bgcolor=transparent
    rankdir=TB
    graph [ranksep=0.3, nodesep=0.2]
    node [shape=circle, fixedsize=true, width=0.35, color="#586e75", fontcolor="#b58900", fontsize=16, fontname="LXGWWenKai"]
    edge [arrowhead=none, color="#586e75", fontcolor="#268bd2", fontsize=16, fontname="LXGWWenKai", len=0.1]

        100 -> 86 [label="0"]
        100 -> 14 [label="1"]

        86 -> 58 [label="0"]  
        86 -> 28 [label="1"]

        n1 [label="14"]
        14 -> n1 [label="0"]

        node [color="#fdf6e3", fontcolor="#fdf6e3"]
        edge [color="#fdf6e3"]

        14 -> 15

        node [shape=box, width=0.6, height=0.3, color="#586e75", fontcolor="#b58900"]
        edge [color="#586e75"]

        58 -> "a:45" [label="0"]
        58 -> "b:13" [label="1"]
        28 -> "c:12" [label="0"]
        28 -> "d:16" [label="1"]
        n1 -> "e:9" [label="0"]
        n1 -> "f:5" [label="1"]

        node [color="#fdf6e3", fontcolor="#fdf6e3"]
        edge [color="#fdf6e3"]

        15 -> "e:10"
        15 -> "e:11"
}
```

```dot {.top-30 .left50per}
digraph g {
    bgcolor=transparent
    rankdir=TB
    graph [ranksep=0.1, nodesep=0.3]
    edge [arrowhead=none, color="#586e75", fontcolor="#268bd2", fontsize=14, fontname="LXGWWenKai", len=0.1]
    node [shape=circle, fixedsize=true, width=0.35, color="#586e75", fontcolor="#b58900", fontsize=16, fontname="LXGWWenKai"]

    100

    node [shape=box, width=0.6, height=0.3]

    100 -> "a:45" [label="0"]

    node [shape=circle, width=0.4]

    100 -> 55 [label="1"]
    55 -> 25 [label="0"]
    55 -> 30 [label="1"]
    30 -> 14 [label="0"]

    node [shape=box, width=0.6, height=0.3]

    n5 [label="c:12"]
    n6 [label="b:13"]
    25 -> n5 [label="0"]
    25 -> n6 [label="1"]
    n7 [label="d:16"]
    30 -> n7 [label="1"]
    n8 [label="f:5"]
    n9 [label="e:9"]
    n4 -> n8 [label="0"]
    n4 -> n9 [label="1"]
}
```
