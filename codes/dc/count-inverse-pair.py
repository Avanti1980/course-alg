import random


def bruteforce(a: list) -> int:
    n, count = len(a), 0
    for i in range(n):
        ai = a[i]
        for j in range(i + 1, n):
            if ai > a[j]:
                count += 1
    return count


def count_cross_inv(a: list, low: int, mid: int, high: int, temp: list) -> int:
    # a[low:mid+1]、a[mid+1:high+1]已排好序
    # 拷贝数据到临时数组
    temp[low:high+1] = a[low:high+1]

    # i = low -> mid
    # j = mid+1 -> high
    i, j, k, count = low, mid+1, low, 0
    while i <= mid and j <= high:
        if temp[i] <= temp[j]:  # 顺序对
            a[k] = temp[i]
            i += 1
        else:  # 逆序对
            a[k] = temp[j]
            j += 1
            count += (mid + 1 - i)
        k += 1

    if i <= mid:  # 拷贝 left 的剩余元素
        a[k:high+1] = temp[i:mid+1]

    return count


def sort_and_count(a: list, low: int, high: int, temp: list) -> int:
    if low < high:
        mid = (low + high) // 2  # 取中间点分开
        count = 0
        count += sort_and_count(a, low, mid, temp)
        count += sort_and_count(a, mid + 1, high, temp)
        if a[mid] > a[mid+1]:
            count += count_cross_inv(a, low, mid, high, temp)
        return count
    else:
        return 0


a = [random.randint(0, 10000) for _ in range(1000)]
n = len(a)
temp = [0] * n
print(bruteforce(a), sort_and_count(a, 0, n-1, temp))
