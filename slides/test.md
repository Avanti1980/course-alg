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

##### 单源最短路径 小结

---

<div class="threelines row2-border-top-dashed bottom-2">

|    &zwnj;    |   方法   |    条件    |    实现    |                       一般时间复杂度                        |
| :----------: | :------: | :--------: | :--------: | :---------------------------------------------------------: |
| Bellman-Ford | 动态规划 | 可以有负边 |   &zwnj;   |            $\Theta(\shu\Vcal\shu \shu\Ecal\shu)$            |
|   Dijkstra   |  贪心法  | 必须无负边 |  线性数组  |          $\Theta(\shu\Vcal\shu^2 + \shu\Ecal\shu)$          |
|      ^       |    ^     |     ^      |   二叉堆   | $\Theta((\shu\Vcal\shu + \shu\Ecal\shu) \lg \shu\Vcal\shu)$ |
|      ^       |    ^     |     ^      | 斐波那契堆 |  $\Theta(\shu\Vcal\shu \lg \shu\Vcal\shu + \shu\Ecal\shu)$  |

</div>

Bellman-Ford 算法可检测负环，进一步考虑图的稀疏性有

<div class="threelines row2-border-top-dashed top-2">

|    &zwnj;    |    实现    |                       一般时间复杂度                        |                   稠密图                    |                  稀疏图                   |
| :----------: | :--------: | :---------------------------------------------------------: | :-----------------------------------------: | :---------------------------------------: |
| Bellman-Ford |   &zwnj;   |            $\Theta(\shu\Vcal\shu \shu\Ecal\shu)$            |          $\Theta(\shu\Vcal\shu^3)$          |         $O(\shu\Vcal\shu^2)$         |
|   Dijkstra   |  线性数组  |          $\Theta(\shu\Vcal\shu^2 + \shu\Ecal\shu)$          |          $\Theta(\shu\Vcal\shu^2)$          |         $\Theta(\shu\Vcal\shu^2)$         |
|      ^       |   二叉堆   | $\Theta((\shu\Vcal\shu + \shu\Ecal\shu) \lg \shu\Vcal\shu)$ | $\Theta(\shu\Vcal\shu^2 \lg \shu\Vcal\shu)$ | $\Theta(\shu\Vcal\shu \lg \shu\Vcal\shu)$ |
|      ^       | 斐波那契堆 |  $\Theta(\shu\Vcal\shu \lg \shu\Vcal\shu + \shu\Ecal\shu)$  |          $\Theta(\shu\Vcal\shu^2)$          | $\Theta(\shu\Vcal\shu \lg \shu\Vcal\shu)$ |

</div>
