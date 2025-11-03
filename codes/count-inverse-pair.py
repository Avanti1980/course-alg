import random


def bruteforce(a):
    n, count = len(a), 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                count += 1
    return count


def count_cross_inv(a, l, m, r):
    n1, n2 = m - l + 1, r - m  # 子数组的长度
    L, R = [0] * n1, [0] * n2  # 创建临时数组

    for i in range(0, n1):  # 拷贝数据到临时数组L
        L[i] = a[l + i]

    for j in range(0, n2):  # 拷贝数据到临时数组R
        R[j] = a[m + 1 + j]

    count = 0
    i, j, k = 0, 0, l
    while i < n1 and j < n2:  # 归并L和R到a[l..r]
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
            count += (n1 - i)
        k += 1

    while i < n1:  # 拷贝L的剩余元素
        a[k] = L[i]
        i += 1
        k += 1

    while j < n2:  # 拷贝R的剩余元素
        a[k] = R[j]
        j += 1
        k += 1

    return count


def sort_and_count(a, l, r):
    if l < r:
        m = int((l + r) / 2)  # 取中间点分开
        left_inv = sort_and_count(a, l, m)
        right_inv = sort_and_count(a, m + 1, r)
        cross_inv = count_cross_inv(a, l, m, r)
        return left_inv + right_inv + cross_inv
    else:
        return 0


a = [x for x in range(1000)]
random.shuffle(a)
print(bruteforce(a))
print(sort_and_count(a, 0, len(a) - 1))
