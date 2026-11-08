from typing import List


def bubble_sort(a: List[int]) -> None:
    n = len(a)
    for i in range(n-1):
        for j in range(n-1, i, -1):  # 从后往前遍历，将较小的元素像气泡一样浮到前面
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]


def bubble_sort_opt(a: List[int]) -> None:
    n = len(a)
    for i in range(n-1):
        swapped = False
        for j in range(n-1, i, -1):  # 从后往前遍历，将较小的元素像气泡一样浮到前面
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
                swapped = True
        if not swapped:
            break


def selection_sort(a: List[int]) -> None:
    n = len(a)
    for i in range(n-1):
        smallest = i
        for j in range(i+1, n):
            if a[j] < a[smallest]:
                smallest = j
        if smallest != i:  # 只有当最小元素不是当前元素时才交换
            a[i], a[smallest] = a[smallest], a[i]


def insertion_sort(a: List[int]) -> None:
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key


def merge(a: List[int], low: int, mid: int, high: int, temp: List[int]) -> None:
    # a[low:mid+1]、a[mid+1:high+1]已排好序
    # 拷贝数据到临时数组
    temp[low:high+1] = a[low:high+1]

    # i = low -> mid
    # j = mid+1 -> high
    i, j, k = low, mid+1, low
    while i <= mid and j <= high:
        if temp[i] <= temp[j]:
            a[k] = temp[i]
            i += 1
        else:
            a[k] = temp[j]
            j += 1
        k += 1

    if i <= mid:  # 拷贝 left 的剩余元素
        a[k:high+1] = temp[i:mid+1]


def merge_sort(a: List[int], low: int, high: int, temp: List[int]) -> None:
    if low < high:
        # 分：计算分解的中间点
        mid = (low + high) // 2
        # 治：递归调用
        merge_sort(a, low, mid, temp)
        merge_sort(a, mid+1, high, temp)
        # 合：合并已排好序的两个子数组
        merge(a, low, mid, high, temp)


def partition(a: List[int], low: int, high: int) -> int:
    pivot = a[high]  # 最右元素作为主元

    # i指向小于主元的元素的存放位置 初始为最左
    i = low

    # low -> high-1 遍历其它元素
    for j in range(low, high):
        if a[j] <= pivot:
            # 小于主元的元素放到主元左边
            a[i], a[j] = a[j], a[i]
            i += 1  # 存放位置右移一位

    # 所有小于主元的元素已位于主元左边
    # 当前的i就是主元应该放的位置
    # 当前的a[i]大于主元
    a[i], a[high] = a[high], a[i]

    return i


def quick_sort(a: List[int], low: int, high: int) -> None:
    if low < high:
        # 分：计算主元位置并将其它元素挪到主元左右
        m = partition(a, low, high)
        # 治：递归调用
        quick_sort(a, low, m-1)
        quick_sort(a, m+1, high)


if __name__ == "__main__":

    import random

    random.seed(2026)
    a = [random.randint(0, 100) for _ in range(10)]

    sorting = [bubble_sort, selection_sort, insertion_sort]
    for s in sorting:
        b = a[:]
        s(b)
        print(b)

    b = a[:]
    n = len(b)
    temp = [0] * n
    merge_sort(b, 0, n-1, temp)
    print(b)

    b = a[:]
    quick_sort(b, 0, n-1)
    print(b)
