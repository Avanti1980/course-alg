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

##### 整数乘法

---

记$x = X[0, \ldots, n-1]$、$y = Y[0, \ldots, n-1]$、$xy = z = Z[0, \ldots, 2n-1]$

<p class="bottom4">
\begin{align}
    \sum_{k=0}^{2n-1} Z[k] 10^k & = \left( \sum_{i=0}^{n-1} X[i] 10^i \right) \left( \sum_{j=0}^{n-1} X[j] 10^j \right) \\
    & = \sum_{i=0}^{n-1} \sum_{j=0}^{n-1} X[i] Y[j] 10^{i+j} = \sum_{k=0}^{2n-2} \underbrace{\class{blue}{\sum_{(i,j): i+j=k} X[i] Y[j]}}_{c_k} 10^k
\end{align}
</p>

- 左：$10^k$的线性组合，组合系数$Z[k]$是一位正整数
- 右：$10^k$的线性组合，组合系数$c_k$是若干个一位正整数的乘积

<div class="top2"></div>

$Z[k]$和$c_k$之间的关系？

<!-- slide data-notes="" -->

##### 小学算法

---

已知$\sum_{k=0}^{2n-1} Z[k] 10^k = \sum_{k=0}^{2n-2} c_k 10^k$，其中

- $Z[k]$是一位正整数
- $c_k = \sum_{(i,j): i+j=k} X[i] Y[j]$是若干个一位正整数的乘积

<div class="top2"></div>

$c_0 = \sum_{(i,j): i+j=0} X[i] Y[j] = X[0] Y[0]$

- $c_0 \bmod 10$：就是$Z[0]$
- $h \gets \lfloor c_0 / 10 \rfloor$：作为进位参与$Z[1]$的计算

<div class="top2"></div>

$c_1 = \sum_{(i,j): i+j=1} X[i] Y[j] = X[0] Y[1] + X[1] Y[0]$，再加上进位$h$

- $(c_1 + h) \bmod 10$：就是$Z[1]$
- $h \gets \lfloor (c_1 + h) / 10 \rfloor$：作为进位参与$Z[2]$的计算

<div class="top2"></div>

如此迭代，继续计算$Z[2], Z[3], \ldots, Z[2n-1]$

<!-- slide vertical=true data-notes="" -->

##### 小学算法

---

以$x = 123$、$y = 456$、$z = 56088$为例

<div class="threelines left4 righta top-2 bottom0">

| $c_k$                                             |         $h$         |      $c_k + h$       |   $Z[k]$   |
| :------------------------------------------------ | :-----------------: | :------------------: | :--------: |
| $c_0 = 3 \times 6 = 18$                           |         $0$         |  $\class{red}{1}8$   | $Z[0] = 8$ |
| $c_1 = 3 \times 5 + 2 \times 6 = 27$              |  $\class{red}{1}$   | $\class{yellow}{2}8$ | $Z[1] = 8$ |
| $c_2 = 3 \times 4 + 2 \times 5 + 1 \times 6 = 28$ | $\class{yellow}{2}$ |  $\class{blue}{3}0$  | $Z[2] = 0$ |
| $c_3 = 2 \times 4 + 1 \times 5 = 13$              |  $\class{blue}{3}$  |  $\class{cyan}{1}6$  | $Z[3] = 6$ |
| $c_4 = 1 \times 4 = 4$                            |  $\class{cyan}{1}$  |         $5$          | $Z[4] = 5$ |

</div>

<img src="../tikz/integer-multiplication/integer-multiplication.svg" class="right6 lefta width25 top-28per">

<!-- slide vertical=true data-notes="" -->

##### 小学算法

---

输入：$X[0, \ldots, n-1]$、$Y[0, \ldots, n-1]$

<div class="top-2"></div>

输出：$Z[0, \ldots, 2n-1]$

1. 初始化进位$c \gets 0$
2. ==for== $k = 0 \rightarrow 2n-1$
3. &emsp;&emsp;==for each== 二元组$(i,j): i+j=k$ ==do==
4. &emsp;&emsp;&emsp;&emsp;$c \gets c + X[i] Y[j]$
5. &emsp;&emsp;==end for==
6. &emsp;&emsp;$Z[k] = c \bmod 10$
7. &emsp;&emsp;下一位进位$c \gets \lfloor c/10 \rfloor$
8. ==end for==

<div class="top2"></div>

二重循环共遍历$n^2$个$(i,j)$二元组，因此$T(n) = \Theta(n^2)$

<!-- slide vertical=true data-notes="" -->

##### 小学算法 实现

---

@import "../codes/dc/integer-multiplication.py" {line_begin=20 line_end=47 .left4 .line-numbers .top1 highlight=[4,7]}

<!-- slide data-notes="" -->

##### 整数乘法 分治

---

将$x$和$y$的数位二等分，记$m = n/2$

