def bubble_sort(a, n):
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]


def selection_sort(a, n):
    for i in range(n - 1):
        smallest = i
        for j in range(i + 1, n):
            if a[j] < a[smallest]:
                smallest = j
        a[i], a[smallest] = a[smallest], a[i]


def insertion_sort(a, n):
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


def merge(a, low, mid, high):

    # 子数组的长度
    n1, n2 = mid - low + 1, high - mid

    # 创建临时数组
    L, R = [0] * n1, [0] * n2

    # 拷贝数据到临时数组L
    for i in range(n1):
        L[i] = a[low + i]

    # 拷贝数据到临时数组R
    for j in range(n2):
        R[j] = a[mid + 1 + j]

    i, j, k = 0, 0, low

    # 归并L和R到a[low,...,high]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1

    # 拷贝L的剩余元素
    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1

    # 拷贝R的剩余元素
    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1


def merge_sort(a, low, high):
    if low < high:
        mid = int((low + high) / 2)  # 中间点
        merge_sort(a, low, mid)
        merge_sort(a, mid + 1, high)
        merge(a, low, mid, high)


def partition(a, low, high):

    # 最右元素作为主元
    pivot = a[high]

    # 小于主元的元素的存放位置 初始为最左
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


def quick_sort(a, low, high):
    if low < high:
        m = partition(a, low, high)
        quick_sort(a, low, m - 1)
        quick_sort(a, m + 1, high)


a = [5, 2, 4, 6, 1, 3]
bubble_sort(a, len(a))
print(a)

a = [5, 2, 4, 6, 1, 3]
selection_sort(a, len(a))
print(a)

a = [5, 2, 4, 6, 1, 3]
insertion_sort(a, len(a))
print(a)

a = [5, 2, 4, 6, 1, 3]
merge_sort(a, 0, len(a) - 1)
print(a)

a = [5, 2, 4, 6, 1, 3]
quick_sort(a, 0, len(a) - 1)
print(a)
