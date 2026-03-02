import random


def bruteforce(a):
    n, count = len(a), 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                count += 1
    return count


def count_cross_inv(a, low, mid, high):
    n1, n2 = mid - low + 1, high - mid  # 子数组的长度
    L, R = [0] * n1, [0] * n2  # 创建临时数组

    for i in range(0, n1):  # 拷贝数据到临时数组L
        L[i] = a[low + i]

    for j in range(0, n2):  # 拷贝数据到临时数组R
        R[j] = a[mid + 1 + j]

    count = 0
    i, j, k = 0, 0, low
    while i < n1 and j < n2:  # 归并L和R到a[low,...,high]
        if L[i] <= R[j]:      # 跨越中点的顺序对
            a[k] = L[i]
            i += 1
        else:                 # 跨越中点的逆序对
            a[k] = R[j]
            j += 1
            count += (n1 - i)  # L[i], ..., L[n1-1]均与R[j]构成逆序对
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


def sort_and_count(a, low, high):
    if low < high:
        mid = int((low + high) / 2)  # 取中间点分开
        left_inv = sort_and_count(a, low, mid)
        right_inv = sort_and_count(a, mid + 1, high)
        cross_inv = count_cross_inv(a, low, mid, high)
        return left_inv + right_inv + cross_inv
    else:
        return 0


a = [x for x in range(1000)]
random.shuffle(a)
print(bruteforce(a))
print(sort_and_count(a, 0, len(a) - 1))
