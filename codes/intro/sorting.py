from typing import List


def bubble_sort(a: List[int]) -> None:
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):  # 从后往前遍历，将较小的元素像气泡一样浮到前面
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]


def bubble_sort_opt(a: List[int]) -> None:
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1, i, -1):  # 从后往前遍历，将较小的元素像气泡一样浮到前面
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
                swapped = True
        if not swapped:
            break


def selection_sort(a: List[int]) -> None:
    n = len(a)
    for i in range(n - 1):
        smallest = i
        for j in range(i + 1, n):
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
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


def merge(a: List[int], low: int, mid: int, high: int) -> None:
    # 拷贝数据到临时数组
    left = a[low:mid + 1]
    right = a[mid + 1:high + 1]

    i, j, k = 0, 0, low

    # 归并 left 和 right 到 a[low,...,high]
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1

    if i < len(left):  # 拷贝 left 的剩余元素
        a[k:high + 1] = left[i:]
    else:  # 拷贝 right 的剩余元素
        a[k:high + 1] = right[j:]


def merge_sort(a: List[int], low: int = 0, high: int = None) -> None:
    if high is None:
        high = len(a) - 1
    if low < high:
        # 分：计算分解的中间点
        mid = (low + high) // 2
        # 治：递归调用
        merge_sort(a, low, mid)
        merge_sort(a, mid + 1, high)
        # 合：合并已排好序的两个子数组
        merge(a, low, mid, high)


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


def quick_sort(a: List[int], low: int = 0, high: int = None) -> None:
    if high is None:
        high = len(a) - 1
    if low < high:
        # 分：计算主元位置并将其它元素挪到主元左右
        m = partition(a, low, high)
        # 治：递归调用
        quick_sort(a, low, m - 1)
        quick_sort(a, m + 1, high)


if __name__ == "__main__":
    sorting = [bubble_sort, selection_sort,
               insertion_sort, merge_sort, quick_sort]
    for s in sorting:
        a = [5, 2, 4, 6, 1, 3]
        s(a)
        print(a)
