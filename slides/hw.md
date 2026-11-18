<!-- slide data-notes="" -->

##### 作业

---

课外阅读：算法导论 4ed 第四章

习题：2-4、4.3-1、4.4-4、4.5-1、4.5-4



<!-- slide data-notes="" -->

##### 作业

---

算法导论 4ed

计算题：14.2-1、14.4-1、14.5-2

设计题：14.1-3、14-9、14-11

证明题：14.2-5、14.3-5


pdf-merge -i part1-cover.pdf part1-main.pdf part2-cover.pdf part2-main.pdf part3-cover.pdf part3-main.pdf part4-cover.pdf part4-main.pdf part5-cover.pdf part5-main.pdf part6-cover.pdf part6-main1.pdf part6-main2.pdf part7-cover.pdf part7-main.pdf part8-cover.pdf part8-main1.pdf part8-main2.pdf part9-cover.pdf part9-main.pdf -o 第一册-技术资料1.pdf


<!-- slide data-notes="" -->

##### LIS 动态规划 改进

---

维护表$e[]$，初始为空

$e[j]$始终记录当前<span class="blue">长度为</span>$\class{blue}{j}$<span class="blue">的递增子序列的末位元素最小值</span>

<div class="top4"></div>

以$X = [2, 8, 4, 9, 1, 6, 7, 3, 0, 5]$为例，最终$e = [0, 3, 5, 7]$

$e$的长度为 4 代表 LIS 的长度为$4$

$e[-1] = 7$代表 LIS 末位元素为$7$，$[2, 4, 6, 7]$是一个 LIS

<p class="fragment comments"> $e$的元素是单调递增的，这是提升速度的关键</p>

<!-- slide vertical=true data-notes="" -->

##### LIS 动态规划 改进

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

##### LIS 动态规划 改进

---

<span class="blue">在任意时刻</span>$\class{blue}{e}$<span class="blue">都是严格单调递增的</span>，若$i<j$且$e[i] > e[j]$，则有

<p>
\begin{align}
    \lis_i:~ \underbrace{\square ~ \square ~ \cdots ~ \square ~ e[i]}_{\len~=~i}, \quad \lis_j:~ \underbrace{\square ~ \square ~ \square ~ \square ~ \cdots ~ \square ~ \square ~ e[j]}_{\len~=~j}
\end{align}
</p>

去掉$\lis_j$前$j-i$个元素可得长度$i$、末位元素$< e[i]$的递增序列

<div class="top2"></div>

在遍历$X$时，对于$X[i]$

- 若$X[i] > e[-1]$，其可接在当前 LIS 后产生更长的 LIS，$e = [e, [X[i]]$
- 若$e[j-1] < X[i] < e[j]$，其可接在长度为$j-1$的递增子序列后产生长度为$j$末位元素更小的递增子序列，$e[j] = X[i]$，确定$j$可用二分查找

<div class="top2"></div>

二分查找时间复杂度$O(\lg n)$，总时间复杂度$O(n \lg n)$

<!-- slide vertical=true data-notes="" -->

##### LIS 动态规划 改进

---

@import "../codes/dp/lis.py" {line_begin=24 line_end=53 .left2 .line-numbers .top1 .bottom0}
