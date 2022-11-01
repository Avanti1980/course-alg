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

##### 递归式求解

---

三种常用的求解方法

- 代入法
- 递归树
- 主方法

<!-- slide vertical=true data-notes="" -->

##### 代入法

---

分两步：

1. 猜测解的形式
2. 用数学归纳法求出解中的常数，并证明解是正确的

<div class="top4"></div>

如何猜测？

- 根据经验，以前是否碰到形式上类似的表达式？
- 根据递归树确定

<!-- slide data-notes="" -->

##### 代入法

---

例：$T(n) = \begin{cases} 1 & n = 1 \\ 2 \cdot T(\lfloor n/2 \rfloor) + n & n > 1 \end{cases}$

这个形式仅比归并排序的递推式多了个向下取整

当$n$很大时取整的影响微乎其微，有理由猜测$T(n) = O(n \lg n)$

下面用数学归纳法证明$T(n) \le c n \lg n$，其中$c$是待定正常数

假设该上界对任意$m < n$都成立，特别的对$\lfloor n/2 \rfloor$也成立

$$
\begin{align*}
    \quad T(n) & = 2 \cdot T(\lfloor n/2 \rfloor) + n \le 2 c \lfloor n/2 \rfloor \lg \lfloor n/2 \rfloor + n \quad \leftarrow \text{归纳假设} \\
    & \le 2 c (n/2) \lg (n/2) + n = cn \lg n - (c-1)n \\
    & \le cn \lg n \quad \leftarrow \text{如果} c \ge 1
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 代入法

---

例：$T(n) = \begin{cases} 1 & n = 1 \\ 2 \cdot T(\lfloor n/2 \rfloor) + n & n > 1 \end{cases}$，求证$T(n) \le c n \lg n$

最后考虑边界条件，当$n=1$时，则$T(n) \le c \lg 1 = 0$

将边界条件替换为$T(2)$、$T(3)$

- $T(2) = 3 \le c 2 \lg 2 \Longrightarrow c \ge 3 / 2$
- $T(3) = 4 \le c 3 \lg 3 \Longrightarrow c \ge 4 / 3 \lg 3$

<div class="top2"></div>

取$c=2$可以使上界对$n=2,3$成立

综上：$T(n) \le 2 n \lg n$对任意$n \ge 2$成立，即$T(n) = O(n \lg n)$

之后不再讨论边界条件的证明细节，取充分大的$c$即可

<!-- slide data-notes="" -->

##### 代入法 

---

例：$T(n) = \begin{cases} 1 & n = 1 \\ 2 \cdot T(\lfloor n/2 \rfloor + 17) + n & n > 1 \end{cases}$

这个形式仅比前一个例子多了个$+17$

当$n$很大时$+17$的影响微乎其微，继续猜测$T(n) \le c n \lg n$

$$
\begin{align*}
    \quad T(n) & = 2 \cdot T(\lfloor n/2 \rfloor + 17) + n \\
    & \le 2 c (\lfloor n/2 \rfloor + 17) \lg (\lfloor n/2 \rfloor + 17) + n \\
    & \le 2 c (n/2 + 17) \lg (n/2 + 17) + n \\
    & = c (n+34) (\lg (n+34) - 1) + n
\end{align*}
$$

<div class="top-2"></div>

出现了$\lg (n+34)$，没法推导下去了

修改猜测为$T(n) \le c (n-t) \lg (n-t)$，其中$t \ge 0$是待定参数

<!-- slide vertical=true data-notes="" -->

##### 代入法 

---

例：$T(n) = \begin{cases} 1 & n = 1 \\ 2 \cdot T(\lfloor n/2 \rfloor + 17) + n & n > 1 \end{cases}$

猜测$T(n) \le c (n-t) \lg (n-t)$，其中$t \ge 0$是待定参数

$$
\begin{align*}
    \quad T(n) & = 2 \cdot T(\lfloor n/2 \rfloor + 17) + n \\
    & \le 2 c (\lfloor n/2 \rfloor + 17) \lg (\lfloor n/2 \rfloor + 17) + n \\
    & \le 2 c (n/2 + 17) \lg (n/2 + 17) + n \\
    & = c (n+34) (\lg (n+34) - 1) + n
\end{align*}
$$

<!-- slide data-notes="" -->

##### 代入法

---

如何猜测递归式？

- 
