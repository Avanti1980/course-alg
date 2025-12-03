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

<!-- slide vertical=true data-notes="" -->

##### 动态规划 改进

---

将长度为$m$的路径拆分为长度为$m-1$的路径和边

$$
\begin{align*}
    \quad \ell_{ij}^{(m)} = \begin{cases} \infty, & m = 0 \\ \min_k \{ \ell_{ik}^{(m-1)} + w_{kj} \}, & m \ge 1 \end{cases}
\end{align*}
$$

将长度为$m$的路径拆分为$2$条长度为$m/2$的路径

$$
\begin{align*}
    \quad \ell_{ij}^{(m)} = \begin{cases} w_{ij}, & m = 1 \\ \min_k \{ \ell_{ik}^{(m/2)} + \ell_{kj}^{(m/2)} \}, & m = 2,4,8, \ldots \end{cases}
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 动态规划 改进

---

当$m \ge n-1$后$\Lv^{(m)}$不再变化，因此$m$不断乘$2$直至达到$n-1$，前驱矩阵的更新也有变化

@import "../codes/sp-all-dp.py" {line_begin=26 line_end=40 .left4 .line-numbers .top1 highlight=[4-5,10-13]}

<!-- slide vertical=true data-notes="" -->

##### 动态规划 改进

---

与矩阵平方的联系

```python {.left4 .line-numbers .top-1 .bottom2}
for i in range(n):
    for j in range(n):
        a[i,j] = 0
        for k in range(n):
            a[i,j] = a[i,j] + aa[i,k] * aa[k,j]

for i in range(n):
    for j in range(n):
        l[i,j] = float("inf")
        for k in range(n):
            l[i,j] = min(l[i,j], ll[i,k] + ll[k,j])
```

该改进算法本质上与计算矩阵幂次时不断平方相同