- $a = X[0, \ldots, n-m-1]$、$b = X[n-m, \ldots, n-1]$，$x = a \cdot 10^m + b$
- $c = Y[0, \ldots, n-m-1]$、$d = Y[n-m, \ldots, n-1]$，$y = c \cdot 10^m + d$

<div class="top2"></div>

乘积$z = xy = (a \cdot 10^m + b)(c \cdot 10^m + d) = a c \cdot 10^{2m} + (a d + b c) 10^m + b d$

- 乘法：$4$个$n/2$位数相乘，$ac$、$ad$、$bc$、$bd$
- 补零：$ac$后补$n$个、$a d + b c$前后各补$n/2$个，$bd$前补$n$个，共补$3n$个
- 加法：$3$个$2n$位数相加，一重循环遍历，逐位相加，共$4n$个加法

<div class="top2"></div>

设$n$位数相乘的时间为$T(n)$，补零、加法的时间为$c_1$、$c_2$

<p>
\begin{align}
    T(n) = 4 \cdot T (n/2) + c_1 \cdot 3n + c_2 \cdot 4n = 4 \cdot T (n/2) + \Theta(n)
\end{align}
</p>

<!-- slide vertical=true data-notes="" -->

##### 整数乘法 分治

---

<p>
\begin{align}
    T(n) = \begin{cases} 1, & n = 1 \\ 4 \cdot T(n/2) + c n, & n > 1 \end{cases}
\end{align}
</p>

代入式$(\diamondsuit)$，注意$a = 4$、$b = 2$、$d = 1$，故$a \ne b^d$、$\log_b a = 2$

<p>
\begin{align}
    T(n) & = n^{\log_b a} \cdot T(1) + c \cdot (n^d - n^{\log_b a})/(1 - a/b^d) \\
    & = n^2 \cdot T(1) + c \cdot (n^1 - n^2)/(1 - 4 / 2^1) \\
    & = \Theta(n^2)
\end{align}
</p>

分解成$4$个规模大致减半的子问题并不改进时间复杂度

<!-- slide data-notes="" -->

##### Karatsuba 算法

---

利用$a d + b c = (a+b) (c+d) - a c - b d$可得

<p>
\begin{align}
    x y = a c \cdot 10^{2m} + ((a+b) (c+d) - a c - b d) \cdot 10^m + b d
\end{align}
</p>

$n/2$位数相乘减少为$3$个：$(a+b) (c+d)$、$a c$、$b d$，补零不变，加法次数变多但时间复杂度依然为$\Theta(n)$

<p>
\begin{align}
    T(n) = 3 \cdot T (n/2) + \Theta(n)
\end{align}
</p>

<div class="top2"></div>

代入式$(\diamondsuit)$，注意$a = 3$、$b = 2$、$d = 1$，故$a \ne b^d$、$\log_b a = \lg 3$

<p>
\begin{align}
    T(n) & = n^{\log_b a} \cdot T(1) + c \cdot (n^d - n^{\log_b a})/(1 - a/b^d) \\
    & = n^{\lg 3} \cdot T(1) + c \cdot (n^1 - n^{\lg 3})/(1 - 3/2^1) \\
    & = \Theta(n^{\lg 3}) \approx \Theta(n^{1.58496250})
\end{align}
</p>

分解成$3$个规模大致减半的子问题可以改进时间复杂度

<!-- slide vertical=true data-notes="" -->

##### Karatsuba 算法 实现

---

@import "../codes/dc/integer-multiplication.py" {line_begin=49 line_end=67 .left4 .line-numbers .top1 highlight=[19-21,37]}

<!-- slide data-notes="" -->

##### 整数乘法 时间对比

---

<img src="../codes/dc/integer-multiplication-karatsuba.svg" class="center width75 top2 bottom-4">

<!-- slide data-notes="" -->

##### Toom 算法

---

将$x$和$y$的数位三等分，记$m = n/3$

<p>
\begin{align}
    x & = a \cdot 10^{2m} + b \cdot 10^m + c \\
    y & = d \cdot 10^{2m} + e \cdot 10^m + f
\end{align}
</p>

于是

<p>
\begin{align}
    xy = a d \cdot 10^{4m} + (a e + b d) \cdot 10^{3m} & + (af + be + cd) \cdot 10^{2m} \\
    & + (bf + ce) \cdot 10^m + cf
\end{align}
</p>

<p class="fragment">共产生$9$个子问题，有点难办！</p>

<!-- slide vertical=true data-notes="" -->

##### Toom 算法

---

引入多项式$x(t) = a t^2 + b t + c$、$y(t) = d t^2 + e t + f$

<p>
\begin{align}
    x(t) y(t) & = a d \cdot t^4 + (a e + b d) \cdot t^3 + (af + be + cd) \cdot t^2 + (bf + ce) \cdot t + cf \\
    & \triangleq w(t) = w_4 t^4 + w_3 t^3 + w_2 t^2 + w_1 t + w_0 
\end{align}
</p>

