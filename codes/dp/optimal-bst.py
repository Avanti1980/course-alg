from decimal import Decimal
INF = float("inf")


def obst(p: list[float], q: list[float]) -> tuple[list[list[float]], list[list[float]], list[list[int]]]:
    n = len(p)
    e: list[list[float]] = [[INF] * (n+1) for _ in range(n+2)]
    w: list[list[float]] = [[0] * (n+1) for _ in range(n+2)]
    r: list[list[int]] = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1, n + 2):
        e[i][i - 1] = w[i][i - 1] = q[i - 1]         # 边界情况
    for l in range(1, n + 1):                        # 子问题 l = 1 -> n
        for i in range(1, n - l + 2):                # 从第i个关键字
            j = i + l - 1                            # 到第j个关键字
            w[i][j] = w[i][j - 1] + p[j - 1] + q[j]  # 填写w表
            for t in range(i, j + 1):                # 遍历寻找最优根结点
                cost = e[i][t - 1] + e[t + 1][j] + w[i][j]
                if cost < e[i][j]:
                    e[i][j] = cost  # 更新期望搜索代价
                    r[i][j] = t     # 更新最优根结点
    return e, w, r


p = [Decimal("0.15"), Decimal("0.10"), Decimal("0.05"),
     Decimal("0.10"), Decimal("0.20")]
q = [Decimal("0.05"), Decimal("0.10"), Decimal("0.05"),
     Decimal("0.05"), Decimal("0.05"), Decimal("0.10")]
e, w, r = obst(p, q)
print(e[1][-1])
print("************* e *************")
for row in e[1:]:
    print(*[f"{item:<4}" for item in row])
print("************* w *************")
for row in w[1:]:
    print(*[f"{item:<4}" for item in row])
print("*** r ***")
for row in r[1:]:
    print(*[f"{item:<1}" for item in row[1:]])
# --------------------------------------------------------
# 2.75
# ************* e *************
# 0.05 0.45 0.90 1.25 1.75 2.75
# inf  0.10 0.40 0.70 1.20 2.00
# inf  inf  0.05 0.25 0.60 1.30
# inf  inf  inf  0.05 0.30 0.90
# inf  inf  inf  inf  0.05 0.50
# inf  inf  inf  inf  inf  0.10
# ************* w *************
# 0.05 0.30 0.45 0.55 0.70 1.00
# 0    0.10 0.25 0.35 0.50 0.80
# 0    0    0.05 0.15 0.30 0.60
# 0    0    0    0.05 0.20 0.50
# 0    0    0    0    0.05 0.35
# 0    0    0    0    0    0.10
# *** r ***
# 1 1 2 2 2
# 0 2 2 2 4
# 0 0 3 4 5
# 0 0 0 4 5
# 0 0 0 0 5


def restore_obst(r, i: int, j: int) -> None:
    if i > j:  # 伪关键字
        return {"key": 0, "pseudo": j, "left": None, "right": None}

    k = r[i][j]  # 关键字
    return {
        "key": k,
        "left": restore_obst(r, i, k - 1),
        "right": restore_obst(r, k + 1, j)
    }


def print_obst(node: dict, depth: int = 0) -> None:
    if node is None:
        return

    print_obst(node["right"], depth + 1)  # 递归打印右子树
    # 打印当前结点
    if node["key"] == 0:  # 伪关键字
        print("    " * depth + f"d{node['pseudo']}")
    else:  # 关键字
        print("    " * depth + f"k{node['key']}")
    print_obst(node["left"], depth + 1)  # 递归打印左子树


print("逆时针旋转 90° 打印：")
print_obst(restore_obst(r, 1, len(p)))
# --------------------------------------------------------
# 逆时针旋转 90° 打印：
#         d5
#     k5
#             d4
#         k4
#                 d3
#             k3
#                 d2
# k2
#         d1
#     k1
#         d0
