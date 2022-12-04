def not_attack(queen, row, col):  # 不会被攻击吗？
    for i in range(row):  # 遍历已在棋盘上的皇后
        # 在同一列 或 在同一个斜角线
        if queen[i] == col or abs(row - i) == abs(queen[i] - col):
            return False
    return True


def nqueen(queen):
    count = row = 0
    queen[row] = 0                   # 先将皇后1放在第1列
    while row >= 0:                  # 全部结点都检测完后会回溯到-1行
        if queen[row] < n:           # 当前行未检测到最后一列
            if not_attack(queen, row, queen[row]):  # 当前位置不会被攻击
                if row == n-1:       # 已到最后一行
                    count += 1       # 解计数+1
                    print(queen)     # 输出
                    row -= 1         # 返回上一行
                    queen[row] += 1  # 上一行的皇后右移一格
                else:
                    row += 1         # 考虑下一行的皇后右移一格
                    queen[row] = 0   # 将下一行的皇后放在第1列
            else:                    # 当前位置不合法，探测当前行的下一个位置
                queen[row] += 1
        else:                        # 当前行已检测到最后一列
            row -= 1                 # 返回上一行
            queen[row] += 1          # 上一行的皇后右移一格
    return count


def nqueen_rec(queen, row):
    for col in range(n):                 # 遍历n个可放位置
        if not_attack(queen, row, col):  # 若(row, col)位置不会被攻击
            queen[row] = col
            if row == n - 1:             # 若是最后一个皇后 输出
                print(queen)
            else:
                nqueen_rec(queen, row + 1)


n = 4
queen = [None for i in range(n)]
print(nqueen(queen))

queen = [None for i in range(n)]
nqueen_rec(queen, 0)
--------------------------------
[1, 3, 0, 2]
[2, 0, 3, 1]
2
[1, 3, 0, 2]
[2, 0, 3, 1]