代入$t = 10^m$ (在系数后面分别添加$4m$、$3m$、$2m$、$m$、$0$个$0$再相加) 就是$xy$，剩下只需确定$w(t)$的$5$个系数

令$t$取$5$个不同的值可得$5$变量线性方程组：

<p>
\begin{align}
    \begin{array}{lrcl}
        t = 0      : & cf                 & = & w_0                                  \\
        t = 1      : & (a+b+c)(d+e+f)     & = & w_4 + w_3 + w_2 + w_1 + w_0          \\
        t = -1     : & (a-b+c)(d-e+f)     & = & w_4 - w_3 + w_2 - w_1 + w_0          \\
        t = 2      : & (4a+2b+c)(4d+2e+f) & = & 16 w_4 + 8 w_3 + 4 w_2 + 2 w_1 + w_0 \\
        t = \infty : & ad                 & = & w_4
    \end{array}
\end{align}
</p>

<!-- slide vertical=true data-notes="" -->

##### Toom 算法

---

方程组涉及$5$个乘法子问题：

<p>
\begin{align}
    \begin{array}{l}
    s_4 \triangleq ad \\
    s_3 \triangleq (4a+2b+c)(4d+2e+f) \\
    s_2 \triangleq (a-b+c)(d-e+f) \\
    s_1 \triangleq (a+b+c)(d+e+f) \\
    s_0 \triangleq cf
    \end{array} \Longrightarrow
    \begin{array}{l}
    w_4 = s_4                                                           \\
    w_3 = (-12 s_4 + s_3 - s_2 - 3 s_1 + 3 s_0) / 6  \\
    w_2 = (-2 s_4 + s_2 + s_1 - 2 s_0) / 2                   \\
    w_1 = (12 s_4 - s_3 - 2 s_2 + 6 s_1 - 3 s_0) / 6 \\
    w_0 = s_0
    \end{array}
\end{align}
</p>

由此可得$T(n) = 5 \cdot T (n/3) + \Theta(n)$

代入式$(\diamondsuit)$，注意$a = 5$、$b = 3$、$d = 1$，故$a \ne b^d$、$\log_b a = \log_3 5$

<p>
\begin{align}
    T(n) & = n^{\log_b a} \cdot T(1) + c \cdot (n^d - n^{\log_b a})/(1 - a/b^d) \\
    & = n^{\log_3 5} \cdot T(1) + c \cdot (n^1 - n^{\log_3 5})/(1 - 5/3^1) = \Theta(n^{\log_3 5}) \approx \Theta(n^{1.46497352})
\end{align}
</p>

比 Karatsuba 算法的$\Theta(n^{\lg_3}) \approx \Theta(n^{1.58496250})$更优

<!-- slide vertical=true data-notes="" -->

##### Toom 算法 实现

---

@import "../codes/dc/integer-multiplication.py" {line_begin=69 line_end=104 .left4 .line-numbers .top1 highlight=[]}

<!-- slide data-notes="" -->

##### 整数乘法 时间对比

---

<img src="../codes/dc/integer-multiplication-all.svg" class="center .width75 .top2 .bottom-4">

<!-- slide vertical=true data-notes="" -->

##### 一般性结论

---

将$x$、$y$作$k$等分，引入多项式

<p>
\begin{align}
    x(t) = a_{k-1} t^{k-1} + a_{k-2} t^{k-2} + \cdots + a_0, \quad y(t) = b_{k-1} t^{k-1} + b_{k-2} t^{k-2} + \cdots + b_0
\end{align}
</p>

<p>
\begin{align}
    x(t) y(t) & = a_{k-1} b_{k-1} \cdot t^{2k-2} + (a_{k-1} b_{k-2} + a_{k-2} b_{k-1}) \cdot t^{2k-3} + \cdots + a_0 b_0 \\
    & \triangleq w(t) = w_{2k-2} t^{2k-2} + w_{2k-3} t^{2k-3} + \cdots + w_0 
\end{align}
</p>

$w(t)$共有$2k-1$个系数，故$t$需取$2k-1$个不同的值，由此产生$2k-1$个规模为$n/k$的子问题，代入式$(\diamondsuit)$，注意$a = 2k-1$、$b = k$、$d = 1$，故$a \ne b^d$、$\log_b a = \log_k (2k-1)$

<p>
\begin{align}
    T(n) & = n^{\log_b a} \cdot T(1) + c \cdot (n^d - n^{\log_b a})/(1 - a/b^d) \\
    & = n^{\log_k (2k-1)} \cdot T(1) + c \cdot (n^1 - n^{\log_k (2k-1)})/(1 - (2k-1) / k^1) \\
    & = \Theta(n^{\log_k (2k-1)})
\end{align}
</p>

<p class="footnote hand"> Karatsuba 算法和 Toom 算法都是该结论的特例，易证$\log_k (2k-1)$关于$k$严格单调减，故$k$越大越好，但$k$越大，关于$w(t)$的$2k-1$个系数的线性方程组也越复杂，实际需取一个适中的$k$</p>
