def available(row, col):
    """检查当前位置是否合法"""
    for k in range(row):
        if queen[k] == col or queen[k]-col == k - row or queen[k]-col == row - k:
            return False
    return True


def find(n):
    """回溯法求解"""
    count = 0
    row = 0
    global queen
    queen[row] = 0
    while row >= 0:  # 当前行为 -1 时结束
        if row < n and queen[row] < n:  # 当前行、当前列均为到达最后
            if available(row, queen[row]):  # 当前位置合法，则探索下一行
                row += 1
                queen[row] = 0
            else:  # 当前位置不合法，探测当前行的下一个位置
                queen[row] += 1
        else:
            if row >= n:  # 当前行、当前列均到了最后，记录一个解
                count += 1
                # print(queen)
            row -= 1  # 返回上一行，继续探索
            queen[row] += 1
    return count


global queen
n = 8
queen = [-1]*(n+1)
print(find(n))

# 检测（x,y）这个位置是否合法（不会被其他皇后攻击到）


def is_attack(queue, x, y):
    for i in range(x):
        if queue[i] == y or abs(x - i) == abs(queue[i] - y):
            return True
    return False


# 按列来摆放皇后
def put_position(n, queue, col):
    for i in range(n):
        if not is_attack(queue, col, i):
            queue[col] = i
            if col == n - 1:    # 此时最后一个皇后摆放好了，打印结果。
                print(queue)
            else:
                put_position(n, queue, col + 1)


n = 4       # 这里是n 就是n皇后
queue = [None for i in range(n)]        # 存储皇后位置的一维数组，数组下标表示皇后所在的列，下标对应的值为皇后所在的行。
put_position(n, queue, 0)
