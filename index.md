@import "css/theme/solarized.css"
@import "css/index.css"

## 算法设计与分析 <span style="font-weight:800">2025</span> 秋

---

#### 概况

授课：张腾 _tengzhang@hust.edu.cn_

地点：西十二楼 S308、西十二楼 S204

32 学时

- 第 9 ~ 10 周：周一 5 ~ 6 节课、周三 1 ~ 2 节课 (西十二楼 S308)
- 第 11 ~ 16 周：周一 3 ~ 4 节课 (西十二楼 S204)、周三 3 ~ 4 节课 (西十二楼 S308)

<div class="top-2"></div>

#### 考核

期末考试 (70%)、平时作业 (30%)

#### 课件

在线浏览，Space 翻页，Esc 导航，可能需要{==科学上网==}

<div class="threelines outline head-highlight">

|        |                讲义                |                                             补充                                             |
| :----: | :--------------------------------: | :------------------------------------------------------------------------------------------: |
| 第一讲 |       [绪论](slides/01.html)       |                                              -                                               |
| 第二讲 |    [函数的增长](slides/02.html)    |                                              -                                               |
| 第三讲 |       [分治](slides/03.html)       |                     [Strassen 矩阵乘法加速](notes/Strassen/Strassen.pdf)                     |
| 第四讲 |     [动态规划](slides/04.html)     |                                              -                                               |
| 第五讲 |       [贪心](slides/05.html)       |                                              -                                               |
| 第六讲 |   [单源最短路径](slides/06.html)   |                                              -                                               |
| 第七讲 | [全结点对最短路径](slides/07.html) |                                              -                                               |
| 第八讲 |       [回溯](slides/08.html)       |                                              -                                               |
| 第九讲 |     [分支限界](slides/09.html)     |                                              -                                               |
| 第十讲 |     [迭代改进](slides/10.html)     | [匹配、覆盖、流、割](notes/MCFC/MCFC.pdf)，[线性规划](notes/Max-Flow/linear-programming.pdf) |

</div>

#### 资料

<span style="font-size:1.8rem;font-style:italic">Introduction to Algorithms</span> [3ed](<books/Introduction%20to%20Algorithms%20(3ed)%20-%20Thomas%20H.%20Cormen,%20Charles%20E.%20Leiserson,%20Ronald%20L.%20Rivest,%20Clifford%20Stein.pdf>) [4ed](<books/Introduction%20to%20Algorithms%20(4ed)%20-%20Thomas%20H.%20Cormen,%20Charles%20E.%20Leiserson,%20Ronald%20L.%20Rivest,%20Clifford%20Stein.pdf>)
Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein

#### 代码

[n 位整数乘法](codes/intro/integer-multiplication.ipynb)、[最大公约数](codes/intro/gcd.ipynb)、[排序](codes/intro/sorting.ipynb)
[最大子数组](codes/dc/max-subarray.ipynb)、[逆序对计数](codes/dc/count-inverse-pair.ipynb)、[最近点对](codes/dc/closest-pair.ipynb)、[矩阵加法](codes/dc/matrix-addition.ipynb)、[矩阵乘法](codes/dc/matrix-multiply.ipynb)
[斐波那契数](codes/dp/fibo.ipynb)、[钢条切割](codes/dp/cut-rod.ipynb)、[子集和数](codes/dp/subset-sum-dp.ipynb)、[矩阵连乘](codes/dp/matrix-chain.ipynb)、[最长公共子序列](codes/dp/lcs.ipynb)、[编辑距离](codes/dp/edit-distance.ipynb)、[最长递增子序列](codes/dp/lis.ipynb)、[最优二叉搜索树](codes/dp/optiaml-bst.ipynb)
[最大兼容活动集合](codes/greedy/activity-selector.ipynb)、[霍夫曼编码](codes/greedy/huffman.ipynb)、[最小生成树](codes/greedy/mst.ipynb)
[Bellman-Ford](codes/sssp/bellman-ford.ipynb)、[Dijkstra](codes/sssp/dijkstra-all.ipynb)、[Floyd-Warshall 等动态规划算法](codes/apsp/sp-all-dp.ipynb)、[传递闭包](codes/apsp/transitive-closure.ipynb)、[Johnson](codes/apsp/sp-all-johnson.ipynb)
[n 皇后](codes/backtrack-bb/nqueen.ipynb)、[哈密顿回路](codes/backtrack-bb/hamilton.ipynb)、[子集和数 定长元组](codes/backtrack-bb/subset-sum-fix-len.ipynb)、[子集和数 变长元组](codes/backtrack-bb/subset-sum-var-len.ipynb)
[Ford-Fulkerson](codes/flow/ford-fulkerson.ipynb)
