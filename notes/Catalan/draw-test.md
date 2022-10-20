```python {cmd="/usr/bin/python"}
N=8
print("以下代码输出前%d个卡特兰数" % (N))
catalan=1
for i in range(1,N+1,1):
    print(i-1, int(catalan))
    catalan = catalan * (4*i-2) / (i+1)
```

```python {cmd=true matplotlib=true}
import matplotlib.pyplot as plt
plt.plot([1,2,3, 4])
plt.show() # show figure
```

```gnuplot {cmd=true output="html"}
set xlabel "月份"
set ylabel "降水量"
set y2label "气温"
set ytics nomirror
set y2tics
set title '降水量与气温'
set xrange [0.5:12.5]
set xtics 1,1,12 
set grid xtics ytics
set term pdfcairo lw 2 font "OperatorLXGW,14"
set samples 50
set output "a.pdf"
plot "a.dat" u 1:2 w lp lc rgbcolor "#b58900" lw 1 pt 7 ps 0.5 axis x1y1 t "北京", "a.dat" u 1:3 w lp lc rgbcolor "#268bd2" lw 1 pt 9 ps 0.5 dt 5 axis x1y2 t "上海"
set output
```

@import "a.pdf"

```latex {cmd=true hide=true}
\documentclass[margin=10pt]{standalone}
\usepackage{tikz}
\usepackage{bm}
\usetikzlibrary{backgrounds,automata,shapes,decorations.pathmorphing,decorations.pathreplacing,decorations.markings,decorations.shapes,arrows,arrows.meta,chains,positioning,calc}
\begin{document}
\begin{tikzpicture}
    \path (-1.3,2.8) node () {$\bm{w}^\top \bm{x} = 0$};
    \draw [smooth,thick] (-3.5,0) circle (0.1);
    \draw [smooth,thick] (-2.35,2) circle (0.1);
    \draw [smooth,thick] (-2.3,-0.3) circle (0.1);
    \draw [smooth,thick] (-2.5,-2) circle (0.1);
    \draw [smooth,thick] (-2,-1) circle (0.1);
    \draw [smooth,thick] (-2,0.5) circle (0.1);
    \draw [smooth,thick] (-1.05,-0.5) circle (0.1);
    \draw [smooth,thick] (1.1,0.55) rectangle ++(0.18,0.18);
    \draw [smooth,thick] (2.6,1.5) rectangle ++(0.18,0.18);
    \draw [smooth,thick] (2.4,-2) rectangle ++(0.18,0.18);
    \draw [smooth,thick] (2,0) rectangle ++(0.18,0.18);
    \draw [smooth,thick] (2.5,-0.2) rectangle ++(0.18,0.18);
    \draw [smooth,thick] (2.9,-1.5) rectangle ++(0.18,0.18);
    \draw [smooth,thick] (3.2,0.8) rectangle ++(0.18,0.18);
    \draw [>=stealth] (-1,-0.5) -- (0.07, 0.07);
    \draw [>=stealth] (1.14, 0.64) -- (0.07, 0.07);
    \path (-0.6,0) node () {$\gamma$};
    \path (0.5,0.55) node () {$\gamma$};
    \draw [smooth,thick] (-1.2,2.454) -- (1.35, -2.3328);
    \draw [smooth,thick,dashed] (0.2,2.454) -- (2.75, -2.3328);
    \draw [smooth,thick,dashed] (-2.6,2.454) -- (-0.05, -2.3328);
\end{tikzpicture}
\end{document}
```
