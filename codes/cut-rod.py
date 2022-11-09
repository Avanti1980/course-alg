def qiege_digui1(p, n):  # 双递归
    if n == 0:
        return 0
    else:
        res = p[n]  # 取不切割和切割之间的最大值
        for i in range(1, n):  # 切割的价格由两段被分割的部分分别递归得到
            res = max(res, qiege_digui1(p, n-i)+qiege_digui1(p, i))
    return res


def qiege_digui2(p, n):  # 单递归
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1, n):  # 切割的都有一个最小量级，始终可视为切两半之后，一半保持不变
            res = max(res, p[i]+qiege_digui2(p, n-i))  # 另一半继续递归价格
    return res


def cut_rod_dp(p, n):  # 函数返回：切割长度为 n 的钢条所得的最大收益
    if n == 0:
        return 0
    q = -1
    for i in range(1, n+1):
        q = max(q, p[i] + CutRod(p, n-i))
        '''
        tmp = p[i] + CutRod(p, n-i)
        if q < tmp:
            q = tmp
        '''
    return q


p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]   # 价格表，下标为对应的钢条长度，如当钢条长度为0时，p=0,即p[0]=0，p[2]=5
print("最大收益为：", CutRod(p, 7))  # 最大收益为： 10
